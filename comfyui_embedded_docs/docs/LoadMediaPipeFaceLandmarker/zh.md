# 加载 MediaPipe 人脸标记器

此节点加载一个 MediaPipe Face Landmarker v2 模型，该模型可检测图像中的人脸及面部关键点（如眼睛、鼻子和嘴巴）。加载后的模型包含两个检测变体（short 和 full），以及用于面部分析的共享网格数据、混合形状和规范几何结构。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 来自 `models/detection/` 目录的人脸检测模型。 | COMBO | 是 | `models/detection/` 目录中可用的模型列表 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `FACE_DETECTION_MODEL` | 一个已加载的 MediaPipe Face Landmarker 模型对象，包含两个检测变体（short/full）、共享网格与混合形状数据、规范几何结构、面部拓扑连接集，以及用于 GPU 管理的模型修补器。 | FACE_DETECTION_MODEL |

**注意：** 该输出是一个复杂对象，可供其他节点用于人脸检测和关键点提取任务。它包含两个检测变体：“short”用于近距离检测，“full”用于全距离检测。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/zh.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
