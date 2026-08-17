# 生成轨道

`GenerateTracks` 节点为视频生成创建多条平行运动路径。它定义了一条从起点到终点的首要路径，然后生成一组与之平行且等间距分布的轨道。您可以控制路径的形状（直线或贝塞尔曲线）、沿路径移动的速度以及轨道在哪些帧中可见。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 视频帧的宽度（以像素为单位）。默认值为 832。 | INT | 是 | 16 - 4096 |
| `height` | 视频帧的高度（以像素为单位）。默认值为 480。 | INT | 是 | 16 - 4096 |
| `start_x` | 起始位置的归一化 X 坐标（0-1）。默认值为 0.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `start_y` | 起始位置的归一化 Y 坐标（0-1）。默认值为 0.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `end_x` | 结束位置的归一化 X 坐标（0-1）。默认值为 1.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `end_y` | 结束位置的归一化 Y 坐标（0-1）。默认值为 1.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `num_frames` | 要生成轨道位置的总帧数。默认值为 81。 | INT | 是 | 1 - 1024 |
| `num_tracks` | 要生成的平行轨道数量。默认值为 5。 | INT | 是 | 1 - 100 |
| `track_spread` | 轨道之间的归一化距离。轨道垂直于运动方向展开。默认值为 0.025。 | FLOAT | 是 | 0.0 - 1.0 |
| `bezier` | 启用贝塞尔曲线路径，使用中点作为控制点。默认值为 False。 | BOOLEAN | 是 | True / False |
| `mid_x` | 贝塞尔曲线的归一化 X 控制点。仅在 `bezier` 启用时使用。默认值为 0.5。 | FLOAT | 是 | 0.0 - 1.0 |
| `mid_y` | 贝塞尔曲线的归一化 Y 控制点。仅在 `bezier` 启用时使用。默认值为 0.5。 | FLOAT | 是 | 0.0 - 1.0 |
| `interpolation` | 控制沿路径移动的时序/速度。默认值为 "linear"。使用 "constant" 时，所有点保持在起始位置。 | COMBO | 是 | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | 用于指示可见帧的可选遮罩。 | MASK | 否 | - |

**注意：** `mid_x` 和 `mid_y` 参数仅在 `bezier` 参数设置为 `True` 时使用。当 `bezier` 为 `False` 时，路径为从起点到终点的直线。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `TRACKS` | 一个轨道对象，包含所有帧中所有轨道的生成路径坐标和可见性信息。 | TRACKS |
| `track_length` | 生成轨道的帧数，与输入的 `num_frames` 相匹配。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/zh.md)

---
**Source fingerprint (SHA-256):** `4bd4d03a84f4b7ea260555b43f217af0b90dd4ca5196aca94e8f3886875ab912`
