# 小内耗 80×80 Artkal S-5mm 实做模板 v3

> **已撤回，不符合用户确认的 MARD 221 编号体系。** `Sxx` 是真实的 Artkal S-5mm 色号，但不是本集要使用的 `A1 / C19 / E11` 模式，禁止把本版当作当前采购清单。当前生产版见 [`../perler-demo-v4-mard-221-mini/README.md`](../perler-demo-v4-mard-221-mini/README.md)。

本版本仅用于保留 Artkal S-5mm 方案的历史过程。网格内的 `Sxx` 不是虚构编号，但品牌、系列、网格密度与用户确认的目标均不一致。

## 锁定规格

- 品牌：Artkal
- 系列：S 系列，5 mm Midi 硬豆
- 色卡：Artkal 官方 S-5mm RGB 色卡
- 网格：80×80，共 6,400 个位置
- 实际主体：1,897 颗，不含空白背景
- 实际尺寸：按 5 mm 豆距计算约 40×40 cm，需要组合底板
- 颜色：7 种，全部来自同一 Artkal S-5mm 实色系列
- 背景：浅蓝底与深蓝圆环均省略

## 文件

- 共用原稿：[`../perler-demo-v1/xiaoneihao-cool-source.png`](../perler-demo-v1/xiaoneihao-cool-source.png)
- 实做效果预览：[`xiaoneihao-cool-80x80-artkal-s5-pixel-preview.png`](xiaoneihao-cool-80x80-artkal-s5-pixel-preview.png)
- 带官方色号底板：[`xiaoneihao-cool-80x80-artkal-s5-numbered-pattern.png`](xiaoneihao-cool-80x80-artkal-s5-numbered-pattern.png)
- 逐格数据：[`xiaoneihao-cool-80x80-artkal-s5-pattern.csv`](xiaoneihao-cool-80x80-artkal-s5-pattern.csv)
- 色号与数量：[`xiaoneihao-cool-80x80-artkal-s5-palette.csv`](xiaoneihao-cool-80x80-artkal-s5-palette.csv)
- 官方来源与映射记录：[`../../01-research/artkal-s5-color-mapping.md`](../../01-research/artkal-s5-color-mapping.md)
- 重建脚本：[`../../07-deliverables/generate_perler_template.py`](../../07-deliverables/generate_perler_template.py)

## 实做用量

| Artkal S-5mm 色号 | 图案用途 | 数量 |
|---|---|---:|
| S13 | 轮廓黑 | 307 |
| S01 | 主体白 | 722 |
| S78 | 浅灰 | 532 |
| S159 | 阴影灰 | 143 |
| S54 | 电路蓝 | 103 |
| S27 | 闪电黄 | 68 |
| S19 | 腮红粉 | 22 |

## 重建命令

需要安装 Pillow。在仓库根目录执行：

```bash
python3 episodes/010-photo-to-perler-pattern/07-deliverables/generate_perler_template.py
```

## 采购与对色限制

- 图纸只能直接对应 Artkal S-5mm；不得把其他品牌或 Artkal 其他尺寸系列的同名颜色混入。
- 中文颜色名是本图用途说明，采购以 `Sxx` 色号为准。
- Artkal 官方明确说明电子 RGB 不能替代实体颜色。大量采购前，用同版本实体色卡或手头实体豆复核。
- v1/v2 的 `01`—`07` 仅是历史演示号，禁止用于采购。
