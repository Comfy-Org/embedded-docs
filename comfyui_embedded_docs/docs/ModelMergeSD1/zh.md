# 模型融合（SD1）

ModelMergeSD1 允许您通过调整两个 Stable Diffusion 1.x 模型各组件的权重来将它们混合在一起。它为时间嵌入、标签嵌入、每个输入块、每个中间块、每个输出块以及最终输出层提供了单独的混合权重，从而可以精细控制两个模型的组合方式。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model1` | 要合并的第一个模型 | MODEL | 是 | - |
| `model2` | 要合并的第二个模型 | MODEL | 是 | - |
| `time_embed.` | 时间嵌入层混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `label_emb.` | 标签嵌入层混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.0.` | 输入块 0 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.1.` | 输入块 1 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.2.` | 输入块 2 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.3.` | 输入块 3 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.4.` | 输入块 4 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.5.` | 输入块 5 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.6.` | 输入块 6 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.7.` | 输入块 7 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.8.` | 输入块 8 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.9.` | 输入块 9 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.10.` | 输入块 10 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.11.` | 输入块 11 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.0.` | 中间块 0 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.1.` | 中间块 1 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.2.` | 中间块 2 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.0.` | 输出块 0 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.1.` | 输出块 1 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.2.` | 输出块 2 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.3.` | 输出块 3 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.4.` | 输出块 4 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.5.` | 输出块 5 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.6.` | 输出块 6 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.7.` | 输出块 7 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.8.` | 输出块 8 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.9.` | 输出块 9 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.10.` | 输出块 10 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.11.` | 输出块 11 混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `out.` | 输出层混合权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `MODEL` | 合并后的模型，融合了两个输入模型的特征 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/zh.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
