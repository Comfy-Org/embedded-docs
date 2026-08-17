# 模型融合Qwen图像

ModelMergeQwenImage 节点通过以可调整的权重组合两个 AI 模型的组件来合并它们。它允许您混合 Qwen 图像模型的特定部分，包括 transformer 块、位置嵌入和文本处理组件。您可以控制每个模型对合并结果不同部分的影响程度。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model1` | 要合并的第一个模型（默认：无） | MODEL | 是 | - |
| `model2` | 要合并的第二个模型（默认：无） | MODEL | 是 | - |
| `pos_embeds.` | 位置嵌入混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `img_in.` | 图像输入处理混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `txt_norm.` | 文本归一化混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `txt_in.` | 文本输入处理混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `time_text_embed.` | 时间与文本嵌入混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `transformer_blocks.0.` 到 `transformer_blocks.59.` | 每个 transformer 块混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |
| `proj_out.` | 输出投影混合的权重（默认：1.0） | FLOAT | 是 | 0.0 到 1.0 |

注意：共有 60 个独立的 transformer 块权重输入（`transformer_blocks.0.` 到 `transformer_blocks.59.`），对应模型中的每个 transformer 块。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 合并后的模型，以指定权重组合两个输入模型的组件 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/zh.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
