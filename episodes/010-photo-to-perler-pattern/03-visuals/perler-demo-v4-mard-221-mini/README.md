# 小内耗 120×120 MARD 221 编号模板 v4

这是第 010 集根据用户确认的正确编号模式重新生成的当前生产版。格内使用 `A1`、`C19`、`E11`、`H6`、`M12` 等 MARD 221 短色号，不再使用统一 `Sxx` 前缀，也不把参考图片中出现的颜色误当成完整色卡。

## 锁定规格

- 色号体系：MARD 标准 221 色
- 厂家对应：Artkal M-2.6mm Mini
- 网格：120×120，共 14,400 个位置
- 实际主体：4,209 颗，不含空白背景
- 实际用色：45 种
- 物理尺寸：按 2.6 mm 豆距约 31.2×31.2 cm
- 背景：浅蓝画布与深蓝装饰圆环省略
- 匹配方式：完整色表内的 CIE L*a*b* 感知色差最近邻

`H1 / MH1` 是透明豆，没有参加普通图像颜色匹配；本图实色白主要使用 `H2 / MH2`。

## 文件

- 原稿：[`../perler-demo-v1/xiaoneihao-cool-source.png`](../perler-demo-v1/xiaoneihao-cool-source.png)
- 像素效果预览：[`xiaoneihao-cool-120x120-mard221-mini-pixel-preview.png`](xiaoneihao-cool-120x120-mard221-mini-pixel-preview.png)
- 四边坐标带色号底板：[`xiaoneihao-cool-120x120-mard221-mini-numbered-pattern.png`](xiaoneihao-cool-120x120-mard221-mini-numbered-pattern.png)
- 逐格数据：[`xiaoneihao-cool-120x120-mard221-mini-pattern.csv`](xiaoneihao-cool-120x120-mard221-mini-pattern.csv)
- 实际用色与数量：[`xiaoneihao-cool-120x120-mard221-mini-palette.csv`](xiaoneihao-cool-120x120-mard221-mini-palette.csv)
- 完整 221 色表：[`../../01-research/mard-221-artkal-m-2.6mm-rgb-2025.csv`](../../01-research/mard-221-artkal-m-2.6mm-rgb-2025.csv)
- 编号核验记录：[`../../01-research/mard-221-numbering-standard.md`](../../01-research/mard-221-numbering-standard.md)
- 重建脚本：[`../../07-deliverables/generate_mard221_template.py`](../../07-deliverables/generate_mard221_template.py)

## 用量摘要

完整 45 色清单已经同时画在编号底板下方并写入采购 CSV。数量最多的颜色为：

| 短色号 | 官方完整码 | 数量 |
|---|---|---:|
| H2 | MH2 | 1,515 |
| H10 | MH10 | 701 |
| H7 | MH7 | 602 |
| H11 | MH11 | 226 |
| D1 | MD1 | 167 |
| C27 | MC27 | 137 |
| H4 | MH4 | 96 |
| H6 | MH6 | 91 |
| A13 | MA13 | 90 |
| H5 | MH5 | 69 |

## 重建命令

脚本依赖 Python 3 和 Pillow。先确认当前 Python 环境能够执行：

```bash
python3 -c "import PIL"
```

如果缺少 Pillow，请在所用的 Python 虚拟环境中安装 `Pillow`，再从仓库根目录执行：

```bash
python3 episodes/010-photo-to-perler-pattern/07-deliverables/generate_mard221_template.py
```

2026-07-30 已使用 Codex 工作区自带的 Pillow 12.2.0 环境在临时目录重建；四个生成文件与当前仓库版本逐文件一致。

## 分享水印版

- 无水印生产母版继续保留，不得覆盖。
- 分享版：[`xiaoneihao-cool-120x120-mard221-mini-numbered-pattern-watermarked.png`](xiaoneihao-cool-120x120-mard221-mini-numbered-pattern-watermarked.png)
- 水印文字：`小耗版权`；位置：正中央；不透明度：10%。
- 分享版尺寸仍为 4,400×5,048，未重新量化、重绘或修改任何格内色号、颗数、坐标、图例及采购数据。
- 分享版 SHA-256：`5ADD6920AB6F86A23D4F01B9899E53F6DF5F1886D87453C301D9A33BB536B157`。

## 实做限制

- 图纸短码与用户参考图一致；采购 CSV 同时给出官方完整码。
- 官方 RGB 是电子参考值，不等于在所有屏幕、光线和生产批次下看到的实物颜色。
- 若使用 5mm“MARD 同码”兼容豆，必须重新确认具体商家及其实体色卡；本版不能被描述为官方 5mm MARD 色表。
