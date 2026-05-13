> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/zh.md)

替换文本节点执行简单的文本替换操作。它会在输入文本中搜索指定的文本片段，并将每次出现的内容替换为新的文本片段。该操作将应用于提供给节点的所有文本输入。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | 是 | - | 要处理的文本。 |
| `find` | STRING | 是 | - | 要查找的文本（默认：空字符串）。 |
| `replace` | STRING | 是 | - | 要替换的文本（默认：空字符串）。 |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `text` | STRING | 处理后的文本，其中所有 `find` 文本的出现位置均被替换为 `replace` 文本。 |

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`
