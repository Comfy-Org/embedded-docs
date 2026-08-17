# 采样算法（Stable Cascade）

The ModelSamplingStableCascade node applies stable cascade sampling to a model by adjusting the sampling parameters with a shift value. It creates a modified clone of the input model with a custom sampling configuration for stable cascade generation.

ModelSamplingStableCascade 节点通过使用 shift 值调整采样参数，对模型应用稳定级联采样。它会创建一个输入模型的修改克隆，并为稳定级联生成配置自定义采样设置。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用稳定级联采样的输入模型 | MODEL | 是 | - |
| `shift` | 应用于采样参数的偏移值（默认：2.0） | FLOAT | 是 | 0.0 - 100.0（步长：0.01） |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用稳定级联采样的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
