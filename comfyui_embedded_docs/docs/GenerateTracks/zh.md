> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/zh.md)

`GenerateTracks` 节点用于为视频生成创建多条平行运动路径。它定义一条从起点到终点的主路径，然后生成一组与该路径平行且等距分布的轨道。您可以控制路径的形状（直线或贝塞尔曲线）、沿路径移动的速度以及轨道可见的帧范围。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 16 - 4096 | 视频帧的宽度（像素）。默认值为 832。 |
| `height` | INT | 是 | 16 - 4096 | 视频帧的高度（像素）。默认值为 480。 |
| `start_x` | FLOAT | 是 | 0.0 - 1.0 | 起始位置的归一化 X 坐标（0-1）。默认值为 0.0。 |
| `start_y` | FLOAT | 是 | 0.0 - 1.0 | 起始位置的归一化 Y 坐标（0-1）。默认值为 0.0。 |
| `end_x` | FLOAT | 是 | 0.0 - 1.0 | 结束位置的归一化 X 坐标（0-1）。默认值为 1.0。 |
| `end_y` | FLOAT | 是 | 0.0 - 1.0 | 结束位置的归一化 Y 坐标（0-1）。默认值为 1.0。 |
| `num_frames` | INT | 是 | 1 - 1024 | 需要生成轨道位置的总帧数。默认值为 81。 |
| `num_tracks` | INT | 是 | 1 - 100 | 要生成的平行轨道数量。默认值为 5。 |
| `track_spread` | FLOAT | 是 | 0.0 - 1.0 | 轨道之间的归一化距离。轨道沿运动方向的垂直方向分布。默认值为 0.025。 |
| `bezier` | BOOLEAN | 是 | True / False | 启用贝塞尔曲线路径，使用中点作为控制点。默认值为 False。 |
| `mid_x` | FLOAT | 是 | 0.0 - 1.0 | 贝塞尔曲线的归一化 X 控制点。仅在启用 `bezier` 时使用。默认值为 0.5。 |
| `mid_y` | FLOAT | 是 | 0.0 - 1.0 | 贝塞尔曲线的归一化 Y 控制点。仅在启用 `bezier` 时使用。默认值为 0.5。 |
| `interpolation` | COMBO | 是 | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | 控制沿路径移动的时间/速度。默认值为 "linear"。 |
| `track_mask` | MASK | 否 | - | 可选的遮罩，用于指示可见帧。 |

**注意：** `mid_x` 和 `mid_y` 参数仅在 `bezier` 参数设置为 `True` 时使用。当 `bezier` 为 `False` 时，路径为从起点到终点的直线。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | 一个轨道对象，包含所有帧中所有轨道的生成路径坐标和可见性信息。 |
| `track_length` | INT | 生成轨道的帧数，与输入的 `num_frames` 一致。 |

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
