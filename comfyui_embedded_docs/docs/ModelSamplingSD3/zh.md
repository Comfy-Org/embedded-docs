# 采样算法（SD3）

ModelSamplingSD3 节点将 Stable Diffusion 3 采样参数应用于模型。它通过调整 `shift` 参数来修改模型的采样行为，该参数控制采样分布特征。该节点会创建输入模型的修改副本，并应用指定的采样配置。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用 SD3 采样参数的输入模型 | MODEL | 是 | - |
| `shift` | 控制采样偏移参数（默认值：3.0） | FLOAT | 是 | 0.0 - 100.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了 SD3 采样参数的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
