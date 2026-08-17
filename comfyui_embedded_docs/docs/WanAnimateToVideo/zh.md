# Wan动画转视频

此实验性节点通过将参考图像与可选的姿态、人脸和背景视频组合，为 Wan 视频生成做准备。它会构建条件数据和用于后续生成的空潜空间视频张量，并返回帧偏移信息，帮助分块扩展现有视频。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 用于引导生成过程趋向期望内容的正面条件。 | CONDITIONING | 是 | - |
| `negative` | 用于引导生成过程远离不需要内容的负面条件。 | CONDITIONING | 是 | - |
| `vae` | 用于编码和解码图像数据的 VAE 模型。 | VAE | 是 | - |
| `width` | 输出视频宽度（像素）（默认值：832，步长：16）。 | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 输出视频高度（像素）（默认值：480，步长：16）。 | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 要生成的帧数（默认值：77，步长：4）。 | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 单批生成的视频数量（默认值：1）。 | INT | 是 | 1 to 4096 |
| `clip_vision_output` | 可选的 CLIP 视觉模型输出，用作正向和负向条件的附加条件。 | CLIP_VISION_OUTPUT | 否 | - |
| `reference_image` | 用作生成起点的参考图像。如果未提供，则使用黑色图像（全零）。 | IMAGE | 否 | - |
| `face_video` | 提供面部表情引导的视频。处理时会调整为 512x512，并归一化到 -1.0 到 1.0 的范围。 | IMAGE | 否 | - |
| `pose_video` | 提供姿态和动作引导的视频。如果其长度短于 `length`，则使用其最后一帧进行填充。 | IMAGE | 否 | - |
| `continue_motion_max_frames` | 从前一段动作继续的最大帧数。仅使用 `continue_motion` 的最后这么多帧（默认值：5，步长：4）。 | INT | 是 | 1 to MAX_RESOLUTION |
| `background_video` | 用于与生成内容合成的背景视频。 | IMAGE | 否 | - |
| `character_mask` | 定义角色区域以进行选择性处理的遮罩。如果遮罩只有一帧，则会在所有帧中重复使用。 | MASK | 否 | - |
| `continue_motion` | 用于在扩展视频时保持时间一致性的前一段动作序列。仅使用最后 `continue_motion_max_frames` 帧。 | IMAGE | 否 | - |
| `video_frame_offset` | 在所有输入视频中要跳过的帧数。用于按块生成更长的视频。连接上一个节点的 video_frame_offset 输出以扩展视频。（默认值：0，步长：1） | INT | 是 | 0 to MAX_RESOLUTION |

**参数约束：**

- 当提供 `pose_video` 时，较短的姿态视频会用其最后一帧填充，以匹配 `length`。源代码中有一个 `trim_to_pose_video` 标志（当前已禁用），若启用则会改为缩短输出以匹配姿态视频的长度。
- `face_video` 会调整为 512x512，并归一化到 -1.0 到 1.0 的范围。
- `continue_motion` 仅限于最后 `continue_motion_max_frames` 帧。使用 `continue_motion` 时，`video_frame_offset` 会减去已使用的帧数，但不会低于 0。
- 输入视频（`face_video`、`pose_video`、`background_video`、`character_mask`）会按 `video_frame_offset` 进行偏移。如果偏移量大于或等于其长度，则忽略该输入；但单帧 `character_mask` 除外，它会始终重复。
- 提供 `clip_vision_output` 时，它会同时应用于正向和负向条件。
- 如果未提供 `reference_image`，则使用黑色图像（全零）作为参考。
- 如果未提供 `continue_motion`，则运动部分使用像素值为 0.5 的灰色帧。
- `width` 和 `height` 使用 16 作为步长；对应的潜空间尺寸为 `width / 8` 和 `height / 8`。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 修改后的正向条件，始终包含拼接后的潜空间图像和拼接后的遮罩。如果提供了 `clip_vision_output`、`pose_video` 或 `face_video`，也会加入它们的值。 | CONDITIONING |
| `negative` | 修改后的负面条件，始终包含拼接后的潜空间图像和拼接后的遮罩。如果提供了 `clip_vision_output`、`pose_video` 或 `face_video`，也会加入它们的值；其中人脸视频像素会被设置为 -1.0。 | CONDITIONING |
| `latent` | 初始化为零的空潜空间张量，形状为 `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`。 | LATENT |
| `trim_latent` | 从开头修剪掉的潜空间帧数，对应于参考图像的潜空间帧。 | INT |
| `trim_image` | 从开头修剪掉的图像帧数，对应于参考运动帧。 | INT |
| `video_frame_offset` | 分块视频生成时更新后的帧偏移，等于调整后的输入偏移加上生成长度。 | INT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
