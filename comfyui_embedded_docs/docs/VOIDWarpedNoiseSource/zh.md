# VOIDWarpedNoiseSource

## 概述

此节点将 LATENT（例如来自 VOIDWarpedNoise 节点的输出）转换为 NOISE 源。这样你就可以将扭曲噪声与 SamplerCustomAdvanced 节点一起使用，以实现更可控的图像生成。

## 输入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `warped_noise` | 来自 VOIDWarpedNoise 的扭曲噪声潜空间表示 | LATENT | Yes | N/A |

## 输出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `NOISE` | 可与 SamplerCustomAdvanced 配合使用的噪声源 | NOISE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/zh.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
