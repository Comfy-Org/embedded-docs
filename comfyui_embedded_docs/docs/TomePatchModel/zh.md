# Tome合并模型Token

TomePatchModel 节点对扩散模型应用 Token Merging (ToMe) 技术，以降低推理过程中的计算需求。其工作原理是在注意力机制中选择性地合并相似的 token，让模型在保持图像质量的同时处理更少的 token。该技术有助于在质量损失不明显的情况下加速生成过程。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用 token 合并的扩散模型 | MODEL | 是 | - |
| `ratio` | 要合并的 token 比例（默认值：0.3，步长：0.01）。数值越大，合并的 token 越多，加速效果越明显，但质量可能会降低。 | FLOAT | 是 | 0.0 - 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用 token 合并后的修改模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/zh.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
