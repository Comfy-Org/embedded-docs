# 三重CLIP加载器

TripleCLIPLoader 节点会同时加载三个文本编码器模型，并将它们组合成一个单一的 CLIP 模型。这对于需要多个文本编码器的高级文本编码场景非常有用，例如在需要 clip-l、clip-g 和 t5 模型协同工作的 SD3 工作流中。

## 输入
| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | 从可用文本编码器中加载的第一个文本编码器模型 | COMBO | Yes | text_encoders 文件夹中的所有文本编码器文件 |
| `clip_name2` | 从可用文本编码器中加载的第二个文本编码器模型 | COMBO | Yes | text_encoders 文件夹中的所有文本编码器文件 |
| `clip_name3` | 从可用文本编码器中加载的第三个文本编码器模型 | COMBO | Yes | text_encoders 文件夹中的所有文本编码器文件 |

**注意：** 所有三个文本编码器参数都必须从系统中的可用文本编码器模型中选择。节点按给定顺序加载全部三个模型，并将它们组合成一个单一的 CLIP 模型进行处理。对于 SD3 工作流，请使用 clip-l、clip-g 和 t5 作为三个编码器。

## 输出
| Output Name | Description | Data Type |
|-----------|-------------|-----------|
| `CLIP` | 包含所有三个已加载文本编码器的组合 CLIP 模型 | CLIP |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/zh.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
