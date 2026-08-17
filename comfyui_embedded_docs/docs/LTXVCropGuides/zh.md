# LTXV裁剪指导

LTXVCropGuides 节点通过移除关键帧信息并调整潜空间维度来处理用于视频生成的条件输入和潜空间输入。它会裁剪潜空间图像和噪声掩码以排除关键帧部分，同时清除正向和负向条件输入中的关键帧索引。这为不需要关键帧引导的视频生成工作流准备好了数据。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 包含用于生成指导信息的正向条件输入 | CONDITIONING | 是 | - |
| `negative` | 包含生成时需要避免内容的负向条件输入 | CONDITIONING | 是 | - |
| `latent` | 包含图像样本和噪声掩码数据的潜空间表示 | LATENT | 是 | - |

注意：如果正向条件不包含关键帧索引，则节点将原样返回正向、负向和潜空间输入。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已处理的正向条件，其中关键帧索引和引导注意力条目已被清除 | CONDITIONING |
| `negative` | 已处理的负向条件，其中关键帧索引和引导注意力条目已被清除 | CONDITIONING |
| `latent` | 已裁剪的潜空间表示，具有调整后的样本和噪声掩码，其中关键帧部分已被移除 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/zh.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
