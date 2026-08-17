# StableZero123条件

`StableZero123_Conditioning` 节点处理输入图像和相机角度，为 3D 模型生成生成条件数据和潜在表示。它使用 CLIP vision 模型对图像特征进行编码，结合基于仰角和方位角的相机嵌入信息，并生成正条件和负条件以及用于下游 3D 生成任务的潜在表示。

## 输入

| 参数 | 描述 | 数据类型 | 是否必须 | 范围 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用于编码图像特征的 CLIP vision 模型 | CLIP_VISION | 是 | - |
| `init_image` | 待处理和编码的输入图像 | IMAGE | 是 | - |
| `vae` | 用于将像素编码到潜在空间的 VAE 模型 | VAE | 是 | - |
| `width` | 潜在表示的输出宽度（默认值：256，必须能被 8 整除） | INT | 是 | 16 到 MAX_RESOLUTION |
| `height` | 潜在表示的输出高度（默认值：256，必须能被 8 整除） | INT | 是 | 16 到 MAX_RESOLUTION |
| `batch_size` | 批次中生成的样本数量（默认值：1） | INT | 是 | 1 到 4096 |
| `elevation` | 相机仰角，单位为度（默认值：0.0） | FLOAT | 是 | -180.0 到 180.0 |
| `azimuth` | 相机方位角，单位为度（默认值：0.0） | FLOAT | 是 | -180.0 到 180.0 |

**注意：** `width` 和 `height` 参数必须能被 8 整除，因为节点会自动将它们除以 8 来创建潜在表示的维度。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 结合图像特征和相机嵌入的正条件数据 | CONDITIONING |
| `negative` | 使用零初始化特征的负条件数据 | CONDITIONING |
| `latent` | 维度为 [batch_size, 4, height//8, width//8] 的潜在表示 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
