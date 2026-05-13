> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/zh.md)

Wan22FunControlToVideo 节点使用 Wan 视频模型架构，为视频生成准备条件化（conditioning）和潜在空间（latent）表示。该节点处理正向和负向条件化输入，以及可选的参考图像和控制视频，为视频合成创建必要的潜在空间表示。节点处理空间缩放和时间维度，以生成适用于视频模型的条件化数据。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用于引导视频生成的正向条件化输入 |
| `negative` | CONDITIONING | 是 | - | 用于引导视频生成的负向条件化输入 |
| `vae` | VAE | 是 | - | 用于将图像编码到潜在空间的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频宽度（像素）（默认值：832，步长：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频高度（像素）（默认值：480，步长：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 视频序列中的帧数（默认值：81，步长：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 要生成的视频序列数量（默认值：1） |
| `ref_image` | IMAGE | 否 | - | 用于提供视觉引导的可选参考图像 |
| `control_video` | IMAGE | 否 | - | 用于引导生成过程的可选控制视频 |

**注意：** `length` 参数以 4 帧为块进行处理，节点会自动处理潜在空间的时间缩放。当提供 `ref_image` 时，它会通过参考潜在变量影响条件化。当提供 `control_video` 时，它会直接影响条件化中使用的拼接潜在表示。`start_image` 参数未作为此节点架构的输入公开，但在执行逻辑中被引用。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改后的正向条件化，包含视频特定的潜在数据，包括拼接潜在变量、遮罩和可选的参考潜在变量 |
| `negative` | CONDITIONING | 修改后的负向条件化，包含视频特定的潜在数据，包括拼接潜在变量、遮罩和可选的参考潜在变量 |
| `latent` | LATENT | 空的潜在张量，具有适合视频生成的适当维度，基于批次大小、潜在通道数以及空间/时间缩放 |

---
**Source fingerprint (SHA-256):** `8b24058f06aa9f779371a402c41cffc95d13ad0131d23d1438067d77755c73e2`
