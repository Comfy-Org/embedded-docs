> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/zh.md)

WanVaceToVideo 节点为视频生成模型处理视频条件数据。它接收正向和负向条件输入以及视频控制数据，并为视频生成准备潜在表示。该节点处理视频放大、遮罩和 VAE 编码，为视频模型创建适当的结构。

## 输入参数

| 参数 | 数据类型 | 必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用于引导生成的正向条件输入 |
| `negative` | CONDITIONING | 是 | - | 用于引导生成的负向条件输入 |
| `vae` | VAE | 是 | - | 用于编码图像和视频帧的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频宽度（像素）（默认：832，步长：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频高度（像素）（默认：480，步长：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 视频帧数（默认：81，步长：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 同时生成的视频数量（默认：1） |
| `strength` | FLOAT | 是 | 0.0 至 1000.0 | 视频条件控制强度（默认：1.0，步长：0.01） |
| `control_video` | IMAGE | 否 | - | 用于控制条件的可选输入视频 |
| `control_masks` | MASK | 否 | - | 用于控制视频修改区域的可选遮罩 |
| `reference_image` | IMAGE | 否 | - | 用于附加条件的可选参考图像 |

**注意：** 当提供 `control_video` 时，它将被放大以匹配指定的宽度和高度。如果提供了 `control_masks`，则必须与控制视频的尺寸匹配。当提供 `reference_image` 时，它通过 VAE 编码并预置到潜在序列中。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 应用了视频控制数据的正向条件 |
| `negative` | CONDITIONING | 应用了视频控制数据的负向条件 |
| `latent` | LATENT | 准备用于视频生成的空潜在张量 |
| `trim_latent` | INT | 使用参考图像时需要修剪的潜在帧数 |