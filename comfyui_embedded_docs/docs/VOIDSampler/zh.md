# VOIDSampler

## Overview

VOIDSampler 节点提供了一种专为 VOID 修复（inpainting）模型设计的专用 DDIM 采样方法。它实现了 VOID 模型训练期间使用的相同去噪过程，但不包含标准 KSampler 所应用的噪声缩放。此节点旨在与 SamplerCustom 或 SamplerCustomAdvanced 节点配合使用，并应与 RandomNoise 或 VOIDWarpedNoiseSource 搭配使用。

## Inputs

此节点没有可配置的输入参数。它是一个自包含的采样器，应用固定的 DDIM 采样算法。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| *无输入* | 此节点不接受任何输入参数。 | - | - | - |

注意：VOID 模型是使用 diffusers 的 CogVideoXDDIMScheduler 训练的，该调度器在 alpha 空间中运行，其中输入标准差约为 1。标准 KSampler 应用的噪声缩放会乘以约 4500 倍，这与该训练方式不兼容。VOIDSampler 跳过了该缩放，并通过 sigma 到 alpha 的转换直接实现 DDIM 更新规则。

## Outputs

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `SAMPLER` | 一个实现 VOID DDIM 算法的采样器对象，可供连接到 SamplerCustom 或 SamplerCustomAdvanced 节点使用。 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/zh.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
