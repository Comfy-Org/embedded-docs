# 预览遮罩

MaskPreview 节点直接在 ComfyUI 界面中显示蒙版数据的可视化预览，以便您在工作流中检查蒙版。它显示预览而不将其保存到 ComfyUI 输出目录，并将蒙版原样传递作为输出。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mask` | 要预览的蒙版数据 | MASK | 是 | - |
| `filename_prefix` | 输出文件名的前缀（默认："ComfyUI"） | STRING | 否 | - |
| `prompt` | 用于元数据的提示信息（自动提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 用于元数据的额外 PNG 信息（自动提供） | EXTRA_PNGINFO | 否 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `mask` | 已预览的蒙版数据，原样传递 | MASK |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/zh.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
