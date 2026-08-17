# SDPoseDrawKeypoints

SDPoseDrawKeypoints 节点接收姿态估计数据（关键点），并将其绘制为空白画布上的可视化骨架。它允许你选择性地绘制姿态的不同部分，如身体、头部、手部、面部和脚部，并可自定义线条宽度和点大小。生成的图像可用于可视化，或作为其他需要姿态图像的节点的输入。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `keypoints` | 要绘制的姿态关键点数据。该数据通常来自姿态检测节点。 | POSE_KEYPOINT | 是 | - |
| `draw_body` | 控制是否绘制主体骨架（默认：True）。 | BOOLEAN | 否 | - |
| `draw_hands` | 控制是否绘制手部关键点（默认：True）。 | BOOLEAN | 否 | - |
| `draw_face` | 控制是否绘制面部关键点（默认：True）。 | BOOLEAN | 否 | - |
| `draw_feet` | 控制是否绘制脚部关键点（默认：False）。 | BOOLEAN | 否 | - |
| `stick_width` | 用于绘制身体骨架的线条宽度（默认：4）。 | INT | 否 | 1 to 10 |
| `face_point_size` | 用于绘制面部关键点的点大小（默认：3）。 | INT | 否 | 1 to 10 |
| `score_threshold` | 关键点必须具备的最低置信度分数才能被绘制。分数低于此值的关键点将被忽略（默认：0.3）。 | FLOAT | 否 | 0.0 to 1.0 |
| `draw_head` | 控制是否绘制头部关键点（鼻子、眼睛、耳朵）和头部连线（默认：True）。 | BOOLEAN | 否 | - |

**注意：** 如果 `keypoints` 输入为空或为 `None`，节点将输出一张空白的 64x64 图像。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 带有已绘制姿态关键点的图像。图像尺寸与输入关键点数据中指定的 `canvas_height` 和 `canvas_width` 一致。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/zh.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
