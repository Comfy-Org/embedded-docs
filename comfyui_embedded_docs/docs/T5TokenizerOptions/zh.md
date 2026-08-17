# T5Tokenizer设置

T5TokenizerOptions 节点允许您为各种 T5 模型类型配置分词器设置。它为多种 T5 模型变体（包括 t5xxl、pile_t5xl、t5base、mt5xl 和 umt5xxl）设置最小填充和最小长度参数。该节点接收 CLIP 输入，并返回应用了指定分词器选项的修改后 CLIP。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 要为其配置分词器选项的 CLIP 模型 | CLIP | 是 | - |
| `min_padding` | 要为所有 T5 模型类型设置的最小填充值（默认值：0） | INT | 否 | 0 to 10000 |
| `min_length` | 要为所有 T5 模型类型设置的最小长度值（默认值：0） | INT | 否 | 0 to 10000 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 已将更新的分词器选项应用于所有 T5 变体的修改后 CLIP 模型 | CLIP |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/zh.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
