from __future__ import annotations

import argparse
import csv
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


EPISODE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = (
    EPISODE_DIR
    / "03-visuals"
    / "perler-request-green-haired-fairy"
    / "source-reference.jpg"
)
DEFAULT_OUTPUT_DIR = (
    EPISODE_DIR / "03-visuals" / "perler-request-green-haired-fairy"
)
DEFAULT_PALETTE = (
    EPISODE_DIR
    / "01-research"
    / "mard-221-artkal-m-2.6mm-rgb-2025.csv"
)

# Normalized source-image boxes. These protect the multicolor irises from
# losing their highlights during global palette reduction.
EYE_BOXES = (
    (0.405, 0.400, 0.545, 0.555),
    (0.555, 0.380, 0.705, 0.535),
)
EYE_COMPARISON_BOX = (0.375, 0.345, 0.725, 0.585)


@dataclass(frozen=True)
class PaletteColor:
    short_code: str
    official_code: str
    rgb: tuple[int, int, int]
    hex_color: str
    lab: tuple[float, float, float]


def rgb_to_lab(color: tuple[int, int, int]) -> tuple[float, float, float]:
    linear: list[float] = []
    for value in color:
        channel = value / 255
        linear.append(
            channel / 12.92
            if channel <= 0.04045
            else ((channel + 0.055) / 1.055) ** 2.4
        )
    red, green, blue = linear
    x = (0.4124564 * red + 0.3575761 * green + 0.1804375 * blue) / 0.95047
    y = 0.2126729 * red + 0.7151522 * green + 0.0721750 * blue
    z = (0.0193339 * red + 0.1191920 * green + 0.9503041 * blue) / 1.08883

    def pivot(value: float) -> float:
        delta = 6 / 29
        if value > delta**3:
            return value ** (1 / 3)
        return value / (3 * delta**2) + 4 / 29

    fx, fy, fz = pivot(x), pivot(y), pivot(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def color_distance(
    left: tuple[float, float, float],
    right: tuple[float, float, float],
) -> float:
    return sum((a - b) ** 2 for a, b in zip(left, right))


def load_palette(path: Path) -> list[PaletteColor]:
    colors: list[PaletteColor] = []
    transparent_count = 0
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            short_code = row["短色号"]
            official_code = row["官方色号"]
            bead_type = row["类型"]
            if official_code != f"M{short_code}":
                raise ValueError(f"Unexpected official code: {official_code}")
            if bead_type == "transparent":
                transparent_count += 1
                continue
            rgb = (int(row["R"]), int(row["G"]), int(row["B"]))
            hex_color = row["HEX"].upper()
            if hex_color != f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}":
                raise ValueError(f"RGB/HEX mismatch for {short_code}")
            colors.append(
                PaletteColor(
                    short_code=short_code,
                    official_code=official_code,
                    rgb=rgb,
                    hex_color=hex_color,
                    lab=rgb_to_lab(rgb),
                )
            )
    if len(colors) != 220 or transparent_count != 1:
        raise ValueError("Expected 220 opaque colors and one transparent color")
    return colors


def square_crop(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    width, height = image.size
    side = min(width, height)
    left = (width - side) // 2
    top = (height - side) // 2
    return image.crop((left, top, left + side, top + side))


def prepare_grid_image(source: Image.Image, size: int) -> Image.Image:
    image = square_crop(source)
    image = image.resize((size, size), Image.Resampling.LANCZOS)
    image = ImageEnhance.Contrast(image).enhance(1.055)
    image = ImageEnhance.Color(image).enhance(1.035)
    return image.filter(
        ImageFilter.UnsharpMask(radius=0.72, percent=145, threshold=2)
    )


def normalized_box(
    box: tuple[float, float, float, float], size: int
) -> tuple[int, int, int, int]:
    return (
        round(box[0] * size),
        round(box[1] * size),
        round(box[2] * size),
        round(box[3] * size),
    )


def median_cut_centers(image: Image.Image, count: int) -> list[tuple[int, int, int]]:
    quantized = image.quantize(
        colors=count,
        method=Image.Quantize.MEDIANCUT,
        dither=Image.Dither.NONE,
    )
    palette = quantized.getpalette()
    histogram = quantized.getcolors(maxcolors=256) or []
    centers: list[tuple[int, int, int]] = []
    for _, index in sorted(histogram, reverse=True):
        offset = index * 3
        centers.append(tuple(palette[offset : offset + 3]))
    return centers


def build_eye_montage(image: Image.Image) -> Image.Image:
    crops: list[Image.Image] = []
    for box in EYE_BOXES:
        crop = image.crop(normalized_box(box, image.width))
        crops.append(crop.resize((crop.width * 6, crop.height * 6)))
    width = sum(crop.width for crop in crops)
    height = max(crop.height for crop in crops)
    montage = Image.new("RGB", (width, height), "white")
    x = 0
    for crop in crops:
        montage.paste(crop, (x, 0))
        x += crop.width
    return montage


def nearest_palette_color(
    rgb: tuple[int, int, int], palette: list[PaletteColor]
) -> PaletteColor:
    lab = rgb_to_lab(rgb)
    return min(palette, key=lambda item: color_distance(lab, item.lab))


def select_mard_colors(
    image: Image.Image,
    palette: list[PaletteColor],
    global_count: int,
    eye_count: int,
) -> tuple[list[PaletteColor], list[PaletteColor]]:
    global_centers = median_cut_centers(image, global_count)
    eye_centers = median_cut_centers(build_eye_montage(image), eye_count)

    def mapped_unique(centers: list[tuple[int, int, int]]) -> list[PaletteColor]:
        result: list[PaletteColor] = []
        seen: set[str] = set()
        for center in centers:
            match = nearest_palette_color(center, palette)
            if match.short_code not in seen:
                result.append(match)
                seen.add(match.short_code)
        return result

    global_colors = mapped_unique(global_centers)
    eye_colors = mapped_unique(eye_centers)

    # Keep one very dark and one near-white option available for crisp outlines
    # and catchlights even if median-cut merges their tiny source regions.
    for sample in ((12, 20, 58), (250, 250, 252)):
        match = nearest_palette_color(sample, palette)
        if all(item.short_code != match.short_code for item in global_colors):
            global_colors.append(match)
    return global_colors, eye_colors


def inside_eye(x: int, y: int, size: int) -> bool:
    for box in EYE_BOXES:
        left, top, right, bottom = normalized_box(box, size)
        if left <= x < right and top <= y < bottom:
            return True
    return False


def build_grid(
    image: Image.Image,
    global_colors: list[PaletteColor],
    eye_colors: list[PaletteColor],
) -> list[list[str]]:
    global_by_rgb = {item.rgb: item for item in global_colors}
    eye_union = list(global_colors)
    seen = set(global_by_rgb)
    for item in eye_colors:
        if item.rgb not in seen:
            eye_union.append(item)
            seen.add(item.rgb)

    global_cache: dict[tuple[int, int, int], str] = {}
    eye_cache: dict[tuple[int, int, int], str] = {}
    pixels = image.load()
    grid: list[list[str]] = []
    for y in range(image.height):
        row: list[str] = []
        for x in range(image.width):
            rgb = pixels[x, y]
            if inside_eye(x, y, image.width):
                if rgb not in eye_cache:
                    eye_cache[rgb] = nearest_palette_color(rgb, eye_union).short_code
                row.append(eye_cache[rgb])
            else:
                if rgb not in global_cache:
                    global_cache[rgb] = nearest_palette_color(
                        rgb, global_colors
                    ).short_code
                row.append(global_cache[rgb])
        grid.append(row)
    return grid


def code_sort_key(code: str) -> tuple[str, int]:
    match = re.fullmatch(r"([A-Z]+)(\d+)", code)
    if not match:
        return code, 0
    return match.group(1), int(match.group(2))


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def readable_text_color(rgb: tuple[int, int, int]) -> str:
    luminance = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
    return "#FFFFFF" if luminance < 132 else "#11151A"


def grid_to_image(
    grid: list[list[str]], palette_by_code: dict[str, PaletteColor]
) -> Image.Image:
    height = len(grid)
    width = len(grid[0])
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            pixels[x, y] = palette_by_code[code].rgb
    return image


def write_csvs(
    grid: list[list[str]],
    palette_by_code: dict[str, PaletteColor],
    output_dir: Path,
    stem: str,
) -> Counter[str]:
    counts: Counter[str] = Counter(code for row in grid for code in row)
    with (output_dir / f"{stem}-pattern.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["行/列", *range(1, len(grid[0]) + 1)])
        for row_number, row in enumerate(grid, start=1):
            writer.writerow([row_number, *row])

    with (output_dir / f"{stem}-palette.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            ["色号体系", "图纸短色号", "官方完整色号", "RGB", "HEX", "数量"]
        )
        for code in sorted(counts, key=code_sort_key):
            item = palette_by_code[code]
            writer.writerow(
                [
                    "MARD 221 / Artkal M-2.6mm",
                    code,
                    item.official_code,
                    ",".join(str(value) for value in item.rgb),
                    item.hex_color,
                    counts[code],
                ]
            )
    return counts


def render_pixel_preview(
    grid: list[list[str]],
    palette_by_code: dict[str, PaletteColor],
    output_dir: Path,
    stem: str,
) -> Image.Image:
    pixel_image = grid_to_image(grid, palette_by_code)
    scale = max(8, 960 // pixel_image.width)
    preview = pixel_image.resize(
        (pixel_image.width * scale, pixel_image.height * scale),
        Image.Resampling.NEAREST,
    )
    preview.save(output_dir / f"{stem}-pixel-preview.png")
    return pixel_image


def render_numbered_pattern(
    grid: list[list[str]],
    counts: Counter[str],
    palette_by_code: dict[str, PaletteColor],
    output_dir: Path,
    stem: str,
    cell_size: int,
) -> None:
    grid_height = len(grid)
    grid_width = len(grid[0])
    grid_width_px = grid_width * cell_size
    grid_height_px = grid_height * cell_size
    coordinate_band = max(34, cell_size)
    header_height = 122
    used_codes = sorted(counts, key=code_sort_key)
    width = grid_width_px + coordinate_band * 2
    legend_columns = max(6, min(12, (width - 40) // 235))
    legend_rows = math.ceil(len(used_codes) / legend_columns)
    legend_height = 96 + legend_rows * 84 + 96
    height = (
        header_height
        + coordinate_band
        + grid_height_px
        + coordinate_band
        + legend_height
    )

    canvas = Image.new("RGB", (width, height), "#F6F7F9")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(38, bold=True)
    subtitle_font = load_font(19)
    coordinate_font = load_font(max(9, round(cell_size * 0.31)), bold=True)
    code_font = load_font(max(10, round(cell_size * 0.34)), bold=True)
    legend_font = load_font(17, bold=True)
    count_font = load_font(15)
    note_font = load_font(17)

    draw.text(
        (coordinate_band, 15),
        f"绿发星灵拼豆图纸｜{grid_width}×{grid_height} MARD 221 实做版",
        fill="#101318",
        font=title_font,
    )
    draw.text(
        (coordinate_band, 69),
        "格内为 MARD 221 短色号；采购表同时提供 Artkal M-2.6mm 官方完整色号。",
        fill="#535B65",
        font=subtitle_font,
    )

    origin_x = coordinate_band
    origin_y = header_height + coordinate_band
    band_color = "#D9E1EC"

    draw.rectangle(
        (origin_x, origin_y, origin_x + grid_width_px, origin_y + grid_height_px),
        fill="#FFFFFF",
    )
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            item = palette_by_code[code]
            x0 = origin_x + x * cell_size
            y0 = origin_y + y * cell_size
            draw.rectangle(
                (x0, y0, x0 + cell_size, y0 + cell_size),
                fill=item.rgb,
            )
            draw.text(
                (x0 + cell_size / 2, y0 + cell_size / 2),
                code,
                anchor="mm",
                fill=readable_text_color(item.rgb),
                font=code_font,
            )

    for index in range(grid_width + 1):
        x = origin_x + index * cell_size
        heavy = index % 10 == 0
        draw.line(
            (x, origin_y, x, origin_y + grid_height_px),
            fill="#1C2025" if heavy else "#6E747B",
            width=3 if heavy else 1,
        )
    for index in range(grid_height + 1):
        y = origin_y + index * cell_size
        heavy = index % 10 == 0
        draw.line(
            (origin_x, y, origin_x + grid_width_px, y),
            fill="#1C2025" if heavy else "#6E747B",
            width=3 if heavy else 1,
        )

    top_y = header_height
    bottom_y = origin_y + grid_height_px
    right_x = origin_x + grid_width_px
    draw.rectangle((origin_x, top_y, right_x, origin_y), fill=band_color)
    draw.rectangle(
        (origin_x, bottom_y, right_x, bottom_y + coordinate_band),
        fill=band_color,
    )
    draw.rectangle((0, origin_y, origin_x, bottom_y), fill=band_color)
    draw.rectangle(
        (right_x, origin_y, right_x + coordinate_band, bottom_y),
        fill=band_color,
    )

    for index in range(grid_width):
        x = origin_x + index * cell_size + cell_size / 2
        label = str(index + 1)
        draw.text(
            (x, top_y + coordinate_band / 2),
            label,
            anchor="mm",
            fill="#11151A",
            font=coordinate_font,
        )
        draw.text(
            (x, bottom_y + coordinate_band / 2),
            label,
            anchor="mm",
            fill="#11151A",
            font=coordinate_font,
        )
    for index in range(grid_height):
        y = origin_y + index * cell_size + cell_size / 2
        label = str(index + 1)
        draw.text(
            (coordinate_band / 2, y),
            label,
            anchor="mm",
            fill="#11151A",
            font=coordinate_font,
        )
        draw.text(
            (right_x + coordinate_band / 2, y),
            label,
            anchor="mm",
            fill="#11151A",
            font=coordinate_font,
        )

    legend_top = bottom_y + coordinate_band + 28
    draw.text(
        (24, legend_top),
        f"共 {sum(counts.values()):,} 颗，使用 {len(used_codes)} 种色号",
        fill="#11151A",
        font=note_font,
    )
    legend_top += 45
    item_width = (width - 40) / legend_columns
    for index, code in enumerate(used_codes):
        column = index % legend_columns
        row = index // legend_columns
        item = palette_by_code[code]
        x = 20 + column * item_width
        y = legend_top + row * 84
        swatch_width = min(78, item_width - 16)
        draw.rectangle(
            (x, y, x + swatch_width, y + 46),
            fill=item.rgb,
            outline="#4F565E",
            width=1,
        )
        draw.text(
            (x + swatch_width / 2, y + 23),
            code,
            anchor="mm",
            fill=readable_text_color(item.rgb),
            font=legend_font,
        )
        draw.text(
            (x + swatch_width / 2, y + 65),
            str(counts[code]),
            anchor="mm",
            fill="#252A31",
            font=count_font,
        )

    note_y = legend_top + legend_rows * 84 + 7
    physical_width = grid_width * 2.6 / 10
    physical_height = grid_height * 2.6 / 10
    draw.text(
        (24, note_y),
        f"按 2.6mm 豆距，成品约 {physical_width:.1f}×{physical_height:.1f} cm。",
        fill="#545C66",
        font=note_font,
    )
    draw.text(
        (24, note_y + 32),
        "电子 RGB 只用于匹配；采购前请用同品牌实体色卡复核。H1 透明豆未参与匹配。",
        fill="#6A727B",
        font=note_font,
    )
    canvas.save(output_dir / f"{stem}-numbered-pattern.png")


def render_eye_comparison(
    source: Image.Image,
    pixel_images: dict[int, Image.Image],
    output_dir: Path,
) -> None:
    panel_width = 720
    panel_height = 520
    title_height = 66
    gap = 18
    labels = ["原图眼部", *[f"{size}×{size} 拼豆效果" for size in pixel_images]]
    panels: list[Image.Image] = []

    def fit_crop(crop: Image.Image, resample: Image.Resampling) -> Image.Image:
        scale = min(panel_width / crop.width, panel_height / crop.height)
        target = (
            max(1, round(crop.width * scale)),
            max(1, round(crop.height * scale)),
        )
        return crop.resize(target, resample)

    source_square = square_crop(source)
    source_crop = source_square.crop(
        normalized_box(EYE_COMPARISON_BOX, source_square.width)
    )
    source_crop = fit_crop(source_crop, Image.Resampling.LANCZOS)
    source_panel = Image.new("RGB", (panel_width, panel_height), "#FFFFFF")
    source_panel.paste(
        source_crop,
        ((panel_width - source_crop.width) // 2, (panel_height - source_crop.height) // 2),
    )
    panels.append(source_panel)

    for size, pixel_image in pixel_images.items():
        crop = pixel_image.crop(normalized_box(EYE_COMPARISON_BOX, size))
        crop = fit_crop(crop, Image.Resampling.NEAREST)
        panel = Image.new("RGB", (panel_width, panel_height), "#FFFFFF")
        panel.paste(
            crop,
            ((panel_width - crop.width) // 2, (panel_height - crop.height) // 2),
        )
        panels.append(panel)

    width = len(panels) * panel_width + (len(panels) - 1) * gap
    canvas = Image.new("RGB", (width, panel_height + title_height), "#EEF1F5")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(27, bold=True)
    for index, (panel, label) in enumerate(zip(panels, labels)):
        x = index * (panel_width + gap)
        draw.text(
            (x + panel_width / 2, title_height / 2),
            label,
            anchor="mm",
            fill="#15191E",
            font=title_font,
        )
        canvas.paste(panel, (x, title_height))
    canvas.save(output_dir / "green-fairy-eye-detail-comparison.png")


def write_readme(
    output_dir: Path,
    results: dict[int, Counter[str]],
) -> None:
    lines = [
        "# 绿发星灵拼豆图纸",
        "",
        "## 结论",
        "",
        "- `78×78` 是严格适配用户现有板子的版本。",
        "- `96×96` 是推荐版：双眼、睫毛和虹膜高光有更多格位，整体仍保持原图完整构图。",
        "- 两版均使用 MARD 221 短色号，并在采购 CSV 中给出 Artkal M-2.6mm 官方完整色号。",
        "",
        "## 文件",
        "",
    ]
    for size, counts in results.items():
        stem = f"green-fairy-{size}x{size}-mard221"
        lines.extend(
            [
                f"### {size}×{size}",
                "",
                f"- 像素效果：`{stem}-pixel-preview.png`",
                f"- 格内色号图：`{stem}-numbered-pattern.png`",
                f"- 逐格 CSV：`{stem}-pattern.csv`",
                f"- 采购色号与数量：`{stem}-palette.csv`",
                f"- 总豆数：{sum(counts.values()):,} 颗",
                f"- 使用色号：{len(counts)} 种",
                f"- 2.6mm 成品约：{size * 2.6 / 10:.1f}×{size * 2.6 / 10:.1f} cm",
                "",
            ]
        )
    lines.extend(
        [
            "## 眼睛处理",
            "",
            "全局配色之外，双眼区域单独提取局部色组，避免紫色睫毛、青绿虹膜、黄色高光和白色反光在降格时被背景色吞掉。对比图见 `green-fairy-eye-detail-comparison.png`。",
            "",
            "## 使用提醒",
            "",
            "- 原图由用户提供，原文件带平台账号水印；本交付仅按委托转换，不据此主张原画版权。公开发布或商用前需确认图片授权。",
            "- RGB 只能用于电子预览。不同屏幕和批次会有色差，采购前请用 MARD 221 / Artkal M-2.6mm 实体色卡复核。",
            "- `H1` 为透明豆，本图未使用。",
            "",
        ]
    )
    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def parse_sizes(raw: str) -> list[int]:
    sizes = [int(value.strip()) for value in raw.split(",") if value.strip()]
    if not sizes or any(size < 32 or size > 180 for size in sizes):
        raise argparse.ArgumentTypeError("sizes must be comma-separated values from 32 to 180")
    return sizes


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate eye-aware MARD 221 anime fuse-bead patterns."
    )
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--palette-csv", type=Path, default=DEFAULT_PALETTE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--sizes", type=parse_sizes, default=parse_sizes("78,96"))
    parser.add_argument("--global-colors", type=int, default=42)
    parser.add_argument("--eye-colors", type=int, default=28)
    parser.add_argument("--cell-size", type=int, default=34)
    args = parser.parse_args()

    if args.global_colors < 8 or args.eye_colors < 4:
        parser.error("palette sizes are too small")
    if args.cell_size < 28:
        parser.error("--cell-size must be at least 28")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    palette = load_palette(args.palette_csv.resolve())
    palette_by_code = {item.short_code: item for item in palette}

    results: dict[int, Counter[str]] = {}
    pixel_images: dict[int, Image.Image] = {}
    with Image.open(args.source.resolve()) as source:
        source.load()
        for size in args.sizes:
            prepared = prepare_grid_image(source, size)
            global_colors, eye_colors = select_mard_colors(
                prepared,
                palette,
                args.global_colors,
                args.eye_colors,
            )
            grid = build_grid(prepared, global_colors, eye_colors)
            stem = f"green-fairy-{size}x{size}-mard221"
            counts = write_csvs(grid, palette_by_code, output_dir, stem)
            pixel_images[size] = render_pixel_preview(
                grid, palette_by_code, output_dir, stem
            )
            render_numbered_pattern(
                grid,
                counts,
                palette_by_code,
                output_dir,
                stem,
                args.cell_size,
            )
            results[size] = counts
            print(
                f"Generated {size}x{size}: {sum(counts.values())} beads, "
                f"{len(counts)} colors"
            )
        render_eye_comparison(source, pixel_images, output_dir)

    write_readme(output_dir, results)


if __name__ == "__main__":
    main()
