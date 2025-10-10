> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/zh.md)

> 本文档由 AI 生成，如果您发现任何错误或有改进建议，请随时贡献！[在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/en.md)

LTXVImgToVideo 节点将输入图像转换为视频生成模型所需的视频潜在表示。它接收单张图像，使用 VAE 编码器将其扩展为帧序列，然后应用带强度控制的调节，以确定在视频生成过程中保留原始图像内容与修改内容的比例。

## 输入参数

| 参数 | 数据类型 | 必需 | 取值范围 | 描述 |
|-------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用于引导视频生成的正向调节提示 |
| `negative` | CONDITIONING | 是 | - | 用于避免视频中出现特定元素的负向调节提示 |
| `vae` | VAE | 是 | - | 用于将输入图像编码到潜在空间的 VAE 模型 |
| `image` | IMAGE | 是 | - | 待转换为视频帧的输入图像 |
| `width` | INT | 否 | 64 至 MAX_RESOLUTION | 输出视频宽度（像素）（默认：768，步长：32） |
| `height` | INT | 否 | 64 至 MAX_RESOLUTION | 输出视频高度（像素）（默认：512，步长：32） |
| `length` | INT | 否 | 9 至 MAX_RESOLUTION | 生成视频的帧数（默认：97，步长：8） |
| `batch_size` | INT | 否 | 1 至 4096 | 同时生成的视频数量（默认：1） |
| `strength` | FLOAT | 否 | 0.0 至 1.0 | 控制视频生成过程中对原始图像的修改程度，1.0 保留最多原始内容，0.0 允许最大程度修改（默认：1.0） |

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 应用视频帧掩码处理后的正向调节 |
| `negative` | CONDITIONING | 应用视频帧掩码处理后的负向调节 |
| `latent` | LATENT | 包含编码帧和噪声掩码的视频潜在表示，用于视频生成 |