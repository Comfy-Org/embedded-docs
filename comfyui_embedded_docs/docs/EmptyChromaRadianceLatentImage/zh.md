# 空Latent图像（ChromaRadiance）

EmptyChromaRadianceLatentImage 节点创建一个指定尺寸的空白潜在图像，用于 chroma radiance 工作流。它生成一个填充为零的张量（包含 3 个颜色通道），作为潜在空间操作的起点。该节点允许你定义空潜在图像的宽度、高度和批次大小。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 潜在图像的宽度（以像素为单位）（默认值：1024，必须能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 潜在图像的高度（以像素为单位）（默认值：1024，必须能被 16 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `batch_size` | 一个批次中生成的潜在图像数量（默认值：1） | INT | 否 | 1 to 4096 |

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 生成的指定尺寸的空潜在图像张量，填充为零 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/zh.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
