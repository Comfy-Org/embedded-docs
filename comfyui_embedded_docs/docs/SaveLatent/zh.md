# 保存Latent

The SaveLatent 节点将潜空间样本以 `.latent` 文件的形式保存到磁盘，以便日后使用或共享。它使用指定的文件名前缀将潜空间张量数据写入输出文件夹，并嵌入可选的元数据，例如提示信息。节点还会将原始潜空间样本原样返回，以便工作流继续使用它们。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 要保存到磁盘的潜空间样本 | LATENT | 是 | - |
| `filename_prefix` | 用于生成输出文件名和子文件夹路径的前缀（默认值："latents/ComfyUI"） | STRING | 是 | - |
| `prompt` | 工作流提示数据，以 JSON 元数据形式存储在保存的文件中（隐藏输入，自动提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 额外的工作流元数据，以 JSON 形式存储在保存的文件中（隐藏输入，自动提供） | EXTRA_PNGINFO | 否 | - |

注意：除非 ComfyUI 以 `--disable-metadata` 参数启动，否则元数据会写入保存的 `.latent` 文件。保存的文件使用 `{filename}_{5位计数器}_.latent` 格式命名，例如 `ComfyUI_00001_.latent`。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `samples` | 原始的潜空间样本，原样返回 | LATENT |
| `ui` | 所保存潜空间文件的文件位置详细信息（文件名、子文件夹和输出类型） | UI |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/zh.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
