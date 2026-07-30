# Artkal S-5mm 官方色号核验与本图映射

## 结论

第 010 集当前实做版统一使用 **Artkal S-5mm Midi 硬豆**。图纸中的 `S01`、`S13`、`S54` 等均为 Artkal 官方 S 系列色号，不是项目自编号。

Hama 官方色卡使用纯数字编号；Perler 主要使用颜色名与商品货号。由于本集要求“字母＋数字”且需要公开可核验的品牌原始色卡，最终选用 Artkal S-5mm。

此前 v1/v2 中的 `01`—`07` 是项目临时演示编号，**禁止用于采购或实物制作**。

## 官方来源

1. Artkal 官方 S-5mm 色卡页：<https://www.artkalfusebeads.com/pages/s-color-chart>
2. Artkal 官方《S-5MM Midi Beads RGB Colors》PDF：<https://cdn.shopify.com/s/files/1/1323/8195/files/S_MIDI_Beads_RGB_Color_Chart_2024.pdf?v=1744686607>
3. Artkal 官方系列与尺寸说明：<https://www.artkalfusebeads.com/blogs/faq/artkal-beads-size>
4. Artkal 官方实体色卡：<https://www.artkalfusebeads.com/products/artkal-beads-color-chart>

官方页面确认 S 系列是 5 mm Midi 硬豆，当前色卡有 225 色。官方 RGB PDF 同时明确说明：电子 RGB 仅供参考，受显示设备与实物差异影响，不能代替查看实体豆颜色。

## 映射方法

- 轮廓和主体的设计语义优先：黑色固定使用官方黑 `S13`，白色固定使用官方白 `S01`。
- 其余颜色按原演示目标色与官方 RGB 表做欧氏距离近邻匹配。
- 映射只在同一个 Artkal S-5mm 实色系列内完成，不混用其他品牌、尺寸或透明/珠光/夜光系列。
- 图纸中的中文颜色名只描述该颜色在本图中的用途；采购识别以 `Sxx` 品牌色号为准。

| 图案用途 | 原目标色 | Artkal S-5mm 色号 | 官方 RGB 参考 | 选择依据 |
|---|---|---|---|---|
| 轮廓黑 | `#111317` | `S13` | `0, 0, 0` | 官方黑色，按设计语义锁定 |
| 主体白 | `#F7F7F5` | `S01` | `255, 255, 255` | 官方白色，按设计语义锁定 |
| 浅灰 | `#C9CDD2` | `S78` | `200, 201, 199` | 官方 RGB 近邻 |
| 阴影灰 | `#858C95` | `S159` | `136, 136, 141` | 官方 RGB 近邻 |
| 电路蓝 | `#1496E8` | `S54` | `0, 144, 218` | 官方 RGB 近邻 |
| 闪电黄 | `#FFC21A` | `S27` | `255, 199, 44` | 官方 RGB 近邻 |
| 腮红粉 | `#F5C6BC` | `S19` | `248, 193, 184` | 官方 RGB 近邻 |

## 实做边界

- 本图只允许按 Artkal S-5mm 采购；其他品牌即使色号相似，也不能直接代替。
- 正式购买大量豆子前，用 Artkal 同版本实体色卡或手头实体豆在相同光线下复核。
- 不同屏幕、拍摄白平衡与生产批次可能造成观感差异，但图纸色号本身保持不变。
- 若以后改用 MARD、Hama、Perler 或 Artkal 其他系列，必须重新跑品牌色卡映射并生成新版本。
