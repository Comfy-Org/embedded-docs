# 调整亮度

调整亮度节点用于修改输入图像的亮度。它通过将每个像素值乘以指定因子，然后将结果值限制在有效范围内来实现。因子为 1.0 时图像不变，低于 1.0 时变暗，高于 1.0 时变亮。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `image` | 要调整的输入图像。 | IMAGE | 是 | - |
| `factor` | 亮度因子。1.0 = 不变，<1.0 = 变暗，>1.0 = 变亮。（默认值：1.0） | FLOAT | 否 | 0.0 - 2.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `image` | 调整亮度后的输出图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/zh.md)

---
**Source fingerprint (SHA-256):** `696fb3c0bfc8edccc2049dad8f44b4b056fe1caa95b0cc0126164269cb65ab1a`
