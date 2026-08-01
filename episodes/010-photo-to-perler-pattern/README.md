# 第 010 集｜你发图，我做拼豆图纸

## 状态

- 当前阶段：中央水印分享底板和 10 秒竖屏成品均已完成；绿发星灵 78×78 / 96×96 投稿图纸已交付，待发布与数据复盘
- 创建日期：2026-07-29
- 画面规格：竖屏 9:16
- 建议成片：15—18 秒
- 实际成片：10 秒，720×1264，30 fps
- 核心用途：为“粉丝投稿转拼豆电子图纸”系列拉来首批有效投稿

## 本集目标

- 前两秒让观众立即看懂：你发图，我把它转成带色号、能照着拼的电子拼豆图纸。
- 用拼豆成品与手机原图的强对比吸引停留，不先介绍账号背景。
- 建立可持续的投稿机制：前期在能力范围内尽量多做，投稿变多后每期选择若干张。
- 互动不是免费服务的交换条件；关注只用于不错过返图和后续公布。

## 核心画面

第一帧直接把一块接近完成的拼豆作品推到镜头前；小内耗在后面举着手机原图。观众不听口播，也能看出“原图 → 拼豆”的服务。

生成动态时使用同一块板完成翻面：正面是拼豆成品，背面是带网格的电子图纸，避免突然生成第二块板或额外道具。

## 服务边界

- 当前免费的是电子拼豆图纸和通用配色参考，不包含拼豆材料、邮寄和实物成品。
- 入选后再通过站内私信收清晰原图。
- 只处理投稿者本人拥有或已获授权的图片。
- 真实交付前要先确认所用拼豆品牌；不同品牌官方色号不通用。
- 当前小内耗演示图已按用户确认的 MARD 221 短码生成，并对应厂家 Artkal M-2.6mm 色表；若投稿者使用其他品牌或尺寸，必须重做色卡映射，不能直接替换编号。

## 当前交付

- 活动与投稿机制：[`01-research/offer-mechanism.md`](01-research/offer-mechanism.md)
- 最终口播与字幕：[`02-script/voiceover-v1.md`](02-script/voiceover-v1.md)
- 竖屏广告首帧：[`03-visuals/keyframes-v1/01-stop-scroll-first-frame.png`](03-visuals/keyframes-v1/01-stop-scroll-first-frame.png)
- 图生视频提示词：[`04-prompts/video-prompt-v1.md`](04-prompts/video-prompt-v1.md)
- 首帧生成提示词：[`04-prompts/keyframe-prompt-v1.md`](04-prompts/keyframe-prompt-v1.md)
- 剪辑方案：[`05-editing/edit-plan-v1.md`](05-editing/edit-plan-v1.md)
- 发布材料：[`06-publishing/publishing-v1.md`](06-publishing/publishing-v1.md)
- MARD 221 编号规则与厂家依据：[`01-research/mard-221-numbering-standard.md`](01-research/mard-221-numbering-standard.md)
- 完整 221 色 RGB 数据：[`01-research/mard-221-artkal-m-2.6mm-rgb-2025.csv`](01-research/mard-221-artkal-m-2.6mm-rgb-2025.csv)
- 用户提供的编号范例（只用于确认编号规则，不代表完整色卡）：[`01-research/reference-mard-221-numbering-example.png`](01-research/reference-mard-221-numbering-example.png)
- 小内耗 120×120 MARD 221 实做模板（当前生产版）：[`03-visuals/perler-demo-v4-mard-221-mini/README.md`](03-visuals/perler-demo-v4-mard-221-mini/README.md)
- 中央 10% 不透明度小耗版权分享底板：[`03-visuals/perler-demo-v4-mard-221-mini/xiaoneihao-cool-120x120-mard221-mini-numbered-pattern-watermarked.png`](03-visuals/perler-demo-v4-mard-221-mini/xiaoneihao-cool-120x120-mard221-mini-numbered-pattern-watermarked.png)
- 第 010 集 10 秒成品：[`07-deliverables/episode-010-final-v1.mp4`](07-deliverables/episode-010-final-v1.mp4)
- 小内耗 80×80 Artkal S-5mm 模板（已撤回，编号体系不符）：[`03-visuals/perler-demo-v3-artkal-s5/README.md`](03-visuals/perler-demo-v3-artkal-s5/README.md)
- 小内耗 80×80 自编号模板（已废弃，禁止采购）：[`03-visuals/perler-demo-v2/README.md`](03-visuals/perler-demo-v2/README.md)
- 小内耗 40×40 低豆量模板（历史 v1）：[`03-visuals/perler-demo-v1/README.md`](03-visuals/perler-demo-v1/README.md)
- 当前 MARD 221 重建脚本：[`07-deliverables/generate_mard221_template.py`](07-deliverables/generate_mard221_template.py)
- 绿发星灵 78×78 / 96×96 MARD 221 图纸：[`03-visuals/perler-request-green-haired-fairy/README.md`](03-visuals/perler-request-green-haired-fairy/README.md)
- 绿发星灵眼部细节对比：[`03-visuals/perler-request-green-haired-fairy/green-fairy-eye-detail-comparison.png`](03-visuals/perler-request-green-haired-fairy/green-fairy-eye-detail-comparison.png)
- 动漫图眼部保护生成脚本：[`07-deliverables/generate_anime_mard221_pattern.py`](07-deliverables/generate_anime_mard221_pattern.py)
- v1—v3 历史重建脚本：[`07-deliverables/generate_perler_template.py`](07-deliverables/generate_perler_template.py)

## 拼豆底板版本决定

- 40×40 仅保留为低豆量历史方案，主体 483 颗；其中 `01`—`07` 不是品牌色号。
- 80×80 v2 虽提高到 1,897 颗，但仍使用项目自编号，已废弃并禁止用于采购。
- 80×80 v3 使用的 `Sxx` 虽是真实 Artkal S-5mm 色号，但不是用户确认的 MARD 221 编号模式，已撤回。
- 120×120 v4 使用完整 MARD 221 色表中的 220 个不透明颜色进行匹配，实际主体 4,209 颗、45 种色号。
- v4 在格内使用 `A1 / C19 / E11` 等短码，采购 CSV 同时保存 `MA1 / MC19 / ME11` 等官方完整码。
- v4 明显改善眼睛、嘴角、手指、电路纹、腰部锯齿和鞋子轮廓；装饰背景仍省略，避免无意义增加豆量。
- 厂家资料把 MARD 221 对应到 2.6mm Mini；120 格按 2.6mm 豆距约为 31.2×31.2 cm。
- `H1` 是透明豆，未参加普通图像颜色匹配；电子 RGB 只用于生成预览，正式采购前仍需实体对色。

## 下一步

1. 发布前确认本期征集数量、截止时间和预计返图时间。
2. 发布时使用中央水印版展示图纸，无水印母版只用于内部生产。
3. 发布后补充作品链接，并记录 24/72 小时播放、完播和互动数据。
4. 收到投稿后，先确定品牌、编号体系和尺寸，再用对应完整色卡重新量化；不能把本演示的 MARD 221 短码直接套给其他品牌。
