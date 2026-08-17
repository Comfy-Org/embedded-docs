# Wan22FunControl视频

Wan22FunControlToVideo 节点使用 Wan 视频模型架构，为视频生成准备 conditioning 和潜在表示。它处理正向和负向的 conditioning 输入，以及可选的参考图像和控制视频，从而为视频合成创建必要的潜在空间表示。该节点通过处理空间缩放和时间维度，生成适合视频模型的 conditioning 数据。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导视频生成的正向 conditioning 输入 | CONDITIONING | 是 | - |
| `negative` | 用于引导视频生成的负向 conditioning 输入 | CONDITIONING | 是 | - |
| `vae` | 用于将图像编码到潜在空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频宽度（像素）（默认值：832，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频高度（像素）（默认值：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 视频序列中的帧数（默认值：81，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 要生成的视频序列数量（默认值：1） | INT | 是 | 1 to 4096 |
| `ref_image` | 可选的参考图像，用于提供视觉引导 | IMAGE | 否 | - |
| `control_video` | 可选的控制视频，用于引导生成过程 | IMAGE | 否 | - |

**注意：** `length` 参数按每 4 帧一组进行处理，节点会自动处理潜在空间的时间缩放。当提供 `ref_image` 时，它会通过参考潜在变量影响 conditioning。当提供 `control_video` 时，它会直接影响 conditioning 中使用的拼接潜在变量表示。`start_image` 参数未作为此节点结构中的输入公开，但在执行逻辑中被引用。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 修改后的正向 conditioning，包含特定于视频的潜在数据，包括拼接潜在变量、掩码以及可选的参考潜在变量 | CONDITIONING |
| `negative` | 修改后的负向 conditioning，包含特定于视频的潜在数据，包括拼接潜在变量、掩码以及可选的参考潜在变量 | CONDITIONING |
| `latent` | 具有适当维度的空潜在张量，用于视频生成，基于批次大小、潜在通道数以及空间/时间缩放 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
