> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoise/zh.md)

# 概述

为 VOID 视频优化流程的第二轮生成时间相关性噪声。它接收第一轮的输出视频，并沿光流矢量扭曲高斯噪声，生成与视频内容一致移动的噪声。此扭曲噪声用作第二轮的初始潜空间，从而改善最终输出的时间一致性。

# 输入

| 参数 | 数据类型 | 必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `optical_flow` | MODEL | 是 | - | 来自 OpticalFlowLoader（RAFT-large）的光流模型。 |
| `video` | IMAGE | 是 | - | 第一轮输出视频帧 [T, H, W, 3]。 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION（步长 8） | 输出潜空间的宽度（默认值：672）。 |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION（步长 8） | 输出潜空间的高度（默认值：384）。 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION（步长 1） | 像素帧数。向下取整以使 latent_t 为偶数（patch_size_t=2 要求），例如 49 → 45（默认值：45）。 |
| `batch_size` | INT | 是 | 1 至 64 | 要生成的相同噪声序列数量（默认值：1）。 |

**关于 `length` 参数的说明：** `length` 值会自动向下取整到最接近的有效值，该值能产生偶数 `latent_t` 维度。这是 CogVideoX-Fun-V1.5 模型的 `patch_size_t=2` 约束所要求的。当发生取整时，会记录一条警告信息。

# 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `warped_noise` | LATENT | 一个 5D 张量 (B, C, T, H, W)，包含经光流扭曲的高斯噪声，可直接用作 VOID 第二轮的初始潜空间。 |