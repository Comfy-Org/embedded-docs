# Pixal3DConditioning

此节点为 Trellis2 3D 生成流程准备图像条件输入。它通过 DINOv3 视觉模型从输入图像中以两种分辨率提取视觉特征，将其组织为分阶段特征图（可选择通过 NAF 模型增强），并结合根据水平视场角计算出的相机数据。节点输出一对正向和负向条件，其中负向条件使用零化特征以实现无分类器指导。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision。 | CLIP_VISION | 是 | — |
| `image` | 来自 ImageCropToMask 的预处理图像（Pixal3D 使用 pad_factor=1.1）。 | IMAGE | 是 | — |
| `camera_angle_x` | 水平视场角（度）（显示名称：fov）。可接入 MoGeGeometryToFOV（axis='horizontal'，unit='degrees'）以获得逐图像 FoV（与上游默认值一致）。默认值：49.13。 | FLOAT | 是 | 1.0 – 170.0 |

注意：`camera_angle_x` 值在内部转换为弧度，并用于计算投影变换矩阵的相机距离。当提供的视觉模型包含 NAF 组件时，节点还会为形状和纹理阶段生成高分辨率特征图。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 正向条件，包含从图像导出的特征图和用于 Trellis2 生成的投影数据。 | CONDITIONING |
| `negative` | 负向条件，包含零化特征张量，用于无分类器指导。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/zh.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
