# SamplerLCM

SamplerLCM 节点提供了一个 LCM（潜在一致性模型）采样器，具有可调的分步噪声设置。`s_noise` 参数作为模型训练噪声尺度的乘数，允许对每个采样步骤应用的噪声进行细粒度控制。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `s_noise` | 第一步的分步噪声乘数（1.0 = 匹配训练）。默认值：1.0。 | FLOAT | 是 | 0.0 to 64.0 (step: 0.01) |
| `s_noise_end` | 最后一步的分步噪声乘数。设置为与 `s_noise` 相等可获得恒定调度。默认值：1.0。 | FLOAT | 是 | 0.0 to 64.0 (step: 0.01) |
| `noise_clip_std` | 将分步噪声限制在 ±N*标准差 范围内。0 表示禁用。默认值：0.0。 | FLOAT | 是 | 0.0 to 10.0 (step: 0.01) |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `SAMPLER` | 配置好的 LCM 采样器对象，可直接用于采样工作流。 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/zh.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
