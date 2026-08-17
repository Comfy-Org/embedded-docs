# 制作训练数据集

此节点通过编码图像和文本来准备训练数据。它接收一个图像列表和一个对应的文本描述列表，然后使用 VAE 模型将图像转换为潜在表示，并使用 CLIP 模型将文本转换为 conditioning 数据。生成的成对潜在变量和 conditioning 数据以列表形式输出，可直接用于训练工作流。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `images` | 要编码的图像列表。 | IMAGE | 是 | N/A |
| `vae` | 用于将图像编码为潜在表示的 VAE 模型。 | VAE | 是 | N/A |
| `clip` | 用于将文本编码为 conditioning 的 CLIP 模型。 | CLIP | 是 | N/A |
| `texts` | 文本描述列表。长度可为 n（与图像匹配）、1（对所有图像重复），或省略（使用空字符串）。 | STRING | 否 | N/A |

**参数约束：**

* `texts` 列表中的项目数必须为 0、1 或与 `images` 列表中的项目数完全匹配。如果为 0，则对所有图像使用空字符串。如果为 1，则对所有图像重复该单个文本。如果数量为其他任何值，节点将引发错误。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latents` | 潜在字典列表。 | LATENT |
| `conditioning` | conditioning 列表的列表。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/zh.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
