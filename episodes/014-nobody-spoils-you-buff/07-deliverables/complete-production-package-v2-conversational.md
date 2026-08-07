# 第 014 集完整制作包｜v2 有来有回版

## 当前结论

- 当前生产版：38.0 秒，15 个独立 AI 镜头。
- 15 张正式关键帧已全部生成并验收，统一为 941×1672 PNG。
- 六组生活场景完整保留“小耗儿先说—NPC 回怼—反向发福利”，不再使用 v1 的单向展示结构。
- 动态生成前仍须登记小耗儿与 NPC 的两套实际声音锚点；不得把内部代码 `VO-XH-01`、`VO-NPC-01` 直接当成平台 Voice ID。

## 一键入口

- [完整口播与声音配置](../02-script/voiceover-v2-conversational.md)
- [剪映字幕 SRT](../02-script/subtitles-v2-conversational.srt)
- [15 条图片生成提示词](../04-prompts/image-prompts-v2-conversational.md)
- [15 条可独立整框复制的有声视频提示词](../04-prompts/video-prompts-v2-conversational.md)
- [38 秒剪辑时间线](../05-editing/edit-plan-v2-conversational.md)
- [声音与音乐方案](../05-editing/sound-plan-v2-conversational.md)
- [发布标题、简介、封面、标签与置顶评论](../06-publishing/publishing-v2-conversational.md)

## 15 张正式关键帧与对应口播

| 镜头 | 正式关键帧 | 口播/用途 |
|---:|---|---|
| 01 | [街头独白](../03-visuals/keyframes-v2-conversational/01-opening-street-monologue.png) | 我就像被我老娘诅咒了一样，长大后真的没人惯着我，要啥不给啥，不要啥偏给我啥。 |
| 02 | [面馆请求](../03-visuals/keyframes-v2-conversational/02-noodle-xiaohao-request.png) | 老板，牛肉面不要肉。 |
| 03 | [面馆回应](../03-visuals/keyframes-v2-conversational/03-noodle-owner-reply.png) | 没人惯着你挑三拣四！全给我吃！ |
| 04 | [便利店请求](../03-visuals/keyframes-v2-conversational/04-store-xiaohao-request.png) | 不用找零了。 |
| 05 | [便利店回应](../03-visuals/keyframes-v2-conversational/05-store-owner-reply.png) | 没人惯着你占小便宜！拿着！ |
| 06 | [奶茶请求](../03-visuals/keyframes-v2-conversational/06-milktea-xiaohao-request.png) | 奶茶不要加布丁。 |
| 07 | [奶茶回应](../03-visuals/keyframes-v2-conversational/07-milktea-clerk-reply.png) | 没人惯着你喝寡茶！全加上！ |
| 08 | [外卖请求](../03-visuals/keyframes-v2-conversational/08-delivery-xiaohao-request.png) | 外卖不用送上来，放驿站就行。 |
| 09 | [外卖回应](../03-visuals/keyframes-v2-conversational/09-delivery-rider-reply.png) | 没人惯着你跑驿站！全给你送上来！ |
| 10 | [办公室请求](../03-visuals/keyframes-v2-conversational/10-office-xiaohao-request.png) | 我再改完这版就走…… |
| 11 | [办公室回应](../03-visuals/keyframes-v2-conversational/11-office-boss-reply.png) | 没人惯着你蹭加班！全给我下班！ |
| 12 | [理发店请求](../03-visuals/keyframes-v2-conversational/12-salon-xiaohao-request.png) | 我想充个会员。 |
| 13 | [理发店回应](../03-visuals/keyframes-v2-conversational/13-salon-stylist-reply.png) | 没人惯着你乱花钱！黑金卡拿好，以后剪头全免费！ |
| 14 | [福利围住](../03-visuals/keyframes-v2-conversational/14-all-benefits-confused.png) | 我怎么觉得……不太对呢？ |
| 15 | [亮黄收尾](../03-visuals/keyframes-v2-conversational/15-yellow-outro-smile.png) | 无口播；后期大字：合着我这诅咒，是来享福的？ |

## 下一步

1. 先登记并验收 `VO-XH-01` 与 `VO-NPC-01` 的实际声音资产。
2. 用镜头 02、03 做一组完整有声试片，确认固定音色、唯一说话者、逐字对白与无牙口型。
3. 通过后按同一参数批量生成其余 13 段；在剪映按既定 38 秒时间线硬切组合。
