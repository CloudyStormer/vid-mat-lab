from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


# 历史 v1-v3 重建脚本。当前生产版请使用 generate_mard221_template.py。
EPISODE_DIR = Path(__file__).resolve().parents[1]
SOURCE = (
    EPISODE_DIR
    / "03-visuals"
    / "perler-demo-v1"
    / "xiaoneihao-cool-source.png"
)
DEFAULT_OUTPUT_DIR = EPISODE_DIR / "03-visuals" / "perler-demo-v3-artkal-s5"

# Artkal 官方 S-5mm RGB 色卡中的真实字母+数字色号。电子 RGB 只用于
# 屏幕预览；官方明确要求采购与实物对色以实体豆/实体色卡为准。
ARTKAL_S5_PALETTE = [
    ("S13", "轮廓黑", "#000000"),
    ("S01", "主体白", "#FFFFFF"),
    ("S78", "浅灰", "#C8C9C7"),
    ("S159", "阴影灰", "#88888D"),
    ("S54", "电路蓝", "#0090DA"),
    ("S27", "闪电黄", "#FFC72C"),
    ("S19", "腮红粉", "#F8C1B8"),
]

# 仅用于重建已归档的 v1/v2 演示图，禁止作为采购色号。
LEGACY_DEMO_PALETTE = [
    ("01", "轮廓黑", "#111317"),
    ("02", "主体白", "#F7F7F5"),
    ("03", "浅灰", "#C9CDD2"),
    ("04", "阴影灰", "#858C95"),
    ("05", "电路蓝", "#1496E8"),
    ("06", "闪电黄", "#FFC21A"),
    ("07", "腮红粉", "#F5C6BC"),
]

PALETTES = {
    "artkal-s5": ARTKAL_S5_PALETTE,
    "legacy-demo": LEGACY_DEMO_PALETTE,
}


def rgb(hex_color: str) -> tuple[int, int, int]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def is_omitted_background(pixel: tuple[int, int, int]) -> bool:
    """Omit the pale-blue canvas and dark-navy decorative halo."""

    r, g, b = pixel
    pale_blue = r > 145 and g > 170 and b > 190 and (b - r) > 13 and (b - g) > 4
    # The halo is dark blue; bright cyan circuit lines must remain printable.
    navy_halo = r < 75 and g < 115 and b < 180 and b > r + 28 and b > g + 8
    return pale_blue or navy_halo


def nearest_palette(
    pixel: tuple[int, int, int],
    palette_rgb: list[tuple[str, str, tuple[int, int, int], str]],
) -> str:
    r, g, b = pixel
    return min(
        palette_rgb,
        key=lambda item: (r - item[2][0]) ** 2
        + (g - item[2][1]) ** 2
        + (b - item[2][2]) ** 2,
    )[0]


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
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


def build_grid(
    image: Image.Image,
    grid_size: int,
    coverage_threshold: float,
    palette_rgb: list[tuple[str, str, tuple[int, int, int], str]],
) -> list[list[str]]:
    source = image.convert("RGB")
    width, height = source.size
    pixels = source.load()
    grid: list[list[str]] = []

    for gy in range(grid_size):
        row: list[str] = []
        y0 = round(gy * height / grid_size)
        y1 = round((gy + 1) * height / grid_size)
        for gx in range(grid_size):
            x0 = round(gx * width / grid_size)
            x1 = round((gx + 1) * width / grid_size)
            kept: list[tuple[int, int, int]] = []
            total = max(1, (x1 - x0) * (y1 - y0))
            for y in range(y0, y1):
                for x in range(x0, x1):
                    pixel = pixels[x, y]
                    if not is_omitted_background(pixel):
                        kept.append(pixel)

            # A cell needs enough real subject coverage to become a bead.
            if len(kept) / total < coverage_threshold:
                row.append("")
                continue

            avg = tuple(round(sum(channel) / len(kept)) for channel in zip(*kept))
            row.append(nearest_palette(avg, palette_rgb))
        grid.append(row)
    return grid


def write_csvs(
    grid: list[list[str]],
    counts: Counter[str],
    output_dir: Path,
    grid_size: int,
    palette: list[tuple[str, str, str]],
    palette_profile: str,
    stem: str,
) -> None:
    with (output_dir / f"{stem}-pattern.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["row/col", *range(1, grid_size + 1)])
        for index, row in enumerate(grid, start=1):
            writer.writerow([index, *row])

    with (output_dir / f"{stem}-palette.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        if palette_profile == "artkal-s5":
            writer.writerow(
                ["品牌", "色卡版本", "品牌色号", "图案用途", "电子色卡HEX", "数量"]
            )
            for code, name, color in palette:
                writer.writerow(
                    ["Artkal", "S-5mm官方RGB色卡2024", code, name, color, counts[code]]
                )
        else:
            writer.writerow(["通用色号", "颜色名称", "HEX", "数量"])
            for code, name, color in palette:
                writer.writerow([code, name, color, counts[code]])


def render_pixel_preview(
    grid: list[list[str]],
    output_dir: Path,
    grid_size: int,
    palette: list[tuple[str, str, str]],
    stem: str,
) -> None:
    scale = max(12, min(24, 1600 // grid_size))
    preview = Image.new(
        "RGBA",
        (grid_size * scale, grid_size * scale),
        (0, 0, 0, 0),
    )
    draw = ImageDraw.Draw(preview)
    colors = {code: color for code, _, color in palette}
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


def code_text_color(hex_color: str) -> str:
    r, g, b = rgb(hex_color)
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "#FFFFFF" if luminance < 125 else "#111317"


def render_pattern(
    grid: list[list[str]],
    counts: Counter[str],
    output_dir: Path,
    grid_size: int,
    cell_size: int,
    palette: list[tuple[str, str, str]],
    palette_profile: str,
    stem: str,
) -> None:
    margin_left = 88 if grid_size > 40 else 72
    margin_top = 126
    legend_height = 330
    grid_px = grid_size * cell_size
    width = margin_left + grid_px + 52
    height = margin_top + grid_px + legend_height
    canvas = Image.new("RGB", (width, height), "#F7F8FA")
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(34, bold=True)
    subtitle_font = load_font(21)
    code_font = load_font(max(9, round(cell_size * 0.43)), bold=True)
    coord_font = load_font(15)
    legend_font = load_font(21)
    legend_small = load_font(17)

    if palette_profile == "artkal-s5":
        edition = "Artkal S-5mm 实做版"
        subtitle = (
            "5 mm 硬豆｜格内为 Artkal 官方 S 系列色号；"
            "电子 RGB 仅供参考，采购前用实体豆或实体色卡复核。"
        )
    else:
        edition = "历史演示版"
        subtitle = "01—07 为项目旧演示号，禁止用于采购；仅用于重建 v1/v2。"
    draw.text(
        (margin_left, 18),
        f"小内耗拼豆模板｜{grid_size}×{grid_size} {edition}",
        fill="#111317",
        font=title_font,
    )
    draw.text(
        (margin_left, 58),
        subtitle,
        fill="#555D66",
        font=subtitle_font,
    )

    colors = {code: color for code, _, color in palette}
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            x0 = margin_left + x * cell_size
            y0 = margin_top + y * cell_size
            if code:
                draw.rectangle(
                    (x0, y0, x0 + cell_size, y0 + cell_size),
                    fill=colors[code],
                )
                text_color = code_text_color(colors[code])
                bbox = draw.textbbox((0, 0), code, font=code_font)
                draw.text(
                    (
                        x0 + (cell_size - (bbox[2] - bbox[0])) / 2,
                        y0 + (cell_size - (bbox[3] - bbox[1])) / 2 - 1,
                    ),
                    code,
                    fill=text_color,
                    font=code_font,
                )

    # Grid lines, with a heavier line every five cells.
    for i in range(grid_size + 1):
        weight = 3 if i % 5 == 0 else 1
        line_color = "#252A30" if i % 5 == 0 else "#9AA1A9"
        x = margin_left + i * cell_size
        y = margin_top + i * cell_size
        draw.line(
            (x, margin_top, x, margin_top + grid_px),
            fill=line_color,
            width=weight,
        )
        draw.line(
            (margin_left, y, margin_left + grid_px, y),
            fill=line_color,
            width=weight,
        )

    label_step = 5 if grid_size > 40 else 2
    for i in range(grid_size):
        if i % label_step == 0:
            label = str(i + 1)
            x = margin_left + i * cell_size + cell_size / 2
            y = margin_top + i * cell_size + cell_size / 2
            draw.text(
                (x, margin_top - 18),
                label,
                anchor="mm",
                fill="#4A5159",
                font=coord_font,
            )
            draw.text(
                (margin_left - 25, y),
                label,
                anchor="mm",
                fill="#4A5159",
                font=coord_font,
            )

    legend_y = margin_top + grid_px + 42
    total = sum(counts.values())
    draw.text(
        (margin_left, legend_y),
        (
            f"Artkal S-5mm 色号与数量｜主体共 {total} 颗（不含空白背景）"
            if palette_profile == "artkal-s5"
            else f"历史演示号与数量｜主体共 {total} 颗（不含空白背景）"
        ),
        fill="#111317",
        font=legend_font,
    )
    legend_y += 45
    column_width = 390
    for index, (code, name, color) in enumerate(palette):
        col = index % 3
        row = index // 3
        x = margin_left + col * column_width
        y = legend_y + row * 58
        draw.rounded_rectangle((x, y, x + 38, y + 38), radius=5, fill=color, outline="#5C626A")
        draw.text(
            (x + 50, y + 6),
            f"{code}  {name}  × {counts[code]}",
            fill="#24292F",
            font=legend_small,
        )

    note_y = legend_y + 3 * 58 + 10
    draw.text(
        (margin_left, note_y),
        (
            "品牌/系列：Artkal S-5mm 硬豆；不得用其他品牌或 Artkal 其他尺寸系列替代。"
            if palette_profile == "artkal-s5"
            else "说明：本版本色号不可采购；生产请改用 Artkal S-5mm 实做版或指定品牌色卡。"
        ),
        fill="#6B737C",
        font=legend_small,
    )
    canvas.save(output_dir / f"{stem}-numbered-pattern.png")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Rebuild historical v1-v3 templates. "
            "Use generate_mard221_template.py for the current production pattern."
        )
    )
    parser.add_argument("--grid-size", type=int, default=80)
    parser.add_argument("--cell-size", type=int)
    parser.add_argument("--coverage-threshold", type=float)
    parser.add_argument(
        "--palette",
        choices=sorted(PALETTES),
        default="artkal-s5",
        help="Rebuild the withdrawn Artkal S-5mm v3 or legacy v1/v2 demos.",
    )
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    if args.grid_size <= 0:
        parser.error("--grid-size must be greater than zero")
    coverage_threshold = (
        args.coverage_threshold
        if args.coverage_threshold is not None
        else (0.18 if args.grid_size > 40 else 0.28)
    )
    if not 0 < coverage_threshold <= 1:
        parser.error("--coverage-threshold must be greater than zero and at most one")
    cell_size = args.cell_size or (
        30 if args.grid_size <= 40 else max(18, min(24, 1920 // args.grid_size))
    )
    if cell_size < 12:
        parser.error("--cell-size must be at least 12 pixels")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    palette = PALETTES[args.palette]
    palette_rgb = [
        (code, name, rgb(color), color) for code, name, color in palette
    ]
    suffix = "-artkal-s5" if args.palette == "artkal-s5" else ""
    stem = f"xiaoneihao-cool-{args.grid_size}x{args.grid_size}{suffix}"
    source = Image.open(args.source)
    grid = build_grid(source, args.grid_size, coverage_threshold, palette_rgb)
    counts: Counter[str] = Counter(code for row in grid for code in row if code)
    write_csvs(
        grid,
        counts,
        output_dir,
        args.grid_size,
        palette,
        args.palette,
        stem,
    )
    render_pixel_preview(grid, output_dir, args.grid_size, palette, stem)
    render_pattern(
        grid,
        counts,
        output_dir,
        args.grid_size,
        cell_size,
        palette,
        args.palette,
        stem,
    )
    print(
        f"Generated {args.grid_size}x{args.grid_size} template "
        f"with {sum(counts.values())} beads using {args.palette} in {output_dir}."
    )
    for code, name, _, _ in palette_rgb:
        print(f"{code} {name}: {counts[code]}")


if __name__ == "__main__":
    main()
