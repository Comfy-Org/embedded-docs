# WanMove预览轨道

WanMoveVisualizeTracks 节点将运动跟踪数据绘制到一系列图像或视频帧上。它在每个跟踪点的当前位置绘制一个圆圈，并绘制一条渐隐的路径线，显示该点在最近几帧中的移动轨迹。如果未提供跟踪数据，则输入图像将原样返回。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 将在其上可视化轨迹的输入图像或视频帧序列。 | IMAGE | 是 | - |
| `tracks` | 包含点位置和可见性信息的运动跟踪数据。如果未提供，则输入图像将原样通过。 | TRACKS | 否 | - |
| `line_resolution` | 绘制每个轨迹的尾迹路径线时使用的先前帧数（默认值：24）。 | INT | 是 | 1 - 1024 |
| `circle_size` | 绘制在每个跟踪点当前位置的圆圈大小（默认值：12）。 | INT | 是 | 1 - 128 |
| `opacity` | 所绘制轨迹叠加层的透明度（默认值：0.75）。 | FLOAT | 是 | 0.0 - 1.0 |
| `line_width` | 用于绘制轨迹路径的线条宽度（默认值：16）。 | INT | 是 | 1 - 128 |

**注意：** 如果输入图像的数量与所提供的 `tracks` 数据中的帧数不匹配，则输入图像序列将重复以与轨迹数据对齐。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| IMAGE | 带有运动跟踪数据叠加层的图像序列。如果未提供 `tracks`，则原始输入图像将原样返回。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/zh.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
