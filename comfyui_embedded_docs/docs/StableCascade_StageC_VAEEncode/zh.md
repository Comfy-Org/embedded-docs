# Stable Cascade_C阶段_VAE编码

StableCascade_StageC_VAEEncode 节点通过 VAE 编码器处理输入图像，为 Stable Cascade 模型生成潜在表示。它首先根据压缩因子和 VAE 的下采样比率调整图像大小，然后对调整后的图像进行编码。该节点输出两个潜在张量：一个用于 stage C（实际编码结果），另一个用于 stage B（零填充占位符）。

## 输入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image` | 要编码到潜在空间的输入图像 | IMAGE | 是 | - |
| `vae` | 用于编码图像的 VAE 模型 | VAE | 是 | - |
| `compression` | 编码前应用于图像的压缩因子。图像尺寸除以该值，然后乘以 VAE 的下采样比率。（默认值：42） | INT | 否 | 4-128 |

## 输出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `stage_c` | Stable Cascade 模型 stage C 的编码潜在表示 | LATENT |
| `stage_b` | stage B 的占位潜在表示。当前返回一个零填充张量，其维度根据输入图像大小计算。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/zh.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
