# CLIP文本编码（PixArtAlpha）

此节点用于编码文本并为 PixArt Alpha 设置分辨率条件控制。它会处理文本输入，并附加宽度和高度信息，以生成专用于 PixArt Alpha 模型的条件控制数据。此节点不适用于 PixArt Sigma 模型。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `width` | 分辨率条件控制的宽度尺寸（默认值：1024） | INT | 是 | 0 至 MAX_RESOLUTION |
| `height` | 分辨率条件控制的高度尺寸（默认值：1024） | INT | 是 | 0 至 MAX_RESOLUTION |
| `text` | 要编码的文本输入，支持多行输入和动态提示 | STRING | 是 | - |
| `clip` | 用于分词和编码的 CLIP 模型 | CLIP | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 包含文本令牌和分辨率信息的编码条件控制数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/zh.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
