# Trellis2Conditioning

Trellis2Conditioning 将输入图像转换为 TRELLIS.2 模型的条件数据。它使用 CLIP 视觉模型将图像编码为两组特征（512 和 1024 尺度），并将其打包为正条件对，同时创建一个匹配的零填充负条件对，作为空参考。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | 用于将图像编码为条件特征的 CLIP 视觉模型。 | CLIP_VISION | 是 | 任何可用的 CLIP 视觉模型 |
| `image` | 来自 ImageCropToMask 的预处理图像（对于 TRELLIS.2，pad_factor=1.0）。 | IMAGE | 是 | 任意图像 |

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `positive` | 包含 512 和 1024 尺度下编码图像特征的条件，用作 TRELLIS.2 模型的正条件。 | CONDITIONING |
| `negative` | 与正条件形状相同的零填充条件，用作空的负参考。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
