# 保存WEBM

The SaveWEBM 节点将一系列图像保存为 WEBM 视频文件。它使用 VP9 或 AV1 编解码器，通过可配置的帧率和质量设置将输入图像编码为视频，并将文件保存到输出目录。当可用时，提示词和工作流元数据会嵌入到视频文件中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要编码为视频的图像序列。RGBA 图像会将其 Alpha 通道作为透明度保存（仅限 vp9 编解码器）。 | IMAGE | 是 | - |
| `filename_prefix` | 输出文件名的前缀；计数器和 .webm 扩展名会自动追加（默认值："ComfyUI"） | STRING | 否 | - |
| `codec` | 用于编码的视频编解码器 | COMBO | 是 | "vp9"<br>"av1" |
| `fps` | 输出视频的帧率（默认值：24.0） | FLOAT | 否 | 0.01-1000.0 |
| `crf` | crf 值越高，质量越低且文件越小；crf 值越低，质量越高且文件越大（默认值：32.0） | FLOAT | 否 | 0-63.0 |

**Alpha 通道说明：** RGBA 图像的 Alpha 通道仅在使用 vp9 编解码器时才会保留。使用 av1 编解码器时，Alpha 通道会被忽略，仅编码 RGB 数据。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `images` | 输入图像序列，原样传递 | IMAGE |
| `ui` | 显示已保存 WEBM 文件的视频预览 | PREVIEW |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/zh.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
