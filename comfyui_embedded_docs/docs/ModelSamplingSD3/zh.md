# 采样算法（SD3）

此节点将 Stable Diffusion 3 风格的采样设置应用到模型上。它会复制该模型，并用基于流的采样配置替换其采样方法，该配置使用给定的 `shift` 值，而 `shift` 值用于控制采样分布的形状。

## 输入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `模型` | 要应用 SD3 采样参数的输入模型 | MODEL | 是 | - |
| `移位` | 控制采样偏移参数（默认值：3.0） | FLOAT | 是 | 0.0 - 100.0 (step: 0.01) |

注意：`shift` 值会与固定的内部乘数 1000 一起应用。如果原始模型带有噪声缩放（noise scale）设置，该值会沿用到修改后的模型中。原始模型不会被改变；返回的是克隆并修补后的副本。

## 输出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | 应用了 SD3 采样参数的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
