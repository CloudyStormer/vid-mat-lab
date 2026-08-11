# 第 017 集完整制作包 v1

## 项目结论

- 主题：亲近，不是越界的通行证
- 类型：生活边界 / 反内耗 / 对话喜剧
- 结构：玄关自然开场 + 三组正反打 + 同一玄关自然结尾
- 镜头数：8
- 有效时长：33.70秒
- 规格：竖屏9:16、1080×1920时间线、60fps
- 当前状态：制作包和关键帧完成，声音锚点与动态成片待制作

## 最终对白顺序

```text
熟人越亲近，越容易把越界当成关心。

你也争点气，下一胎生个儿子
那你是哪个不争气的生的？

我们那时候生完孩子就下地干活了，哪像现在的人金贵得很
那你可真挺惨的，牲口干完活都知道休息几天

你家孩子怎么跟我家狗一个名？
巧了，我老家也有个人跟你同名，坟头草都老高了，不看见你我都忘了这人了

亲近不是冒犯的通行证。该挡回去的话，当场挡回去。
```

## 生产顺序

1. 查看 [关键帧目录](../03-visuals/keyframes-v1/README.md)，按01—08使用。
2. 在 [声音登记表](../05-editing/voice-anchor-register-v1.md) 锁定实际小耗儿声音；不要把内部配置名当Voice ID。
3. 逐镜复制 [独立视频提示词](../04-prompts/video-prompts-v1-standalone.md)，生成6秒或10秒源片。
4. 按 [制作剧本](../02-script/production-script-v1.md) 只取有效区间。
5. 导入 [字幕SRT](../02-script/subtitles-v1.srt)，按 [剪辑方案](../05-editing/edit-plan-v1.md) 完成时间线。
6. 按 [声音方案](../05-editing/sound-plan-v1.md) 补底噪、转场音和低音量BGM。
7. 抽查首帧、25%、50%、75%和尾帧，验收角色与口型。
8. 使用 [发布材料](../06-publishing/publishing-v1.md) 完成封面、配文与发布设置。

## 关键帧

| 镜头 | 文件 | 角色/场景 |
|---:|---|---|
| 01 | `01-opening-closeness-boundary.png` | 小耗儿，饭局后玄关开场 |
| 02 | `02-family-relative-son.png` | 催生亲戚，节日餐桌正打 |
| 03 | `03-family-xiaohao-reply.png` | 小耗儿，节日餐桌反打 |
| 04 | `04-elder-pua.png` | PUA长辈，老式客厅正打 |
| 05 | `05-elder-xiaohao-reply.png` | 小耗儿，老式客厅反打 |
| 06 | `06-same-name-neighbor.png` | 同名邻居与一只灰狗，电梯厅正打 |
| 07 | `07-same-name-xiaohao-reply.png` | 小耗儿，电梯厅反打 |
| 08 | `08-closing-closeness-boundary.png` | 小耗儿，同一玄关收束 |

## 最终验收门槛

- 8镜时间线合计33.70秒；每镜0.30秒闭嘴准备、0.45秒闭嘴收口。
- 开场与结尾逐字正确；三组用户原对白无改词、漏词或续写。
- 每段只有一名说话者；灰狗和所有画外听者闭嘴。
- 小耗儿始终为单一横向近圆机体、两短手、两极短腿、唯一无牙无舌小嘴；无头顶球、双蛋、人类五指手或纹路漂移。
- 镜头08抬手必须保持短圆无分指小手。
- 不生成坟墓、骷髅或恐怖联想画面。
- 视频有人声且清晰，BGM不盖对白；字幕无错字并避开角色五官。

## 文件索引

- [选题简报](../01-research/brief-v1.md)
- [原始对白锁定](../01-research/source-dialogue-v1.md)
- [制作剧本](../02-script/production-script-v1.md)
- [口播稿](../02-script/voiceover-v1.md)
- [字幕](../02-script/subtitles-v1.srt)
- [视觉连续性](../03-visuals/continuity-v1.md)
- [分镜表](../03-visuals/storyboard-v1.csv)
- [关键帧清单](../03-visuals/keyframe-manifest-v1.csv)
- [图片提示词](../04-prompts/image-prompts-v1.md)
- [视频提示词](../04-prompts/video-prompts-v1-standalone.md)
- [剪辑方案](../05-editing/edit-plan-v1.md)
- [声音方案](../05-editing/sound-plan-v1.md)
- [声音登记](../05-editing/voice-anchor-register-v1.md)
- [发布材料](../06-publishing/publishing-v1.md)
