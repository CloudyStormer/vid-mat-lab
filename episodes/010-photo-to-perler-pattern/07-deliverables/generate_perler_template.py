from __future__ import annotations

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
OUTPUT_DIR = EPISODE_DIR / "03-visuals" / "perler-demo-v1"

GRID_SIZE = 40
CELL_SIZE = 30
MARGIN_LEFT = 72
MARGIN_TOP = 126
LEGEND_HEIGHT = 330

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
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def build_grid(image: Image.Image) -> list[list[str]]:
    source = image.convert("RGB")
    width, height = source.size
    pixels = source.load()
    grid: list[list[str]] = []

    for gy in range(GRID_SIZE):
        row: list[str] = []
        y0 = round(gy * height / GRID_SIZE)
        y1 = round((gy + 1) * height / GRID_SIZE)
        for gx in range(GRID_SIZE):
            x0 = round(gx * width / GRID_SIZE)
            x1 = round((gx + 1) * width / GRID_SIZE)
            kept: list[tuple[int, int, int]] = []
            total = max(1, (x1 - x0) * (y1 - y0))
            for y in range(y0, y1):
                for x in range(x0, x1):
                    pixel = pixels[x, y]
                    if not is_omitted_background(pixel):
                        kept.append(pixel)

            # A cell needs enough real subject coverage to become a bead.
            if len(kept) / total < 0.28:
                row.append("")
                continue

            avg = tuple(round(sum(channel) / len(kept)) for channel in zip(*kept))
            row.append(nearest_palette(avg))
        grid.append(row)
    return grid


def write_csvs(grid: list[list[str]], counts: Counter[str]) -> None:
    with (OUTPUT_DIR / "xiaoneihao-cool-40x40-pattern.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["row/col", *range(1, GRID_SIZE + 1)])
        for index, row in enumerate(grid, start=1):
            writer.writerow([index, *row])

    with (OUTPUT_DIR / "xiaoneihao-cool-40x40-palette.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["通用色号", "颜色名称", "HEX", "数量"])
        for code, name, color in PALETTE:
            writer.writerow([code, name, color, counts[code]])


def render_pixel_preview(grid: list[list[str]]) -> None:
    scale = 24
    preview = Image.new("RGBA", (GRID_SIZE * scale, GRID_SIZE * scale), (0, 0, 0, 0))
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
    preview.save(OUTPUT_DIR / "xiaoneihao-cool-40x40-pixel-preview.png")


def render_pattern(grid: list[list[str]], counts: Counter[str]) -> None:
    grid_px = GRID_SIZE * CELL_SIZE
    width = MARGIN_LEFT + grid_px + 52
    height = MARGIN_TOP + grid_px + LEGEND_HEIGHT
    canvas = Image.new("RGB", (width, height), "#F7F8FA")
    draw = ImageDraw.Draw(canvas)

    title_font = load_font(34, bold=True)
    subtitle_font = load_font(21)
    code_font = load_font(13, bold=True)
    coord_font = load_font(15)
    legend_font = load_font(21)
    legend_small = load_font(17)

    draw.text((MARGIN_LEFT, 18), "小内耗拼豆模板｜40×40 低豆量版", fill="#111317", font=title_font)
    draw.text(
        (MARGIN_LEFT, 58),
        "装饰背景已省略；01—07 为通用演示色号，正式制作前需映射到所用品牌。",
        fill="#555D66",
        font=subtitle_font,
    )

    colors = {code: color for code, _, color in PALETTE}
    for y, row in enumerate(grid):
        for x, code in enumerate(row):
            x0 = MARGIN_LEFT + x * CELL_SIZE
            y0 = MARGIN_TOP + y * CELL_SIZE
            if code:
                draw.rectangle(
                    (x0, y0, x0 + CELL_SIZE, y0 + CELL_SIZE),
                    fill=colors[code],
                )
                text_color = "#FFFFFF" if code in {"01", "04"} else "#111317"
                bbox = draw.textbbox((0, 0), code, font=code_font)
                draw.text(
                    (
                        x0 + (CELL_SIZE - (bbox[2] - bbox[0])) / 2,
                        y0 + (CELL_SIZE - (bbox[3] - bbox[1])) / 2 - 1,
                    ),
                    code,
                    fill=text_color,
                    font=code_font,
                )

    # Grid lines, with a heavier line every five cells.
    for i in range(GRID_SIZE + 1):
        weight = 3 if i % 5 == 0 else 1
        line_color = "#252A30" if i % 5 == 0 else "#9AA1A9"
        x = MARGIN_LEFT + i * CELL_SIZE
        y = MARGIN_TOP + i * CELL_SIZE
        draw.line((x, MARGIN_TOP, x, MARGIN_TOP + grid_px), fill=line_color, width=weight)
        draw.line((MARGIN_LEFT, y, MARGIN_LEFT + grid_px, y), fill=line_color, width=weight)

    for i in range(GRID_SIZE):
        if i % 2 == 0:
            label = str(i + 1)
            x = MARGIN_LEFT + i * CELL_SIZE + CELL_SIZE / 2
            y = MARGIN_TOP + i * CELL_SIZE + CELL_SIZE / 2
            draw.text((x, MARGIN_TOP - 18), label, anchor="mm", fill="#4A5159", font=coord_font)
            draw.text((MARGIN_LEFT - 20, y), label, anchor="mm", fill="#4A5159", font=coord_font)

    legend_y = MARGIN_TOP + grid_px + 42
    total = sum(counts.values())
    draw.text(
        (MARGIN_LEFT, legend_y),
        f"色号与数量｜主体共 {total} 颗（不含空白背景）",
        fill="#111317",
        font=legend_font,
    )
    legend_y += 45
    column_width = 390
    for index, (code, name, color) in enumerate(PALETTE):
        col = index % 3
        row = index // 3
        x = MARGIN_LEFT + col * column_width
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
        (MARGIN_LEFT, note_y),
        "说明：本模板用于账号广告与流程演示；不同拼豆品牌的官方色号并不通用。",
        fill="#6B737C",
        font=legend_small,
    )
    canvas.save(OUTPUT_DIR / "xiaoneihao-cool-40x40-numbered-pattern.png")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    source = Image.open(SOURCE)
    grid = build_grid(source)
    counts: Counter[str] = Counter(code for row in grid for code in row if code)
    write_csvs(grid, counts)
    render_pixel_preview(grid)
    render_pattern(grid, counts)
    print(f"Generated 40x40 template with {sum(counts.values())} beads.")
    for code, name, _, _ in PALETTE_RGB:
        print(f"{code} {name}: {counts[code]}")


if __name__ == "__main__":
    main()
