# MARD 221 编号规则与第 010 集生产标准

## 用户确认

用户于 2026-07-30 提供了 [`reference-mard-221-numbering-example.png`](reference-mard-221-numbering-example.png)，并明确说明：

- 图中的编号模式是正确的；
- 该图片本身并不包含完整色卡；
- 只能用它确认 `A1`、`C19`、`E11`、`H6`、`M12` 等编号规则，不能照抄图片中出现的颜色集合。

因此，本集必须使用完整色表重新量化原图，再输出本图实际用到的色号和数量。

## 编号体系结论

参考图采用 **MARD 标准 221 色短码**：

- A：`A1`—`A26`，26 色
- B：`B1`—`B32`，32 色
- C：`C1`—`C29`，29 色
- D：`D1`—`D26`，26 色
- E：`E1`—`E24`，24 色
- F：`F1`—`F25`，25 色
- G：`G1`—`G21`，21 色
- H：`H1`—`H23`，23 色
- M：`M1`—`M15`，15 色

合计 221 色。它是实体豆采购色号体系，不是某个图纸软件临时编写的序号。仅凭版式不能反推参考图由哪款软件生成。

## 厂家与官方来源

1. 优肯 / Artkal 厂家产品页：<https://artkalbeads.com/artkal_beads/527.html>
   - 产品名直接写明 “Mard 221 colors 2.6mm fuse beads”；
   - 规格写明 `Product size: 2.6mm`、`Colors: Mard 221 colors`。
2. Artkal 官方 M-2.6mm Mini 系列：<https://www.artkalfusebeads.com/collections/m-2-6mm-mini-beads>
3. Artkal 官方《M-2.6MM Mini Beads RGB Colors 2025》：
   <https://cdn.shopify.com/s/files/1/1323/8195/files/M_MINI_Beads_RGB_Color_Chart_2025.pdf?v=1760661747>
4. 厂家 MARD 221 实体色卡图：
   <https://www.artkalbeads.com/uploads/allimg/20251016/2-251016110255P7.bmp>

本地提取后的完整 221 色数据见
[`mard-221-artkal-m-2.6mm-rgb-2025.csv`](mard-221-artkal-m-2.6mm-rgb-2025.csv)。

## 短码与完整码

国内图纸通常省略 M 系列产品码最前面的 `M`：

| 图纸短码 | 官方 PDF 完整码 |
|---|---|
| `A1` | `MA1` |
| `C19` | `MC19` |
| `E11` | `ME11` |
| `H6` | `MH6` |
| `M12` | `MM12` |

第 010 集图纸格内使用用户确认的短码，采购 CSV 同时保留短码和官方完整码。

## 尺寸与透明色边界

- 厂家一手资料把 MARD 221 对应到 Artkal M-2.6mm Mini，不是 S-5mm。
- `H1 / MH1` 在 2025 官方 RGB 表中是透明豆，没有 RGB 数值；自动量化时不把它当普通白色使用。
- `H2 / MH2` 才是 RGB `255,255,255` 的实色白。
- 若改用市场上的 5mm“MARD 同码”兼容豆，必须锁定具体品牌或商家的实体色卡；不能把 2.6mm 官方 RGB 直接冒充该商家的 5mm 实物色。

## 本集量化规则

- 网格由 80×80 提升到 120×120。
- 使用完整 221 色表中的 220 个不透明颜色进行自动匹配。
- 使用 CIE L*a*b* 感知色差做逐格最近邻，不再把原图先压缩成 7 种项目色。
- 浅蓝画布与深蓝装饰圆环继续作为空白背景省略。
- 输出格内短码、四边逐格坐标、每 10 格粗辅助线、全部实用色号与颗数。
- 官方 RGB 只用于电子匹配；正式大量采购仍需用实体豆或实体色卡复核。
