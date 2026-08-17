# FluxKontext多参考潜在方法

FluxKontextMultiReferenceLatentMethod 节点通过设置特定的 reference latents 方法来修改 conditioning 数据。它将所选方法附加到 conditioning 输入中，从而影响后续生成步骤中 reference latents 的处理方式。此节点标记为实验性，属于 Flux conditioning 系统的一部分。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要使用 reference latents 方法进行修改的 conditioning 数据 | CONDITIONING | 是 | - |
| `reference_latents_method` | 用于 reference latents 处理的方法。如果选择 "uxo" 或 "uso"，将转换为 "uxo"。此参数标记为高级。 | COMBO | 是 | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `conditioning` | 已应用 reference latents 方法的修改后 conditioning 数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/zh.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
