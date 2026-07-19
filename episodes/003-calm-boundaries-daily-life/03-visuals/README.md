# 第 003 集视觉规划

- 当前状态：八组首尾帧 v1 已生成并完成视觉检查。
- 实际规格：约 1672×941，横版近标准 16:9；剪辑时按项目画布缩放到 1920×1080。
- 固定角色：白色小电阻人。
- 实际数量：8 个场景 × 起始帧/收尾帧各 1 张，共 16 张。
- 图片本身不生成文字、字幕、Logo 或水印。
- 每组起始帧和收尾帧保持相同场景、服装、光线和镜头轴线，方便后续首尾帧图生视频。
- 角色已检查：白色脸部只有腰带上方一张嘴；灰色腰带和白色锯齿保持封闭硬质结构，没有舌头、牙齿或第二张嘴。

## 联系表

![第 003 集八组首尾帧联系表](horizontal-v1/contact-sheet.jpg)

- 文件尺寸与 SHA-256：[horizontal-v1/MANIFEST.md](horizontal-v1/MANIFEST.md)

## 文件清单

| 场景 | 起始帧 | 收尾帧 |
|---:|---|---|
| 01 深夜加班 | [start](horizontal-v1/01-overtime-start.png) | [end](horizontal-v1/01-overtime-end.png) |
| 02 团结与待遇 | [start](horizontal-v1/02-solidarity-pay-start.png) | [end](horizontal-v1/02-solidarity-pay-end.png) |
| 03 亲戚问工资 | [start](horizontal-v1/03-salary-privacy-start.png) | [end](horizontal-v1/03-salary-privacy-end.png) |
| 04 太爷爷姓名 | [start](horizontal-v1/04-marriage-ancestor-start.png) | [end](horizontal-v1/04-marriage-ancestor-end.png) |
| 05 购物与良心 | [start](horizontal-v1/05-tour-shopping-start.png) | [end](horizontal-v1/05-tour-shopping-end.png) |
| 06 朋友与还钱 | [start](horizontal-v1/06-debt-friendship-start.png) | [end](horizontal-v1/06-debt-friendship-end.png) |
| 07 吃亏是福 | [start](horizontal-v1/07-suffer-blessing-start.png) | [end](horizontal-v1/07-suffer-blessing-end.png) |
| 08 说话太直 | [start](horizontal-v1/08-blunt-speech-start.png) | [end](horizontal-v1/08-blunt-speech-end.png) |

## 生成与连续性说明

- 起始帧使用固定 IP 图作为角色身份参考。
- 收尾帧同时使用固定 IP 图和对应起始帧，锁定场景、构图、人物服装与镜位。
- 第 06 组首次生成曾偏向真人摄影风格，已弃用并定向重生为统一二维赛璐璐动画；错误版本未进入项目。
- 联系表只用于检查顺序与连续性，不作为发布画面。
