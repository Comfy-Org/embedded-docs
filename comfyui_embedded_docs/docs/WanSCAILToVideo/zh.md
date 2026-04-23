> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh.md)

WanSCAILToVideo 节点为视频生成准备条件输入和空潜空间。它处理可选输入，如参考图像、姿态视频和 CLIP 视觉输出，并将它们嵌入到视频模型的正向和负向条件中。该节点输出修改后的条件输入以及指定视频尺寸的空白潜张量。

## 输入参数

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向条件输入。 |
| `negative` | CONDITIONING | 是 | - | 负向条件输入。 |
| `vae` | VAE | 是 | - | 用于编码图像和视频帧的 VAE 模型。 |
| `width` | INT | 是 | 32 至 MAX_RESOLUTION | 输出视频的宽度（像素），默认为 512。必须能被 8 整除。 |
| `height` | INT | 是 | 32 至 MAX_RESOLUTION | 输出视频的高度（像素），默认为 896。必须能被 8 整除。 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 视频的帧数，默认为 81。 |
| `batch_size` | INT | 是 | 1 至 4096 | 批量生成的视频数量，默认为 1。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 用于条件输入的可选 CLIP 视觉输出。 |
| `reference_image` | IMAGE | 否 | - | 用于条件输入的可选参考图像。 |
| `pose_video` | IMAGE | 否 | - | 用于姿态条件输入的视频。将被下采样至主视频分辨率的一半。 |
| `pose_strength` | FLOAT | 是 | 0.0 至 10.0 | 姿态潜变量的强度，默认为 1.0。 |
| `pose_start` | FLOAT | 是 | 0.0 至 1.0 | 开始使用姿态条件输入的步骤，默认为 0.0。 |
| `pose_end` | FLOAT | 是 | 0.0 至 1.0 | 结束使用姿态条件输入的步骤，默认为 1.0。 |

**注意：** `pose_video` 输入仅处理前 `length` 帧。`reference_image` 仅处理批次中的第一张图像。

## 输出参数

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改后的正向条件输入，可能包含嵌入的参考图像潜变量、CLIP 视觉输出或姿态视频潜变量。 |
| `negative` | CONDITIONING | 修改后的负向条件输入，可能包含嵌入的参考图像潜变量、CLIP 视觉输出或姿态视频潜变量。 |
| `latent` | LATENT | 一个形状为 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空潜张量。 |