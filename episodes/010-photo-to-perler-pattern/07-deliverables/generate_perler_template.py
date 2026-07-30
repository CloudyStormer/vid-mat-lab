from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EPISODE_DIR = Path(__file__).resolve().parents[1]
SOURCE = (
    EPISODE_DIR
    / "03-visuals"
    / "perler-demo-v1"
    / "xiaoneihao-cool-source.png"
)
DEFAULT_OUTPUT_DIR = EPISODE_DIR / "03-visuals" / "perler-demo-v1"

# 这是项目内部的通用演示色号，不冒充任一拼豆品牌的官方色号。
PALETTE = [
    ("01", "轮廓黑", "#111317"),
    ("02", "主体白", "#F7F7F5"),
    ("03", "浅灰", "#C9CDD2"),
    ("04", "阴影灰", "#858C95"),
    ("05", "电路蓝", "#1496E8"),
    ("06", "闪电黄", "#FFC21A"),
    ("07", "腮红粉", "#F5C6BC"),
]


def rgb(hex_color: str) -> tuple[int, int, int]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


PALETTE_RGB = [(code, name, rgb(color), color) for code, name, color in PALETTE]


def is_omitted_background(pixel: tuple[int, int, int]) -> bool:
    """Omit the pale-blue canvas and dark-navy decorative halo."""

    r, g, b = pixel
    pale_blue = r > 145 and g > 170 and b > 190 and (b - r) > 13 and (b - g) > 4
    # The halo is dark blue; bright cyan circuit lines must remain printable.
    navy_halo = r < 75 and g < 115 and b < 180 and b > r + 28 and b > g + 8
    return pale_blue or navy_halo


def nearest_palette(pixel: tuple[int, int, int]) -> str:
    r, g, b = pixel
    return min(
        PALETTE_RGB,
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
            row.append(nearest_palette(avg))
        grid.append(row)
    return grid


def write_csvs(
    grid: list[list[str]],
    counts: Counter[str],
    output_dir: Path,
    grid_size: int,
) -> None:
    stem = f"xiaoneihao-cool-{grid_size}x{grid_size}"
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
        writer.writerow(["通用色号", "颜色名称", "HEX", "数量"])
        for code, name, color in PALETTE:
            writer.writerow([code, name, color, counts[code]])


def render_pixel_preview(
    grid: list[list[str]],
    output_dir: Path,
    grid_size: int,
) -> None:
    scale = max(12, min(24, 1600 // grid_size))
    preview = Image.new(
        "RGBA",
        (grid_size * scale, grid_size * scale),
        (0, 0, 0, 0),
    )
    draw = ImageDraw.Draw(preview)
    colors = {code: color for code, _, color in PALETTE}
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
    preview.save(
        output_dir / f"xiaoneihao-cool-{grid_size}x{grid_size}-pixel-preview.png"
    )


def render_pattern(
    grid: list[list[str]],
    counts: Counter[str],
    output_dir: Path,
    grid_size: int,
    cell_size: int,
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

    edition = "高还原版" if grid_size > 40 else "低豆量版"
    draw.text(
        (margin_left, 18),
        f"小内耗拼豆模板｜{grid_size}×{grid_size} {edition}",
        fill="#111317",
        font=title_font,
    )
    draw.text(
        (margin_left, 58),
        "装饰背景已省略；01—07 为通用演示色号，正式制作前需映射到所用品牌。",
        fill="#555D66",
        font=subtitle_font,
    )

    colors = {code: color for code, _, color in PALETTE}
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            x0 = margin_left + x * cell_size
            y0 = margin_top + y * cell_size
            if code:
                draw.rectangle(
                    (x0, y0, x0 + cell_size, y0 + cell_size),
                    fill=colors[code],
                )
                text_color = "#FFFFFF" if code in {"01", "04"} else "#111317"
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
        f"色号与数量｜主体共 {total} 颗（不含空白背景）",
        fill="#111317",
        font=legend_font,
    )
    legend_y += 45
    column_width = 390
    for index, (code, name, color) in enumerate(PALETTE):
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
        "说明：本模板用于账号广告与流程演示；不同拼豆品牌的官方色号并不通用。",
        fill="#6B737C",
        font=legend_small,
    )
    canvas.save(
        output_dir / f"xiaoneihao-cool-{grid_size}x{grid_size}-numbered-pattern.png"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a numbered perler-bead pattern from the episode demo image."
    )
    parser.add_argument("--grid-size", type=int, default=40)
    parser.add_argument("--cell-size", type=int)
    parser.add_argument("--coverage-threshold", type=float)
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
        30 if args.grid_size <= 40 else max(16, min(24, 1600 // args.grid_size))
    )
    if cell_size < 12:
        parser.error("--cell-size must be at least 12 pixels")

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    source = Image.open(args.source)
    grid = build_grid(source, args.grid_size, coverage_threshold)
    counts: Counter[str] = Counter(code for row in grid for code in row if code)
    write_csvs(grid, counts, output_dir, args.grid_size)
    render_pixel_preview(grid, output_dir, args.grid_size)
    render_pattern(grid, counts, output_dir, args.grid_size, cell_size)
    print(
        f"Generated {args.grid_size}x{args.grid_size} template "
        f"with {sum(counts.values())} beads in {output_dir}."
    )
    for code, name, _, _ in PALETTE_RGB:
        print(f"{code} {name}: {counts[code]}")


if __name__ == "__main__":
    main()
