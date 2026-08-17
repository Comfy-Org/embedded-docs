# SD_4X放大条件

SD_4XUpscale_Conditioning 节点用于准备扩散模型放大图像所需的 conditioning 数据。它接收输入图像和 conditioning 数据，然后应用缩放和噪声增强，生成用于引导放大过程的修改后 conditioning。该节点输出正负 conditioning 以及对应放大尺寸的潜在表示。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 待放大的输入图像 | IMAGE | 是 | - |
| `positive` | 正向 conditioning 数据，用于引导生成趋向期望内容 | CONDITIONING | 是 | - |
| `negative` | 负向 conditioning 数据，用于引导生成远离不想要的内容 | CONDITIONING | 是 | - |
| `scale_ratio` | 应用于输入图像的缩放因子（默认值：4.0） | FLOAT | 是 | 0.0 - 10.0 |
| `noise_augmentation` | 放大过程中添加的噪声量（默认值：0.0） | FLOAT | 是 | 0.0 - 1.0 |

目标放大尺寸通过将输入图像尺寸乘以 `scale_ratio` 计算得出。嵌入在 conditioning 中的图像以及输出的潜在表示均按目标尺寸的四分之一创建。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 应用了放大信息的修改后正向 conditioning | CONDITIONING |
| `negative` | 应用了放大信息的修改后负向 conditioning | CONDITIONING |
| `latent` | 与放大尺寸匹配的空潜在表示 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
