# 保存 LoRA

SaveLoRA 节点将 LoRA（低秩自适应）模型保存到文件中。它将以 `.safetensors` 格式将 LoRA 模型写入输出目录。你可以指定文件名前缀和可选的步数；提供步数后，步数会包含在保存的文件名中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `lora` | 要保存的 LoRA 模型。请勿使用带有 LoRA 层的模型。 | LORA_MODEL | 是 | N/A |
| `prefix` | 用于保存的 LoRA 文件的前缀（默认："loras/ComfyUI_trained_lora"）。 | STRING | 是 | N/A |
| `steps` | 可选：LoRA 已训练步数，用于命名保存的文件。 | INT | 否 | N/A |

**注意：** `lora` 输入必须是纯 LoRA 模型。请勿提供已应用 LoRA 层的基础模型。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| *None* | 此节点不会向工作流输出任何数据。它是一个输出节点，将文件保存到磁盘。 | N/A |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/zh.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
