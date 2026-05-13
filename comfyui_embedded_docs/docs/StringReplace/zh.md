> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/zh.md)

StringReplace 节点对输入字符串执行文本替换操作。它会在输入文本中搜索指定的子字符串，并将所有匹配项替换为另一个子字符串。此节点返回完成所有替换后的修改字符串。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 是 | - | 将要执行替换操作的输入文本字符串 |
| `find` | STRING | 是 | - | 在输入文本中要搜索的子字符串 |
| `replace` | STRING | 是 | - | 用于替换所有找到匹配项的替换文本 |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | STRING | 已将查找文本的所有匹配项替换为替换文本后的修改字符串 |

---
**Source fingerprint (SHA-256):** `72159dba72261efe9df283c1ea3f789651eade923efdaeb108bacc1d0da663f8`
