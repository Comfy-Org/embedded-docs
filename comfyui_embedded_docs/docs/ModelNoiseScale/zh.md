# 模型噪声尺度

此节点调整模型采样过程中使用的噪声尺度。它允许您设置特定的噪声尺度值，该值控制应用于模型采样过程的噪声量。该节点会克隆模型，并使用新的噪声尺度更新其采样配置，同时保留现有的偏移和乘数设置。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用噪声尺度调整的模型。 | MODEL | 是 | - |
| `noise_scale` | 绝对训练噪声尺度。例如 HiDream-O1 base：8.0，dev：7.5。（默认：1.0） | FLOAT | 是 | 0.0 至 64.0（步长：0.01） |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `MODEL` | 应用了新噪声尺度后的修改模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/zh.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
