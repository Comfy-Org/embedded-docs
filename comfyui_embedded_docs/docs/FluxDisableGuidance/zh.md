# Flux禁用指导

此节点完全禁用 Flux 及类 Flux 模型的引导嵌入功能。它接收条件数据作为输入，通过将引导分量设置为 None 来移除该分量，并返回修改后的条件数据，从而在生成过程中有效关闭基于引导的条件控制。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要处理并移除引导分量的条件数据 | CONDITIONING | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `conditioning` | 已禁用引导功能的修改后条件数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/zh.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
