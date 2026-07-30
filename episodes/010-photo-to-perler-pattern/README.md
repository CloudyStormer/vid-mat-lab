# 第 010 集｜你发图，我做拼豆图纸

## 状态

- 当前阶段：广告首帧、口播、图生视频提示词和 80×80 高还原演示模板已完成，待生成动态与剪辑
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

## 当前交付

- 活动与投稿机制：[`01-research/offer-mechanism.md`](01-research/offer-mechanism.md)
- 最终口播与字幕：[`02-script/voiceover-v1.md`](02-script/voiceover-v1.md)
- 竖屏广告首帧：[`03-visuals/keyframes-v1/01-stop-scroll-first-frame.png`](03-visuals/keyframes-v1/01-stop-scroll-first-frame.png)
- 图生视频提示词：[`04-prompts/video-prompt-v1.md`](04-prompts/video-prompt-v1.md)
- 首帧生成提示词：[`04-prompts/keyframe-prompt-v1.md`](04-prompts/keyframe-prompt-v1.md)
- 剪辑方案：[`05-editing/edit-plan-v1.md`](05-editing/edit-plan-v1.md)
- 发布材料：[`06-publishing/publishing-v1.md`](06-publishing/publishing-v1.md)
- 小内耗 80×80 高还原模板（当前默认）：[`03-visuals/perler-demo-v2/README.md`](03-visuals/perler-demo-v2/README.md)
- 小内耗 40×40 低豆量模板（历史 v1）：[`03-visuals/perler-demo-v1/README.md`](03-visuals/perler-demo-v1/README.md)
- 可配置网格与轮廓阈值的重建脚本：[`07-deliverables/generate_perler_template.py`](07-deliverables/generate_perler_template.py)

## 拼豆底板版本决定

- 40×40 仅保留为低豆量方案，主体 483 颗，不再作为高还原展示的默认底板。
- 80×80 为当前默认高还原方案，主体 1,897 颗；线性分辨率翻倍，网格位置数量从 1,600 增至 6,400。
- 80×80 明显改善眼睛、嘴角、手指、电路纹、腰部锯齿和鞋子轮廓；装饰背景仍省略，避免无意义增加豆量。
- 5 mm 拼豆做满 80 格约为 40×40 cm，真实制作需要组合底板。

## 下一步

1. 把广告首帧上传到可灵、即梦或 Grok，按图生视频提示词生成 10 秒主体动态。
2. 在剪映把动态延长为 15—18 秒，并加入准确中文、口播和免责声明。
3. 发布前确认本期征集数量、截止时间和预计返图时间。
4. 收到投稿后，先确定拼豆品牌，再把通用颜色映射为该品牌官方色号。
