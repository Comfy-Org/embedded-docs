# CLIP文本编码（Lumina2）

The CLIP Text Encode for Lumina2 node encodes a system prompt and a user prompt using a CLIP model into an embedding that can guide the diffusion model to generate specific images. It combines a pre-defined system prompt with your custom text prompt and processes them through the CLIP model to create conditioning data for image generation.

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 取值范围 |
| --- | --- | --- | --- | --- |
| `system_prompt` | Lumina2 提供两种系统提示词："superior" 生成具有卓越图像-文本对齐效果的图像；"alignment" 生成具有最高图像-文本对齐度的高质量图像。 | COMBO | 是 | `"superior"`<br>`"alignment"` |
| `user_prompt` | 要编码的文本。支持多行输入和动态提示词。 | STRING | 是 | N/A |
| `clip` | 用于编码文本的 CLIP 模型。 | CLIP | 是 | N/A |

**注意：** `clip` 输入是必填项，不能为 None。如果 clip 输入无效，节点将引发错误，提示检查点可能不包含有效的 CLIP 或文本编码器模型。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 包含嵌入文本的条件数据，用于引导扩散模型生成图像。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/zh.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
