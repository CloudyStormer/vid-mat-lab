from __future__ import annotations

import argparse
import csv
import math
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EPISODE_DIR = Path(__file__).resolve().parents[1]
SOURCE = (
    EPISODE_DIR
    / "03-visuals"
    / "perler-demo-v1"
    / "xiaoneihao-cool-source.png"
)
PALETTE_CSV = (
    EPISODE_DIR
    / "01-research"
    / "mard-221-artkal-m-2.6mm-rgb-2025.csv"
)
DEFAULT_OUTPUT_DIR = (
    EPISODE_DIR / "03-visuals" / "perler-demo-v4-mard-221-mini"
)


@dataclass(frozen=True)
class PaletteColor:
    short_code: str
    official_code: str
    rgb: tuple[int, int, int]
    hex_color: str
    lab: tuple[float, float, float]


def rgb_to_lab(color: tuple[int, int, int]) -> tuple[float, float, float]:
    """Convert sRGB to CIE L*a*b* using a D65 reference white."""

    linear = []
    for value in color:
        channel = value / 255
        linear.append(
            channel / 12.92
            if channel <= 0.04045
            else ((channel + 0.055) / 1.055) ** 2.4
        )
    red, green, blue = linear
    x = (0.4124564 * red + 0.3575761 * green + 0.1804375 * blue) / 0.95047
    y = (0.2126729 * red + 0.7151522 * green + 0.0721750 * blue) / 1.0
    z = (0.0193339 * red + 0.1191920 * green + 0.9503041 * blue) / 1.08883

    def pivot(value: float) -> float:
        delta = 6 / 29
        return (
            value ** (1 / 3)
            if value > delta**3
            else value / (3 * delta**2) + 4 / 29
        )

    fx, fy, fz = pivot(x), pivot(y), pivot(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def load_palette(path: Path) -> tuple[list[PaletteColor], dict[str, str]]:
    """Load all 221 codes, excluding transparent H1 from opaque auto-matching."""

    opaque: list[PaletteColor] = []
    type_by_code: dict[str, str] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            short_code = row["短色号"]
            official_code = row["官方色号"]
            bead_type = row["类型"]
            type_by_code[short_code] = bead_type
            if official_code != f"M{short_code}":
                raise ValueError(
                    f"Unexpected full code {official_code!r} for {short_code!r}"
                )
            if bead_type == "transparent":
                continue
            color = (int(row["R"]), int(row["G"]), int(row["B"]))
            hex_color = row["HEX"].upper()
            expected_hex = f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}"
            if hex_color != expected_hex:
                raise ValueError(
                    f"RGB/HEX mismatch for {short_code}: "
                    f"{color} versus {hex_color}"
                )
            opaque.append(
                PaletteColor(
                    short_code=short_code,
                    official_code=official_code,
                    rgb=color,
                    hex_color=hex_color,
                    lab=rgb_to_lab(color),
                )
            )
    if len(type_by_code) != 221:
        raise ValueError(f"Expected 221 MARD codes, found {len(type_by_code)}")
    if len(opaque) != 220 or type_by_code.get("H1") != "transparent":
        raise ValueError("Expected 220 opaque colors plus transparent H1")
    return opaque, type_by_code


def is_omitted_background(pixel: tuple[int, int, int]) -> bool:
    """Omit the pale-blue canvas and dark-navy decorative halo."""

    red, green, blue = pixel
    pale_blue = (
        red > 145
        and green > 170
        and blue > 190
        and blue - red > 13
        and blue - green > 4
    )
    navy_halo = (
        red < 75
        and green < 115
        and blue < 180
        and blue > red + 28
        and blue > green + 8
    )
    return pale_blue or navy_halo


def nearest_code(
    pixel: tuple[int, int, int],
    palette: list[PaletteColor],
) -> str:
    pixel_lab = rgb_to_lab(pixel)
    return min(
        palette,
        key=lambda entry: sum(
            (left - right) ** 2 for left, right in zip(pixel_lab, entry.lab)
        ),
    ).short_code


def build_grid(
    image: Image.Image,
    grid_width: int,
    grid_height: int,
    coverage_threshold: float,
    palette: list[PaletteColor],
) -> list[list[str]]:
    source = image.convert("RGB")
    source_width, source_height = source.size
    pixels = source.load()
    grid: list[list[str]] = []

    for grid_y in range(grid_height):
        row: list[str] = []
        y0 = round(grid_y * source_height / grid_height)
        y1 = round((grid_y + 1) * source_height / grid_height)
        for grid_x in range(grid_width):
            x0 = round(grid_x * source_width / grid_width)
            x1 = round((grid_x + 1) * source_width / grid_width)
            kept: list[tuple[int, int, int]] = []
            total = max(1, (x1 - x0) * (y1 - y0))
            for y in range(y0, y1):
                for x in range(x0, x1):
                    pixel = pixels[x, y]
                    if not is_omitted_background(pixel):
                        kept.append(pixel)
            if len(kept) / total < coverage_threshold:
                row.append("")
                continue
            average = tuple(
                round(sum(channel) / len(kept)) for channel in zip(*kept)
            )
            row.append(nearest_code(average, palette))
        grid.append(row)
    return grid


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path(
            "C:/Windows/Fonts/msyhbd.ttc"
            if bold
            else "C:/Windows/Fonts/msyh.ttc"
        ),
        Path(
            "C:/Windows/Fonts/arialbd.ttf"
            if bold
            else "C:/Windows/Fonts/arial.ttf"
        ),
        Path("/System/Library/Fonts/Hiragino Sans GB.ttc"),
        Path(
            "/System/Library/Fonts/STHeiti Medium.ttc"
            if bold
            else "/System/Library/Fonts/STHeiti Light.ttc"
        ),
        Path(
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
            if bold
            else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
        ),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def text_color(hex_color: str) -> str:
    red = int(hex_color[1:3], 16)
    green = int(hex_color[3:5], 16)
    blue = int(hex_color[5:7], 16)
    luminance = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    return "#FFFFFF" if luminance < 125 else "#15171A"


def write_csvs(
    grid: list[list[str]],
    counts: Counter[str],
    palette: list[PaletteColor],
    output_dir: Path,
    stem: str,
) -> None:
    grid_width = len(grid[0])
    grid_height = len(grid)
    with (output_dir / f"{stem}-pattern.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["row/col", *range(1, grid_width + 1)])
        for index, row in enumerate(grid, start=1):
            writer.writerow([index, *row])

    palette_by_code = {entry.short_code: entry for entry in palette}
    ordered_codes = sorted(counts, key=lambda code: (-counts[code], code))
    with (output_dir / f"{stem}-palette.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "色号体系",
                "图纸短色号",
                "官方完整色号",
                "官方RGB参考",
                "HEX",
                "数量",
            ]
        )
        for code in ordered_codes:
            entry = palette_by_code[code]
            writer.writerow(
                [
                    "MARD 221 / Artkal M-2.6mm",
                    code,
                    entry.official_code,
                    ",".join(str(value) for value in entry.rgb),
                    entry.hex_color,
                    counts[code],
                ]
            )


def render_preview(
    grid: list[list[str]],
    palette: list[PaletteColor],
    output_dir: Path,
    stem: str,
) -> None:
    grid_height = len(grid)
    grid_width = len(grid[0])
    scale = max(10, min(20, 1920 // max(grid_width, grid_height)))
    preview = Image.new(
        "RGBA",
        (grid_width * scale, grid_height * scale),
        (0, 0, 0, 0),
    )
    draw = ImageDraw.Draw(preview)
    colors = {entry.short_code: entry.hex_color for entry in palette}
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            if code:
                draw.rectangle(
                    (
                        x * scale,
                        y * scale,
                        (x + 1) * scale - 1,
                        (y + 1) * scale - 1,
                    ),
                    fill=colors[code],
                )
    preview.save(output_dir / f"{stem}-pixel-preview.png")


def render_numbered_pattern(
    grid: list[list[str]],
    counts: Counter[str],
    palette: list[PaletteColor],
    output_dir: Path,
    stem: str,
    cell_size: int,
) -> None:
    grid_height = len(grid)
    grid_width = len(grid[0])
    grid_px_width = grid_width * cell_size
    grid_px_height = grid_height * cell_size
    coordinate_band = max(30, cell_size + 4)
    header_height = 112
    palette_by_code = {entry.short_code: entry for entry in palette}
    used_codes = sorted(counts, key=lambda code: (-counts[code], code))

    width = grid_px_width + coordinate_band * 2
    legend_columns = max(5, min(12, (width - 40) // 250))
    legend_rows = math.ceil(len(used_codes) / legend_columns)
    legend_height = 92 + legend_rows * 88 + 92
    height = (
        header_height
        + coordinate_band
        + grid_px_height
        + coordinate_band
        + legend_height
    )
    canvas = Image.new("RGB", (width, height), "#F7F8FA")
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(34, bold=True)
    subtitle_font = load_font(19)
    code_font = load_font(max(9, round(cell_size * 0.39)), bold=True)
    coordinate_font = load_font(max(8, round(cell_size * 0.34)), bold=True)
    legend_code_font = load_font(18, bold=True)
    legend_count_font = load_font(16)
    footer_font = load_font(17)

    draw.text(
        (coordinate_band, 16),
        (
            f"小内耗拼豆模板｜{grid_width}×{grid_height} "
            "MARD 221 编号实做版"
        ),
        fill="#111317",
        font=title_font,
    )
    draw.text(
        (coordinate_band, 60),
        (
            "格内 A1 / C19 / E11 等为 MARD 221 短色号；"
            "对应厂家 M-2.6mm 完整码 MA1 / MC19 / ME11。"
        ),
        fill="#525A64",
        font=subtitle_font,
    )

    origin_x = coordinate_band
    origin_y = header_height + coordinate_band
    band_color = "#8493E6"
    colors = {
        entry.short_code: entry.hex_color
        for entry in palette
    }

    draw.rectangle(
        (
            origin_x,
            origin_y,
            origin_x + grid_px_width,
            origin_y + grid_px_height,
        ),
        fill="#FFFFFF",
    )
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            if not code:
                continue
            x0 = origin_x + x * cell_size
            y0 = origin_y + y * cell_size
            draw.rectangle(
                (x0, y0, x0 + cell_size, y0 + cell_size),
                fill=colors[code],
            )
            draw.text(
                (x0 + cell_size / 2, y0 + cell_size / 2),
                code,
                anchor="mm",
                fill=text_color(colors[code]),
                font=code_font,
            )

    for index in range(grid_width + 1):
        x = origin_x + index * cell_size
        heavy = index % 10 == 0
        draw.line(
            (x, origin_y, x, origin_y + grid_px_height),
            fill="#17191C" if heavy else "#81868C",
            width=4 if heavy else 1,
        )
    for index in range(grid_height + 1):
        y = origin_y + index * cell_size
        heavy = index % 10 == 0
        draw.line(
            (origin_x, y, origin_x + grid_px_width, y),
            fill="#17191C" if heavy else "#81868C",
            width=4 if heavy else 1,
        )

    top_y = header_height
    bottom_y = origin_y + grid_px_height
    left_x = 0
    right_x = origin_x + grid_px_width
    draw.rectangle(
        (origin_x, top_y, origin_x + grid_px_width, origin_y),
        fill=band_color,
    )
    draw.rectangle(
        (
            origin_x,
            bottom_y,
            origin_x + grid_px_width,
            bottom_y + coordinate_band,
        ),
        fill=band_color,
    )
    draw.rectangle(
        (left_x, origin_y, origin_x, origin_y + grid_px_height),
        fill=band_color,
    )
    draw.rectangle(
        (
            right_x,
            origin_y,
            right_x + coordinate_band,
            origin_y + grid_px_height,
        ),
        fill=band_color,
    )

    for index in range(grid_width):
        x = origin_x + index * cell_size + cell_size / 2
        label = str(index + 1)
        draw.text(
            (x, top_y + coordinate_band / 2),
            label,
            anchor="mm",
            fill="#17191C",
            font=coordinate_font,
        )
        draw.text(
            (x, bottom_y + coordinate_band / 2),
            label,
            anchor="mm",
            fill="#17191C",
            font=coordinate_font,
        )
    for index in range(grid_height):
        y = origin_y + index * cell_size + cell_size / 2
        label = str(index + 1)
        draw.text(
            (coordinate_band / 2, y),
            label,
            anchor="mm",
            fill="#17191C",
            font=coordinate_font,
        )
        draw.text(
            (right_x + coordinate_band / 2, y),
            label,
            anchor="mm",
            fill="#17191C",
            font=coordinate_font,
        )

    legend_top = bottom_y + coordinate_band + 28
    total = sum(counts.values())
    draw.text(
        (24, legend_top),
        (
            f"本图实际使用 {len(used_codes)} 种 MARD 221 色号｜"
            f"共 {total} 颗（不含空白背景）"
        ),
        fill="#111317",
        font=footer_font,
    )
    legend_top += 46
    item_width = (width - 40) / legend_columns
    for index, code in enumerate(used_codes):
        column = index % legend_columns
        row = index // legend_columns
        entry = palette_by_code[code]
        x = 20 + column * item_width
        y = legend_top + row * 88
        swatch_width = min(76, item_width - 18)
        draw.rounded_rectangle(
            (x, y, x + swatch_width, y + 48),
            radius=8,
            fill=entry.hex_color,
            outline="#5C626A",
            width=1,
        )
        draw.text(
            (x + swatch_width / 2, y + 24),
            code,
            anchor="mm",
            fill=text_color(entry.hex_color),
            font=legend_code_font,
        )
        draw.text(
            (x + swatch_width / 2, y + 68),
            str(counts[code]),
            anchor="mm",
            fill="#252A30",
            font=legend_count_font,
        )

    note_y = legend_top + legend_rows * 88 + 6
    physical_width = grid_width * 2.6 / 10
    physical_height = grid_height * 2.6 / 10
    draw.text(
        (24, note_y),
        (
            "厂家色表：Artkal M-2.6mm / MARD 221；"
            f"按 2.6mm 豆距约 {physical_width:.1f}×{physical_height:.1f} cm。"
        ),
        fill="#555D66",
        font=footer_font,
    )
    draw.text(
        (24, note_y + 30),
        (
            "H1 为透明豆，未参与本图自动配色；RGB 只供电子匹配，"
            "采购前仍需用实体豆或实体色卡复核。"
        ),
        fill="#6B737C",
        font=footer_font,
    )
    canvas.save(output_dir / f"{stem}-numbered-pattern.png")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a MARD 221 / Artkal M-2.6mm numbered fuse-bead pattern."
        )
    )
    parser.add_argument("--grid-width", type=int, default=120)
    parser.add_argument("--grid-height", type=int, default=120)
    parser.add_argument("--cell-size", type=int, default=36)
    parser.add_argument("--coverage-threshold", type=float, default=0.18)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--palette-csv", type=Path, default=PALETTE_CSV)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    if args.grid_width <= 0 or args.grid_height <= 0:
        parser.error("grid dimensions must be greater than zero")
    if args.cell_size < 20:
        parser.error("--cell-size must be at least 20 pixels")
    if not 0 < args.coverage_threshold <= 1:
        parser.error("--coverage-threshold must be greater than zero and at most one")

    palette, _ = load_palette(args.palette_csv.resolve())
    with Image.open(args.source.resolve()) as source:
        grid = build_grid(
            source,
            args.grid_width,
            args.grid_height,
            args.coverage_threshold,
            palette,
        )
    counts: Counter[str] = Counter(
        code for row in grid for code in row if code
    )
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = (
        f"xiaoneihao-cool-{args.grid_width}x{args.grid_height}-"
        "mard221-mini"
    )
    write_csvs(grid, counts, palette, output_dir, stem)
    render_preview(grid, palette, output_dir, stem)
    render_numbered_pattern(
        grid,
        counts,
        palette,
        output_dir,
        stem,
        args.cell_size,
    )
    print(
        f"Generated {args.grid_width}x{args.grid_height} MARD 221 pattern "
        f"with {sum(counts.values())} beads and {len(counts)} used colors "
        f"in {output_dir}."
    )
    for code in sorted(counts, key=lambda item: (-counts[item], item)):
        print(f"{code}: {counts[code]}")


if __name__ == "__main__":
    main()
