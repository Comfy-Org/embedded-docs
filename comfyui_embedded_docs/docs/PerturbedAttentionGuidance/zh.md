# PAG注意力引导

PerturbedAttentionGuidance 节点对扩散模型应用扰动注意力引导，以提升生成质量。它在采样过程中将模型的自注意力机制替换为简化版本，该版本专注于值投影。通过调整条件去噪过程，该技术有助于提高生成图像的连贯性和质量。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用扰动注意力引导的扩散模型。 | MODEL | 是 | - |
| `scale` | 扰动注意力引导效果的强度（默认值：3.0）。当设置为 0 时，该节点无效并返回原始去噪结果。 | FLOAT | 是 | 0.0 - 100.0 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用扰动注意力引导的修改后模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/zh.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
