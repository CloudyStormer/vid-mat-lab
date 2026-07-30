# 小内耗 80×80 拼豆演示模板 v2

这是第 010 集当前默认使用的高还原版电子拼豆图纸。它沿用已经确认的小内耗酷图原稿，把网格从 v1 的 40×40 提高到 80×80，优先保留眼睛、嘴角、手指、电路纹、腰部锯齿和鞋子等识别细节。

旧版 40×40 仍保留为低豆量方案，不覆盖、不伪装成高还原成品。

## 文件

- 共用原稿：[`../perler-demo-v1/xiaoneihao-cool-source.png`](../perler-demo-v1/xiaoneihao-cool-source.png)
- 80×80 像素预览：[`xiaoneihao-cool-80x80-pixel-preview.png`](xiaoneihao-cool-80x80-pixel-preview.png)
- 80×80 带编号底板：[`xiaoneihao-cool-80x80-numbered-pattern.png`](xiaoneihao-cool-80x80-numbered-pattern.png)
- 网格数据：[`xiaoneihao-cool-80x80-pattern.csv`](xiaoneihao-cool-80x80-pattern.csv)
- 颜色与数量：[`xiaoneihao-cool-80x80-palette.csv`](xiaoneihao-cool-80x80-palette.csv)
- 可配置重建脚本：[`../../07-deliverables/generate_perler_template.py`](../../07-deliverables/generate_perler_template.py)

## 规格

- 网格：80×80，共 6,400 个可用位置
- 实际主体：1,897 颗，不含空白背景
- 颜色：7 种
- 背景：浅蓝底与深蓝圆环均省略
- 轮廓保留阈值：18%，用于减少高密度网格下细线断裂
- 色号：`01`—`07` 是项目通用演示编号，不是任何拼豆品牌的官方色号
- 5 mm 拼豆按 80 格计算，完整图案约为 40×40 cm，需要组合底板

## 数量

| 通用色号 | 颜色 | 数量 |
|---|---|---:|
| 01 | 轮廓黑 | 328 |
| 02 | 主体白 | 736 |
| 03 | 浅灰 | 507 |
| 04 | 阴影灰 | 130 |
| 05 | 电路蓝 | 107 |
| 06 | 闪电黄 | 68 |
| 07 | 腮红粉 | 21 |

## 与 v1 的关系

- 40×40：483 颗，适合低成本、低豆量演示。
- 80×80：1,897 颗，线性分辨率翻倍，网格位置数量是原来的 4 倍，作为当前默认高还原交付。
- 若投稿原图特别复杂，应先裁切主体、简化背景，再决定是否继续提高网格；不要只靠无限增加豆量解决构图问题。

## 重建命令

需要安装 Pillow：

```bash
python3 episodes/010-photo-to-perler-pattern/07-deliverables/generate_perler_template.py \
  --grid-size 80 \
  --output-dir episodes/010-photo-to-perler-pattern/03-visuals/perler-demo-v2
```

## 使用限制

正式给客户返图前，先确认客户使用的拼豆品牌，再把 `01`—`07` 映射为该品牌真实官方色号。不同品牌颜色名称和编号不通用，不能直接把本演示编号当成采购色号。
