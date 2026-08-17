# 模型融合（LTXV）

ModelMergeLTXV 通过混合两个 LTXV 模型的内部组件，将它们合并为一个模型。每个权重参数控制 `model2` 的特定部分以多大强度混入 `model1`，值越低越偏向 `model1`，值越高越偏向 `model2`。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model1` | 要合并的第一个模型 | MODEL | 是 | - |
| `model2` | 要合并的第二个模型 | MODEL | 是 | - |
| `patchify_proj.` | patchify 投影层的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `adaln_single.` | 自适应层归一化单层的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `caption_projection.` | 字幕投影层的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.0.` | Transformer 块 0 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.1.` | Transformer 块 1 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.2.` | Transformer 块 2 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.3.` | Transformer 块 3 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.4.` | Transformer 块 4 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.5.` | Transformer 块 5 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.6.` | Transformer 块 6 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.7.` | Transformer 块 7 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.8.` | Transformer 块 8 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.9.` | Transformer 块 9 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.10.` | Transformer 块 10 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.11.` | Transformer 块 11 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.12.` | Transformer 块 12 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.13.` | Transformer 块 13 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.14.` | Transformer 块 14 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.15.` | Transformer 块 15 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.16.` | Transformer 块 16 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.17.` | Transformer 块 17 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.18.` | Transformer 块 18 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.19.` | Transformer 块 19 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.20.` | Transformer 块 20 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.21.` | Transformer 块 21 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.22.` | Transformer 块 22 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.23.` | Transformer 块 23 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.24.` | Transformer 块 24 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.25.` | Transformer 块 25 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.26.` | Transformer 块 26 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.27.` | Transformer 块 27 的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `scale_shift_table` | 缩放偏移表的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `proj_out.` | 投影输出层的插值权重（默认：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 根据指定的插值权重，融合两个输入模型特征的合并模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/zh.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
