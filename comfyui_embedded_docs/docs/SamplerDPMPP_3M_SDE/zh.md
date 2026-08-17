# DPMPP_3M_SDE采样器

SamplerDPMPP_3M_SDE 节点创建一个用于采样过程的 DPM++ 3M SDE 采样器。该采样器采用三阶多步随机微分方程方法，并支持可配置的噪声参数。此节点允许您选择在 GPU 还是 CPU 上执行噪声计算。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `eta` | 控制采样过程的随机性（默认值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制采样过程中添加的噪声量（默认值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `noise_device` | 选择用于噪声计算的设备，可以是 GPU 或 CPU（默认值："gpu"） | COMBO | 是 | "gpu"<br>"cpu" |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sampler` | 返回一个配置好的采样器对象，用于采样工作流 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/zh.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
