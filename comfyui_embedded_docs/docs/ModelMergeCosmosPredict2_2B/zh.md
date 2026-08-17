# 模型融合（CosmosPredict2_2B）

The ModelMergeCosmosPredict2_2B node merges two diffusion models using a block-based approach with fine-grained control over different model components. It allows you to blend specific parts of two models by adjusting interpolation weights for position embedders, time embedders, transformer blocks, and final layers. This provides precise control over how different architectural components from each model contribute to the final merged result.

ModelMergeCosmosPredict2_2B 节点采用基于块的方法合并两个扩散模型，并可对不同模型组件进行精细控制。通过调整位置嵌入器、时间嵌入器、Transformer 块和最终层的插值权重，您可以混合两个模型的特定部分。这样可以精确控制每个模型的不同架构组件对最终合并结果的贡献程度。

## Inputs

## 输入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model1` | The first model to merge | MODEL | Yes | - |
| `model1` | 要合并的第一个模型 | MODEL | 是 | - |
| `model2` | The second model to merge | MODEL | Yes | - |
| `model2` | 要合并的第二个模型 | MODEL | 是 | - |
| `pos_embedder.` | Position embedder interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `pos_embedder.` | 位置嵌入器的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `x_embedder.` | Input embedder interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `x_embedder.` | 输入嵌入器的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedder.` | Time embedder interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `t_embedder.` | 时间嵌入器的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedding_norm.` | Time embedding normalization interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `t_embedding_norm.` | 时间嵌入归一化的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.0.` | Transformer block 0 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.0.` | Transformer 块 0 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.1.` | Transformer block 1 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.1.` | Transformer 块 1 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.2.` | Transformer block 2 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.2.` | Transformer 块 2 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.3.` | Transformer block 3 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.3.` | Transformer 块 3 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.4.` | Transformer block 4 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.4.` | Transformer 块 4 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.5.` | Transformer block 5 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.5.` | Transformer 块 5 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.6.` | Transformer block 6 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.6.` | Transformer 块 6 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.7.` | Transformer block 7 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.7.` | Transformer 块 7 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.8.` | Transformer block 8 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.8.` | Transformer 块 8 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.9.` | Transformer block 9 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.9.` | Transformer 块 9 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.10.` | Transformer block 10 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.10.` | Transformer 块 10 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.11.` | Transformer block 11 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.11.` | Transformer 块 11 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.12.` | Transformer block 12 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.12.` | Transformer 块 12 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.13.` | Transformer block 13 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.13.` | Transformer 块 13 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.14.` | Transformer block 14 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.14.` | Transformer 块 14 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.15.` | Transformer block 15 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.15.` | Transformer 块 15 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.16.` | Transformer block 16 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.16.` | Transformer 块 16 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.17.` | Transformer block 17 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.17.` | Transformer 块 17 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.18.` | Transformer block 18 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.18.` | Transformer 块 18 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.19.` | Transformer block 19 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.19.` | Transformer 块 19 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.20.` | Transformer block 20 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.20.` | Transformer 块 20 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.21.` | Transformer block 21 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.21.` | Transformer 块 21 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.22.` | Transformer block 22 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.22.` | Transformer 块 22 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.23.` | Transformer block 23 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.23.` | Transformer 块 23 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.24.` | Transformer block 24 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.24.` | Transformer 块 24 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.25.` | Transformer block 25 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.25.` | Transformer 块 25 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.26.` | Transformer block 26 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.26.` | Transformer 块 26 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.27.` | Transformer block 27 interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `blocks.27.` | Transformer 块 27 的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `final_layer.` | Final layer interpolation weight (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `final_layer.` | 最终层的插值权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## Outputs

## 输出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The merged model combining features from both input models | MODEL |
| `model` | 融合了两个输入模型特征的合并模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/zh.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
