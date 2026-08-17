# WanSCAILToVideo

WanSCAILToVideo 节点为视频生成准备 conditioning 和空的潜在空间。它处理可选输入，如参考图像、姿态视频、CLIP 视觉输出和先前帧块，并将它们嵌入到视频模型的正向和负向 conditioning 中。该节点输出修改后的 conditioning 和指定视频尺寸的空白潜在张量。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 正向 conditioning 输入。 | CONDITIONING | 是 | - |
| `negative` | 负向 conditioning 输入。 | CONDITIONING | 是 | - |
| `vae` | 用于编码图像和视频帧的 VAE 模型。 | VAE | 是 | - |
| `width` | 输出视频的宽度（像素）（默认：512）。可按 32 的步长调整。 | INT | 是 | 32 to MAX_RESOLUTION |
| `height` | 输出视频的高度（像素）（默认：896）。可按 32 的步长调整。 | INT | 是 | 32 to MAX_RESOLUTION |
| `length` | 视频的帧数（默认：81）。可从 1 开始按 4 的步长调整。 | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 批次中生成的视频数量（默认：1）。 | INT | 是 | 1 to 4096 |
| `pose_strength` | 姿态潜在特征的强度（默认：1.0）。 | FLOAT | 是 | 0.0 to 10.0 |
| `pose_start` | 姿态 conditioning 的起始步（默认：0.0）。 | FLOAT | 是 | 0.0 to 1.0 |
| `pose_end` | 姿态 conditioning 的结束步（默认：1.0）。 | FLOAT | 是 | 0.0 to 1.0 |
| `video_frame_offset` | 此块开始的累积输出帧数。从前一块的 `video_frame_offset` 输出连接（默认：0）。 | INT | 是 | 0 to MAX_RESOLUTION |
| `previous_frame_count` | 用于锚定的 `previous_frames` 尾部帧数。SCAIL-2 在 5 处训练（81 帧块，76 帧步长）（默认：5）。 | INT | 是 | 1 to MAX_RESOLUTION |
| `pose_video` | 用于姿态 conditioning 的视频。将被缩小到主视频分辨率的一半。 | IMAGE | 否 | - |
| `pose_video_mask` | 仅限 SCAIL-2。与 `pose_video` 分辨率相同的按身份着色的 SAM3 掩码视频。 | IMAGE | 否 | - |
| `replacement_mode` | 仅限 SCAIL-2。False = 动画模式（`pose_video_mask` 应为黑色背景）。True = 替换模式（`pose_video_mask` 应为白色背景）。默认：False。 | BOOLEAN | 否 | - |
| `reference_image` | 参考图像。第一张图像是主要参考（将所有身份合成到其上）。SCAIL-2：额外的批次图像用作附加视图（背面视图、特写、被遮挡背景），每个都需要匹配该身份颜色的 `reference_image_mask`。 | IMAGE | 否 | - |
| `reference_image_mask` | 仅限 SCAIL-2。着色参考掩码，批次与 `reference_image` 匹配（第一个 = 主要参考掩码，其余 = 附加 `reference_image` 的身份掩码）。 | IMAGE | 否 | - |
| `clip_vision_output` | 用于 conditioning 的 CLIP 视觉特征。模型使用拉伸调整到宽高比进行训练。 | CLIP_VISION_OUTPUT | 否 | - |
| `previous_frames` | 仅限 SCAIL-2。前一个块的完整解码输出。仅使用最后 `previous_frame_count` 帧作为扩展锚定。 | IMAGE | 否 | - |

**注意：**

- `pose_video` 和 `pose_video_mask` 输入从 `video_frame_offset` 处开始切片；如果视频在该偏移之后没有帧，则忽略。然后它们被一起截断为两者中较短的长度，并限制为 `length` 帧。`pose_video` 在编码前被缩小到主视频分辨率的一半。
- `reference_image_mask` 输入仅在同时提供 `reference_image` 时生效。`reference_image` 批次中的每个图像分别编码为单帧潜在参考。在替换模式（`replacement_mode=True`）下，参考图像使用参考图像掩码作为 alpha 遮罩合成到黑色背景上。
- 当提供 `clip_vision_output` 时，它应用于正向和负向 conditioning。
- 当提供 `previous_frames` 时，仅使用最后 `previous_frame_count` 帧作为扩展锚定。输出潜在部分填充有这些帧的编码，潜在输出中包含噪声掩码，并且通过减去保留帧数（不低于 0）来调整 `video_frame_offset`。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 修改后的正向 conditioning，可能包含嵌入的参考图像潜在特征、CLIP 视觉输出、姿态视频潜在特征、驱动掩码、参考掩码或先前帧潜在特征。 | CONDITIONING |
| `negative` | 修改后的负向 conditioning，可能包含嵌入的参考图像潜在特征、CLIP 视觉输出、姿态视频潜在特征、驱动掩码、参考掩码或先前帧潜在特征。 | CONDITIONING |
| `latent` | 形状为 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空潜在张量。当提供 `previous_frames` 时，潜在部分填充有编码的先前帧，并包含噪声掩码。 | LATENT |
| `video_frame_offset` | 调整后的偏移量 + 长度。连接到下一个块以进行顺序视频生成。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
