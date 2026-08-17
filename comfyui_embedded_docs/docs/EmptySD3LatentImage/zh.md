# 空Latent图像（SD3）

EmptySD3LatentImage 节点创建一个空白潜在图像张量，该张量专门针对 Stable Diffusion 3 模型格式化。它生成一个填充为零的张量，具有 SD3 流水线所期望的正确尺寸和结构。通常用作图像生成工作流的起点。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 输出潜在图像的宽度（以像素为单位）（默认：1024） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 输出潜在图像的高度（以像素为单位）（默认：1024） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `batch_size` | 一批中生成的潜在图像数量（默认：1） | INT | 是 | 1 to 4096 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 包含空白样本的潜在张量，其维度与 SD3 兼容。该张量有 16 个通道，空间尺寸相较于输入的宽度和高度缩小为 1/8。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/zh.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
