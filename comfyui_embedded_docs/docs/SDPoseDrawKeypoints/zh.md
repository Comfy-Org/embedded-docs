> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/zh.md)

SDPoseDrawKeypoints 节点接收姿态估计数据（关键点）并在空白画布上将其绘制为可视化的骨架。它允许您选择性地绘制姿态的不同部分，例如身体、手部、面部和脚部，并可以自定义线条宽度和点的大小。生成的图像可用于可视化，或作为其他需要姿态图像的节点的输入。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | 是 | - | 要绘制的姿态关键点数据。此数据通常来自姿态检测节点。 |
| `draw_body` | BOOLEAN | 否 | - | 控制是否绘制主体骨架（默认：True）。 |
| `draw_hands` | BOOLEAN | 否 | - | 控制是否绘制手部关键点（默认：True）。 |
| `draw_face` | BOOLEAN | 否 | - | 控制是否绘制面部关键点（默认：True）。 |
| `draw_feet` | BOOLEAN | 否 | - | 控制是否绘制脚部关键点（默认：False）。 |
| `stick_width` | INT | 否 | 1 到 10 | 用于绘制身体骨架的线条宽度（默认：4）。 |
| `face_point_size` | INT | 否 | 1 到 10 | 用于绘制面部关键点的点的大小（默认：3）。 |
| `score_threshold` | FLOAT | 否 | 0.0 到 1.0 | 关键点被绘制所需的最低置信度分数。低于此值的关节点将被忽略（默认：0.3）。 |

**注意：** 如果 `keypoints` 输入为空或为 `None`，节点将输出一个空白的 64x64 图像。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 包含已绘制姿态关键点的图像。图像尺寸与输入关键点数据中指定的 `canvas_height` 和 `canvas_width` 相匹配。 |