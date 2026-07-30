# 第 010 集｜你发图，我做拼豆图纸

## 状态

- 当前阶段：广告首帧、口播、图生视频提示词和 80×80 Artkal S-5mm 官方色号实做模板已完成，待生成动态与剪辑
- 创建日期：2026-07-29
- 画面规格：竖屏 9:16
- 建议成片：15—18 秒
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
- 当前小内耗演示图已明确锁定为 Artkal S-5mm；若投稿者使用其他品牌或尺寸，必须重做色卡映射，不能直接替换编号。

## 当前交付

- 活动与投稿机制：[`01-research/offer-mechanism.md`](01-research/offer-mechanism.md)
- 最终口播与字幕：[`02-script/voiceover-v1.md`](02-script/voiceover-v1.md)
- 竖屏广告首帧：[`03-visuals/keyframes-v1/01-stop-scroll-first-frame.png`](03-visuals/keyframes-v1/01-stop-scroll-first-frame.png)
- 图生视频提示词：[`04-prompts/video-prompt-v1.md`](04-prompts/video-prompt-v1.md)
- 首帧生成提示词：[`04-prompts/keyframe-prompt-v1.md`](04-prompts/keyframe-prompt-v1.md)
- 剪辑方案：[`05-editing/edit-plan-v1.md`](05-editing/edit-plan-v1.md)
- 发布材料：[`06-publishing/publishing-v1.md`](06-publishing/publishing-v1.md)
- Artkal 官方色卡核验与映射依据：[`01-research/artkal-s5-color-mapping.md`](01-research/artkal-s5-color-mapping.md)
- 小内耗 80×80 Artkal S-5mm 实做模板（当前唯一生产版）：[`03-visuals/perler-demo-v3-artkal-s5/README.md`](03-visuals/perler-demo-v3-artkal-s5/README.md)
- 小内耗 80×80 自编号模板（已废弃，禁止采购）：[`03-visuals/perler-demo-v2/README.md`](03-visuals/perler-demo-v2/README.md)
- 小内耗 40×40 低豆量模板（历史 v1）：[`03-visuals/perler-demo-v1/README.md`](03-visuals/perler-demo-v1/README.md)
- 支持 Artkal S-5mm 与历史演示模式的重建脚本：[`07-deliverables/generate_perler_template.py`](07-deliverables/generate_perler_template.py)

## 拼豆底板版本决定

- 40×40 仅保留为低豆量历史方案，主体 483 颗；其中 `01`—`07` 不是品牌色号。
- 80×80 v2 虽提高到 1,897 颗，但仍使用项目自编号，已废弃并禁止用于采购。
- 80×80 v3 是当前实做方案，锁定 Artkal S-5mm 官方色号：`S13`、`S01`、`S78`、`S159`、`S54`、`S27`、`S19`。
- 80×80 明显改善眼睛、嘴角、手指、电路纹、腰部锯齿和鞋子轮廓；装饰背景仍省略，避免无意义增加豆量。
- 5 mm 拼豆做满 80 格约为 40×40 cm，真实制作需要组合底板。
- 电子 RGB 只用于生成预览；Artkal 官方明确要求实体对色，正式采购前用同版本实体色卡或实体豆复核。

## 下一步

1. 把广告首帧上传到可灵、即梦或 Grok，按图生视频提示词生成 10 秒主体动态。
2. 在剪映把动态延长为 15—18 秒，并加入准确中文、口播和免责声明。
3. 发布前确认本期征集数量、截止时间和预计返图时间。
4. 收到投稿后，先确定品牌和尺寸，再用该品牌官方色卡重新量化；不能跨品牌照抄本演示的 `Sxx` 色号。
