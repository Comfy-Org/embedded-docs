# WanTrack视频

WanTrackToVideo 节点使用运动跟踪数据（点轨迹）来指导视频生成。它处理轨迹，并可选地与起始图像结合，为 Wan 视频模型生成条件化的正负输出以及潜在张量。当没有提供有效轨迹时，它会回退到标准的图像到视频转换。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于视频生成的正向条件 | CONDITIONING | 是 | - |
| `negative` | 用于视频生成的负向条件 | CONDITIONING | 是 | - |
| `vae` | 用于编码视频帧的 VAE 模型 | VAE | 是 | - |
| `tracks` | 包含点跟踪数据的 JSON 格式跟踪数据，以多行字符串形式表示（默认："[]"） | STRING | 是 | - |
| `width` | 输出视频宽度（像素）（默认：832，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频高度（像素）（默认：480，步长：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 输出视频的帧数（默认：81，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同时生成的视频数量（默认：1） | INT | 是 | 1 to 4096 |
| `temperature` | 用于运动修补的高级温度参数（默认：220.0，步长：0.1） | FLOAT | 是 | 1.0 to 1000.0 |
| `topk` | 用于运动修补的高级 top-k 值（默认：2） | INT | 是 | 1 to 10 |
| `start_image` | 用于视频生成第一帧的起始图像 | IMAGE | 是 | - |
| `clip_vision_output` | 用于额外条件的 CLIP 视觉输出 | CLIP_VISION_OUTPUT | 否 | - |

**注意：**
- `tracks` 输入需要 JSON 字符串或 JSON 字符串列表，其中包含点跟踪数据。如果 `tracks` 为空或无法解析，节点将回退到 WanImageToVideo 行为。
- 当提供 `start_image` 时，它会被调整大小以匹配 `width` 和 `height`，并用作视频序列的第一帧。
- 当提供 `clip_vision_output` 时，它会被添加到正向和负向条件中。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 应用了运动轨迹和可选图像信息的正向条件 | CONDITIONING |
| `negative` | 应用了运动轨迹和可选图像信息的负向条件 | CONDITIONING |
| `latent` | 按请求的视频尺寸、长度和批大小调整大小的零填充潜在张量 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
