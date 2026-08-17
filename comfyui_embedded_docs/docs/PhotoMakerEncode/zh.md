# PhotoMaker编码

PhotoMakerEncode 通过将参考图像与文本提示相结合，为 AI 图像生成创建 conditioning 数据。它会搜索文本提示中的 "photomaker" 一词，当找到时，使用 PhotoMaker 模型在该提示位置应用参考图像的视觉特征。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `photomaker` | 用于处理参考图像并生成基于图像的 embedding 的 PhotoMaker 模型 | PHOTOMAKER | 是 | - |
| `image` | 为 conditioning 提供视觉特征的参考图像 | IMAGE | 是 | - |
| `clip` | 用于文本分词和编码的 CLIP 模型 | CLIP | 是 | - |
| `text` | 用于生成 conditioning 的文本提示。支持多行文本和动态提示（默认值："photograph of photomaker"） | STRING | 是 | - |

**注意：** 文本提示中必须将 "photomaker" 作为独立单词出现（匹配区分大小写），才会应用基于图像的 conditioning。如果存在该词，图像特征会在提示中的该位置被注入。如果未找到 "photomaker"，节点将返回不包含图像影响的标准文本 conditioning。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 包含图像和文本 embedding 的 conditioning 数据，用于引导图像生成，以及来自 CLIP 文本编码器的池化输出 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/zh.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
