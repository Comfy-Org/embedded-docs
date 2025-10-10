> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh.md)

WanImageToVideo 节点为视频生成任务准备条件约束和潜在表示。它创建一个用于视频生成的空潜在空间，并可以选择性地结合起始图像和 CLIP 视觉输出来指导视频生成过程。该节点会根据提供的图像和视觉数据修改正向和负向条件约束输入。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用于引导生成的正向条件约束输入 |
| `negative` | CONDITIONING | 是 | - | 用于引导生成的负向条件约束输入 |
| `vae` | VAE | 是 | - | 用于将图像编码到潜在空间的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频的宽度（默认：832，步长：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频的高度（默认：480，步长：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 视频中的帧数（默认：81，步长：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 单次批量生成的视频数量（默认：1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 用于附加条件约束的可选 CLIP 视觉输出 |
| `start_image` | IMAGE | 否 | - | 用于初始化视频生成的可选起始图像 |

**注意：** 当提供 `start_image` 时，节点会对图像序列进行编码并对条件约束输入应用掩码处理。当提供 `clip_vision_output` 参数时，会向正向和负向输入添加基于视觉的条件约束。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 融合了图像和视觉数据的修改后正向条件约束 |
| `negative` | CONDITIONING | 融合了图像和视觉数据的修改后负向条件约束 |
| `latent` | LATENT | 准备用于视频生成的空潜在空间张量 |