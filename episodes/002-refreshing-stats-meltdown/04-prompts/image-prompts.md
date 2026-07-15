# 连续画面生成提示词

## 全局约束

- 参考图只用于锁定角色身份，不照搬参考图背景。
- 保留白色圆形电阻身体、灰色电阻腰带、锯齿电阻纹、蓝色电路纹、黄色闪电和黑色粗线条。
- 竖版 9:16，角色始终是唯一主角，现代卡通动画电影质感。
- 表情与动作逐张升级：不安、错愕、惊恐、癫狂、过载瘫倒。
- 画面不生成任何文字、数字、Logo、水印或平台界面；字幕后期添加。
- 角色不得变成机器人、蛋、猫或真人，不增加多余四肢。

## 已生成文件

| 顺序 | 文件 | 情绪与动作 |
|---:|---|---|
| 1 | `03-visuals/01-signal-no-response.png` | 发布后等待，弱信号发出又消失，轻微不安 |
| 2 | `03-visuals/02-forty-views-shock.png` | 贴近手机，瞳孔放大，突然错愕 |
| 3 | `03-visuals/03-zero-interactions-panic.png` | 向后弹起，双手张开，电流爆发，惊恐尖叫 |
| 4 | `03-visuals/04-refresh-meltdown.png` | 疯狂点击刷新，旋涡眼、残影、电流风暴 |
| 5 | `03-visuals/05-overheated-aftermath.png` | 过载瘫倒，冒烟，仍想伸手刷新 |

## 最终提示词结构

五张图均使用以下结构生成：

1. 原始 IP 图作为强制角色身份参考。
2. 上一张成图作为房间、灯光、构图和动画质感的连续性参考。
3. 明确本帧动作与情绪升级阶段。
4. 重复角色不变量与“一对手脚、无文字、无数字、无界面”的约束。
5. 竖版 9:16，并为后期字幕留安全区。

统一风格关键词：

~~~text
polished expressive 2D cartoon animation keyframe,
cinematic comedy, hand-drawn kinetic energy,
cool blue night lighting with warm ring-light accent,
same room and same resistor mascot, vertical 9:16
~~~
