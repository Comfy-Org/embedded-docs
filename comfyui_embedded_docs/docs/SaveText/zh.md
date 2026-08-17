# 保存文本

Save Text 节点用于将文本内容写入输出目录中的文件。它支持以 .txt、.csv、.md 或 .json 格式保存，并且在提供有效 JSON 时会自动进行美观打印。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要保存到文件的文本内容。此输入必须从另一个节点连接。 | STRING | 是 | - |
| `filename_prefix` | 输出文件名的前缀。会追加一个 5 位计数器以防止覆盖现有文件（默认值："ComfyUI"）。 | STRING | 否 | - |
| `format` | 保存文本的文件格式（默认值："txt"）。当选择 "json" 时，有效的 JSON 文本会以 2 个空格缩进进行美观打印；否则，文本将按原样保存。 | COMBO | 否 | `"txt"`<br>`"csv"`<br>`"md"`<br>`"json"` |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `text` | 已保存到文件的原始文本内容 | STRING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/zh.md)

---
**Source fingerprint (SHA-256):** `09bd896cab770358132834892c1b37efd2ffa0cb0aa7b02b7ef91163331dc9b1`
