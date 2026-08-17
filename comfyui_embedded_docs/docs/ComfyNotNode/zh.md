# 非

Not 节点对任何输入值执行逻辑非（NOT）运算。如果输入值被视为假值（例如 0、空字符串、None 或 False），则返回 True；如果输入值为真值，则返回 False。该节点使用 Python 的标准规则来确定真值。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `value` | 需要进行逻辑取反的输入值。接受任意数据类型，并使用 Python 的真值规则进行求值。 | ANY | 是 | 任意值 |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 输入值的逻辑反值。如果输入为假值则返回 True，如果输入为真值则返回 False。 | BOOLEAN |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/zh.md)

---
**Source fingerprint (SHA-256):** `24bbe667a0800b187d991b24894794e2ce710256200a2667ff391c1e644963a5`
