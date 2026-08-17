# 保存Checkpoint（仅图像）

ImageOnlyCheckpointSave 节点保存包含模型、CLIP 视觉编码器和 VAE 的检查点文件。它使用指定的文件名前缀创建 safetensors 文件，并将其存储在输出目录中。此节点专门用于将图像相关的模型组件一起保存在单个检查点文件中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要保存在检查点中的模型 | MODEL | 是 | - |
| `clip_vision` | 要保存在检查点中的 CLIP 视觉编码器 | CLIP_VISION | 是 | - |
| `vae` | 要保存在检查点中的 VAE（变分自编码器） | VAE | 是 | - |
| `filename_prefix` | 输出文件名的前缀（默认："checkpoints/ComfyUI"） | STRING | 是 | - |
| `prompt` | 隐藏参数，用于工作流提示数据 | PROMPT | 否 | - |
| `extra_pnginfo` | 隐藏参数，用于额外的 PNG 元数据 | EXTRA_PNGINFO | 否 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| - | 此节点不返回任何输出 | - |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/zh.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
