# 参考Latent

此节点为编辑模型设置引导潜在变量。它接收条件数据和可选的潜在输入，然后修改条件以包含参考潜在信息。如果模型支持，您可以链式连接多个 ReferenceLatent 节点以设置多个参考图像。

## 输入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `conditioning` | 要使用参考潜在信息修改的条件数据 | CONDITIONING | Yes | - |
| `latent` | 可选的潜在数据，用作编辑模型的参考 | LATENT | No | - |

## 输出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | 包含参考潜在信息的修改后条件数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
