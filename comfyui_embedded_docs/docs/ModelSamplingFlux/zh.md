# 采样算法（Flux）

The ModelSamplingFlux 节点根据图像尺寸计算 shift 参数，将 Flux 模型采样应用于给定模型。它会创建一种专门的采样配置，根据指定的宽度、高度和 shift 参数调整模型行为，然后返回已应用新采样设置的修改后模型。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用 Flux 采样的模型 | MODEL | 是 | - |
| `max_shift` | 用于采样计算的最大 shift 值（默认值：1.15） | FLOAT | 是 | 0.0 - 100.0 |
| `base_shift` | 用于采样计算的基础 shift 值（默认值：0.5） | FLOAT | 是 | 0.0 - 100.0 |
| `width` | 目标图像的宽度（像素，默认值：1024） | INT | 是 | 16 - MAX_RESOLUTION |
| `height` | 目标图像的高度（像素，默认值：1024） | INT | 是 | 16 - MAX_RESOLUTION |

有效 shift 值根据从 `width` 和 `height` 推导出的 latent 大小，在 `base_shift` 与 `max_shift` 之间进行插值。`max_shift` 和 `base_shift` 的 `step` 值为 0.01，`width` 和 `height` 的 `step` 值为 8。`max_shift` 和 `base_shift` 参数在用户界面中标记为高级选项。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用 Flux 采样配置的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/zh.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
