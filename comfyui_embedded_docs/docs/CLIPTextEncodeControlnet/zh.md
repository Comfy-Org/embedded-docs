# CLIP文本编码(ControlNet)

CLIPTextEncodeControlnet 节点使用 CLIP 模型处理文本输入，并将其与现有条件数据结合，为 controlnet 应用生成增强的条件输出。它对输入文本进行分词，通过 CLIP 模型进行编码，并将生成的嵌入作为交叉注意力 controlnet 参数添加到提供的条件数据中。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `clip` | 用于文本分词和编码的 CLIP 模型 | CLIP | 是 | - |
| `conditioning` | 现有条件数据，将使用 controlnet 参数进行增强 | CONDITIONING | 是 | - |
| `text` | 由 CLIP 模型处理的文本输入。支持多行文本和动态提示 | STRING | 是 | - |

**注意：** 此节点需要所有三个输入（`clip`、`conditioning` 和 `text`）才能正常运行。`text` 输入支持动态提示和多行文本，以便灵活处理文本。此节点被标记为实验性。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 增强的条件数据，包含来自 CLIP 文本编码的附加 controlnet 交叉注意力参数（`cross_attn_controlnet` 和 `pooled_output_controlnet`） | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/zh.md)

---
**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`
