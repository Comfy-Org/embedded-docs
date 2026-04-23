> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/zh.md)

SDPoseFaceBBoxes 节点处理姿态关键点数据，以检测并生成人脸周围的边界框。它会分析帧中每个人的 2D 人脸关键点，基于这些点计算边界框，并可调整框的大小和形状。生成的边界框格式与 SDPose 工作流中的其他节点（如 SDPoseKeypointExtractor）兼容。

## 输入参数

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | 是 | - | 包含每帧检测到的人及其身体/面部关键点信息的姿态关键点数据。 |
| `scale` | FLOAT | 否 | 1.0 - 10.0 | 每个检测到的人脸周围边界框面积的乘数。值越大，生成的框越大。（默认值：1.5） |
| `force_square` | BOOLEAN | 否 | - | 扩展较短的边界框轴，使裁剪区域始终为正方形。（默认值：True） |

**注意：** `keypoints` 输入必须是由 SDPoseKeypointExtractor 等节点生成的特定格式，包含 `canvas_height`、`canvas_width` 以及每个人的 `face_keypoints_2d` 数据。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | 每帧的人脸边界框列表。每个边界框由其左上角坐标 (`x`, `y`)、`width` 和 `height` 定义。此输出与 SDPoseKeypointExtractor 节点的 `bboxes` 输入兼容。 |