> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/zh.md)

根据文本提示和原始图像的宽高比同步修改图像。此节点接收输入图像，并根据提供的提示对其进行变换，使用可配置的图像权重来控制原始图像的修改程度。

## 输入

| 参数 | 数据类型 | 是否必填 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 待修改的输入图像 |
| `prompt` | STRING | 是 | - | 图像生成的提示词（默认值：""） |
| `image_weight` | FLOAT | 否 | 0.0-0.98 | 图像权重；数值越接近 1.0，图像修改程度越小（默认值：0.1）。内部会将此值反转（1.0 - image_weight）并限制在 0.0 到 0.98 之间。 |
| `model` | STRING | 是 | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` | 用于图像修改的 Luma 模型。不同模型的成本不同。 |
| `seed` | INT | 否 | 0-18446744073709551615 | 用于确定节点是否应重新运行的种子值；实际结果与种子无关，具有不确定性（默认值：0） |

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 由 Luma 模型生成的修改后图像 |

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
