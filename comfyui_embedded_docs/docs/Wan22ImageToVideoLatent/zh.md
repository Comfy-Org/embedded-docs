# Wan22图像转视频潜变量

Wan22ImageToVideoLatent 节点用于准备 Wan 2.2 视频生成所需的 latent 输入。它会创建一个具有指定宽度、高度和帧数的空视频 latent，并在提供起始图像时，将该图像编码到 latent 的前几帧中。该节点还会输出一个噪声掩码，用于标记哪些帧已被图像填充、哪些帧仍需要生成。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `vae` | 用于将起始图像编码到 latent 空间的 VAE 模型 | VAE | 是 | - |
| `width` | 输出视频的宽度（像素）（默认值：1280，步长：32） | INT | 是 | 32 to MAX_RESOLUTION |
| `height` | 输出视频的高度（像素）（默认值：704，步长：32） | INT | 是 | 32 to MAX_RESOLUTION |
| `length` | 视频的帧数（默认值：49，步长：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 并行生成的视频 latent 数量（默认值：1） | INT | 是 | 1 to 4096 |
| `start_image` | 可选图像或图像序列，将放入视频 latent 的前几帧。仅使用前 `length` 帧。图像在由 VAE 编码前，会通过双线性重采样和中心裁剪调整到 `width` × `height` 大小。 | IMAGE | 否 | - |

**注意：** latent 的空间维度为 `width / 16` 和 `height / 16`，因此 `width` 和 `height` 必须能被 16 整除。latent 的时间维度计算公式为 `((length - 1) // 4) + 1`，并且有 48 个通道。当提供了 `start_image` 时，编码后的图像会填充 latent 的前几帧，且 `noise_mask` 对这些帧设为 0，对其余帧设为 1，这告诉采样器保持图像帧不变并生成其余帧。当未提供 `start_image` 时，latent 用零填充，并且不包含噪声掩码。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 生成的视频 latent，重复 `batch_size` 次。当提供了 `start_image` 时，它还包含一个 `noise_mask`，用于标记已由图像编码的帧（0）和需要生成的帧（1）。 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/zh.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
