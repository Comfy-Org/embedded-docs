# Hunyuan3Dv2条件

Hunyuan3Dv2Conditioning 节点处理 CLIP 视觉输出，为 3D 模型生成条件数据。它从视觉输出中提取最后的隐藏状态嵌入，并创建正负条件对。正条件使用实际嵌入，负条件使用形状相同的零值嵌入。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | 来自 CLIP 视觉模型的输出，包含视觉嵌入 | CLIP_VISION_OUTPUT | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 包含 CLIP 视觉嵌入的正条件数据 | CONDITIONING |
| `negative` | 包含与正嵌入形状相同的零值嵌入的负条件数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
