# StableZero123条件_批处理

StableZero123_Conditioning_Batched 节点用于准备使用 Stable Zero123 模型生成物体 3D 视图所需的条件数据。它使用 CLIP 视觉模型和 VAE 对输入图像进行编码，将图像特征与批次中每个项目的相机仰角（elevation）和方位角（azimuth）相结合，并输出正向条件、负向条件以及一个空 latent。批次增量输入会依次提高或降低批次中每个连续项目的相机角度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用于将输入图像编码为图像嵌入的 CLIP 视觉模型 | CLIP_VISION | 是 | - |
| `init_image` | 要处理并编码的初始输入图像 | IMAGE | 是 | - |
| `vae` | 用于将图像像素编码到潜空间（latent space）的 VAE 模型 | VAE | 是 | - |
| `width` | 处理后图像的目标宽度（默认：256） | INT | 是 | 16 to MAX_RESOLUTION (step 8) |
| `height` | 处理后图像的目标高度（默认：256） | INT | 是 | 16 to MAX_RESOLUTION (step 8) |
| `batch_size` | 批次中要生成的条件样本数量（默认：1） | INT | 是 | 1 to 4096 |
| `elevation` | 起始相机仰角，单位为度（默认：0.0） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |
| `azimuth` | 起始相机方位角，单位为度（默认：0.0） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |
| `elevation_batch_increment` | 批次中每个连续项目的仰角增加值（默认：0.0，高级参数） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |
| `azimuth_batch_increment` | 批次中每个连续项目的方位角增加值（默认：0.0，高级参数） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |

**注意：** `width` 和 `height` 的值必须是 8 的倍数（选择步长为 8 可确保这一点），因为节点会将它们除以 8 来构建 latent 维度。对于批次中的每个项目，`elevation` 和 `azimuth` 的值会分别增加 `elevation_batch_increment` 和 `azimuth_batch_increment`，因此批次中的连续项目会获得逐步递增的相机角度。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 正向条件，包含图像嵌入、相机嵌入以及生成时用于拼接的已编码输入图像 | CONDITIONING |
| `negative` | 负向条件，使用零初始化的图像嵌入和用于拼接的零 latent | CONDITIONING |
| `latent` | 空 latent 张量，维度为 (batch_size, 4, height/8, width/8)，包含批次索引信息 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/zh.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
