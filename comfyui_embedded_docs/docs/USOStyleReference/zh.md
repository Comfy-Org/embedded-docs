# USO风格参考

USOStyleReference 节点将参考图像中的风格信息应用到 Flux 模型。它从 CLIP 视觉输出构建风格嵌入，然后修补模型的克隆，以便在生成过程中，风格嵌入被插入到文本提示条件之前。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用风格参考修补的基础模型 | MODEL | 是 | - |
| `model_patch` | 包含风格参考信息的模型修补 | MODEL_PATCH | 是 | - |
| `clip_vision_output` | 从 CLIP 视觉处理中提取的编码视觉特征。该节点将来自第 -20 层和第 -11 层的隐藏状态与倒数第二层的隐藏状态组合在一起，以构建风格嵌入 | CLIP_VISION_OUTPUT | 是 | - |

注意：所有三个输入都是必需的。此节点标记为实验性。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用风格参考修补的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/zh.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
