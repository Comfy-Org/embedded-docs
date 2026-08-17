# 文本编码（Hunyuan视频_图像到视频）

TextEncodeHunyuanVideo_ImageToVideo 节点通过将文本提示与图像嵌入相结合，为视频生成创建条件数据。它使用 CLIP 模型处理文本输入和来自 CLIP 视觉输出的视觉信息，然后根据指定的图像交错（image interleave）设置生成融合这两种来源的令牌。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于分词和编码的 CLIP 模型 | CLIP | 是 | - |
| `clip_vision_output` | 来自 CLIP 视觉模型的视觉嵌入，提供图像上下文 | CLIP_VISION_OUTPUT | 是 | - |
| `prompt` | 用于指导视频生成的文本描述。支持多行输入和动态提示。提示词使用一个模板进行格式化，该模板要求模型基于参考图像描述视频，涵盖主要内容、物体细节、动作、背景和镜头角度等方面。 | STRING | 是 | - |
| `image_interleave` | 图像相对于文本提示的影响程度。数值越高表示文本提示的影响越大。（默认值：2，高级参数） | INT | 是 | 1-512 |

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 结合文本和图像信息用于视频生成的条件数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/zh.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
