# 自定义采样器（高级）

The SamplerCustomAdvanced node performs advanced latent space sampling using custom noise, guidance, and sampling configurations. It processes a latent image through a guided sampling process with customizable noise generation and sigma schedules, producing both the final sampled output and a denoised version when available.

SamplerCustomAdvanced 节点使用自定义噪声、引导和采样配置执行高级潜在空间采样。它通过可自定义的噪声生成和 sigma 调度，对潜在图像执行引导式采样过程，在可用时同时生成最终的采样输出和去噪版本。

## Inputs

## 输入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `noise` | The noise generator that provides the initial noise pattern and seed for the sampling process | NOISE | Yes | - |
| `guider` | The guidance model that directs the sampling process toward desired outputs | GUIDER | Yes | - |
| `sampler` | The sampling algorithm that defines how the latent space is traversed during generation | SAMPLER | Yes | - |
| `sigmas` | The sigma schedule that controls the noise levels throughout the sampling steps | SIGMAS | Yes | - |
| `latent_image` | The initial latent representation that serves as the starting point for sampling. Supports optional `noise_mask` for selective denoising, and optional `downscale_ratio_spacial` and `downscale_ratio_temporal` keys for advanced latent handling | LATENT | Yes | - |

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `noise` | 为采样过程提供初始噪声模式和种子的噪声生成器 | NOISE | 是 | - |
| `guider` | 引导采样过程朝向期望输出的引导模型 | GUIDER | 是 | - |
| `sampler` | 定义生成过程中潜在空间遍历方式的采样算法 | SAMPLER | 是 | - |
| `sigmas` | 控制整个采样步骤中噪声水平的 sigma 调度 | SIGMAS | 是 | - |
| `latent_image` | 作为采样起点的初始潜在表示。支持可选的 `noise_mask` 用于选择性去噪，以及可选的 `downscale_ratio_spacial` 和 `downscale_ratio_temporal` 键用于高级潜在处理 | LATENT | 是 | - |

## Outputs

## 输出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | The final sampled latent representation after completing the sampling process. Any `downscale_ratio_spacial` or `downscale_ratio_temporal` keys from the input latent are removed from this output | LATENT |
| `denoised_output` | A denoised version of the output when the sampling process produces an intermediate clean prediction (x0), otherwise returns the same as the output. When available, this represents the model's best estimate of the clean latent at each step | LATENT |

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 采样过程完成后最终得到的采样潜在表示。输入潜在中的任何 `downscale_ratio_spacial` 或 `downscale_ratio_temporal` 键都会从该输出中移除 | LATENT |
| `denoised_output` | 当采样过程产生中间干净预测（x0）时，该输出去噪版本的潜在表示；否则与 `output` 相同。在可用时，它表示模型在每一步对干净潜在的最佳估计 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/zh.md)

---
**Source fingerprint (SHA-256):** `23cffad0f7cf74dcd494c2828b2116bb4d00a1e55e42ded074b587ac20183290`
