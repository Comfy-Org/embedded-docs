# 加载帧插值模型

## 概述

此节点从文件中加载帧插值模型，并为其在工作流中的使用做好准备。它会自动检测模型类型（FILM 或 RIFE），并配置模型以在您的硬件上实现最佳性能。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model_name` | 选择要加载的帧插值模型。模型必须放置在 `frame_interpolation` 文件夹中。 | COMBO | 是 | `frame_interpolation` 文件夹中的模型文件列表 |

注意：如果所选文件不是可识别的 FILM 或 RIFE 帧插值模型，节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | 已加载并配置好的帧插值模型，可直接用于其他节点。 | INTERP_MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/zh.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
