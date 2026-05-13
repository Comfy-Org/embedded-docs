> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/zh.md)

## 概述

StringCompare节点使用不同的比较方法来比较两个文本字符串。它可以检查一个字符串是否以另一个字符串开头、结尾，或者两个字符串是否完全相等。比较时可以区分或忽略字母大小写。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | 是 | - | 要比较的第一个字符串 |
| `string_b` | STRING | 是 | - | 用于比较的第二个字符串 |
| `mode` | COMBO | 是 | "Starts With"<br>"Ends With"<br>"Equal" | 使用的比较方法（默认值："Starts With"） |
| `case_sensitive` | BOOLEAN | 否 | - | 比较时是否区分字母大小写（默认值：true） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | BOOLEAN | 如果满足比较条件则返回true，否则返回false |

---
**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`
