CLIPSubtract 节点对两个 CLIP 模型执行减法运算。它以第一个 CLIP 模型为基础，减去第二个 CLIP 模型的关键补丁，并可通过可选的乘数控制减法强度。这使得能够通过使用一个模型去除另一个模型的特定特征来实现精细的模型混合。

## 输入

| 参数 | 描述 | 数据类型 | 输入类型 | 默认值 | 范围 |
| --- | --- | --- | --- | --- | --- |
| `clip1` | 将被修改的基础 CLIP 模型 | CLIP | 必需 | - | - |
| `clip2` | 其关键补丁将从基础模型中减去的 CLIP 模型 | CLIP | 必需 | - | - |
| `multiplier` | 控制减法运算的强度。正值从 clip2 中减去特征，负值则添加特征。 | FLOAT | 必需 | 1.0 | -10.0 到 10.0，步长 0.01 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CLIP` | 减法运算后得到的 CLIP 模型 | CLIP |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/zh.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
