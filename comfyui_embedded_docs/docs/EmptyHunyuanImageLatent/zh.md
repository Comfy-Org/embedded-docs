# 空Latent图像（Hunyuan）

EmptyHunyuanImageLatent 节点会创建一个具有特定尺寸的空潜空间张量，用于 Hunyuan 图像生成模型。它会生成一个空白起始点，供工作流中的后续节点处理。该节点允许你指定潜空间的宽度、高度和批大小。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `width` | 生成的潜空间图像的宽度，单位为像素（默认值：2048，步长：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `height` | 生成的潜空间图像的高度，单位为像素（默认值：2048，步长：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `batch_size` | 一批中生成的潜空间样本数量（默认值：1） | INT | 是 | 1 to 4096 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `LATENT` | 用于 Hunyuan 图像处理的、具有指定尺寸的空潜空间张量。该张量有 64 个通道，其空间尺寸为请求宽度和高度的三十二分之一（1/32）。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/zh.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
