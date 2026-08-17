# LTXV添加指导

LTXVAddGuide 通过将输入图像或视频编码为关键帧并嵌入条件数据，为潜在序列添加视频条件引导。该节点使用 VAE 编码器处理输入，并将生成的潜在表示策略性地放置在指定的帧位置，同时使用关键帧信息更新正向和负向条件。该节点处理帧对齐约束，并允许控制条件影响的强度。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 待添加关键帧引导的正向条件输入 | CONDITIONING | 是 | - |
| `negative` | 待添加关键帧引导的负向条件输入 | CONDITIONING | 是 | - |
| `vae` | 用于编码输入图像/视频帧的 VAE 模型 | VAE | 是 | - |
| `latent` | 将接收条件帧的输入潜在序列 | LATENT | 是 | - |
| `image` | 用于对潜在视频进行条件处理的图像或视频。帧数必须为 8*n + 1。如果视频帧数不符合 8*n + 1，将自动裁剪至最接近的 8*n + 1 帧。 | IMAGE | 是 | - |
| `frame_idx` | 开始条件处理的帧索引。对于单帧图像或 1-8 帧的视频，任何 `frame_idx` 值均可接受。对于 9 帧及以上的视频，`frame_idx` 必须能被 8 整除，否则将向下取整至最接近的 8 的倍数。负值从视频末尾开始计数。（默认值：0） | INT | 否 | -9999 至 9999 |
| `strength` | 条件影响强度，1.0 表示完全应用条件，0.0 表示不应用条件（默认值：1.0） | FLOAT | 否 | 0.0 至 10.0 |
| `attention_mask` | 可选的像素空间空间掩码。通过自注意力控制每个区域的条件影响，并与 `strength` 相乘。 | MASK | 否 | - |
| `iclora_parameters` | 可选的 IC-LoRA 参数，来自“获取 IC-LoRA 参数”节点。用于根据特定 IC-LoRA 的要求调整引导处理（例如，具有 `reference_downscale_factor` > 1 的 IC-LoRA）。当链式使用时，每个 LTXVAddGuide 仅使用连接到自身的参数。 | IC_LORA_PARAMETERS | 否 | - |

**注释：**

- 输入图像/视频的帧数必须符合 8*n + 1 模式（例如 1、9、17、25 帧）。如果输入帧数超出该模式，将自动裁剪至最接近的有效帧数。
- 当使用 `reference_downscale_factor` 大于 1 的 IC-LoRA 参数时，潜在空间维度（宽度和高度）必须能被该因子整除。如果条件不满足，节点将引发错误。
- 引导必须能放入潜在序列中：起始帧索引加上引导帧数不能超过潜在长度，否则节点将引发错误。
- 该节点不支持音频-视频组合的潜在表示。输入的 `latent` 和编码后的引导都必须使用标准的 128 通道视频潜在格式，否则节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已使用关键帧引导信息更新的正向条件 | CONDITIONING |
| `negative` | 已使用关键帧引导信息更新的负向条件 | CONDITIONING |
| `latent` | 已并入条件帧并更新噪声掩码的潜在序列 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/zh.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`
