> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/zh.md)

SVD_img2vid_Conditioning 节点用于准备基于 Stable Video Diffusion 的视频生成条件数据。它接收初始图像，通过 CLIP 视觉编码器和 VAE 编码器进行处理，生成正负条件对，以及用于视频生成的空潜在空间。该节点设置了控制生成视频中运动量、帧率和增强级别的必要参数。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 是 | - | 用于编码输入图像的 CLIP 视觉模型 |
| `init_image` | IMAGE | 是 | - | 用作视频生成起点的初始图像 |
| `vae` | VAE | 是 | - | 用于将图像编码到潜在空间的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频宽度（默认值：1024，步长：8） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 输出视频高度（默认值：576，步长：8） |
| `video_frames` | INT | 是 | 1 至 4096 | 生成视频的帧数（默认值：14） |
| `motion_bucket_id` | INT | 是 | 1 至 1023 | 控制生成视频中的运动量（默认值：127） |
| `fps` | INT | 是 | 1 至 1024 | 生成视频的帧率（默认值：6） |
| `augmentation_level` | FLOAT | 是 | 0.0 至 10.0 | 应用于输入图像的噪声增强级别（默认值：0.0，步长：0.01） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含图像嵌入和视频参数的正条件数据 |
| `negative` | CONDITIONING | 嵌入和视频参数归零后的负条件数据 |
| `latent` | LATENT | 准备用于视频生成的空潜在空间张量 |

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
