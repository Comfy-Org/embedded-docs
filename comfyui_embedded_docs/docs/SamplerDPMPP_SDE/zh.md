# DPMPP_SDE采样器

SamplerDPMPP_SDE 节点创建一个 DPM++ SDE（随机微分方程）采样器，用于采样过程。该采样器提供一种具有可配置噪声参数和设备选择的随机采样方法。它返回一个采样器对象，可用于采样流程中。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `eta` | 控制采样过程中的随机性（默认值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制采样过程中添加的噪声量（默认值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `r` | 影响采样行为的参数（默认值：0.5） | FLOAT | 是 | 0.0 - 100.0 |
| `noise_device` | 选择执行噪声计算的设备（默认值："gpu"）。当设置为 "cpu" 时，使用标准 `dpmpp_sde` 采样器；当设置为 "gpu" 时，使用 `dpmpp_sde_gpu` 采样器。 | COMBO | 是 | "gpu"<br>"cpu" |

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `sampler` | 返回一个已配置的 DPM++ SDE 采样器对象，用于采样流程中 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/zh.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
