# CLIP文本编码（混元DiT）

`CLIPTextEncodeHunyuanDiT` 节点将文本描述转换为 HunyuanDiT 模型可以理解的格式。它是一个为 HunyuanDiT 双文本编码器架构设计的高级 conditioning 节点，通过不同的分词器处理两个独立的文本输入，并将它们组合成单个 conditioning 输出。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 取值范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于文本分词和编码的 CLIP 模型实例，是生成条件（conditions）的核心。 | CLIP | Yes | - |
| `bert` | 通过 BERT 分词器进行编码的文本输入。优先使用短语和关键词。支持多行和动态提示。 | STRING | Yes | - |
| `mt5xl` | 通过 mT5-XL 分词器进行编码的文本输入。支持多行和动态提示（多语言）。可以使用完整句子和复杂描述。 | STRING | Yes | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 编码后的 conditioning 输出，结合了 BERT 和 mT5-XL 分词后的文本，用于生成任务中的进一步处理。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/zh.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
