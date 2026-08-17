# 模型融合（Auraflow ）

ModelMergeAuraflow 允许您通过调整不同模型组件的特定混合权重，将两个不同的模型混合在一起。它可以对模型各部分（从初始层到最终输出）的合并方式进行精细控制，专为 Auraflow 风格的模型架构设计。此节点在创建自定义模型组合时尤为有用，可实现对合并过程的精确控制。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model1` | 要合并的第一个模型 | MODEL | 是 | - |
| `model2` | 要合并的第二个模型 | MODEL | 是 | - |
| `init_x_linear.` | 初始线性变换的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `positional_encoding` | 位置编码组件的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `cond_seq_linear.` | 条件序列线性层的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `register_tokens` | 令牌注册组件的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedder.` | 时间嵌入组件的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.0.` | 双层层组 0 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.1.` | 双层层组 1 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.2.` | 双层层组 2 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.3.` | 双层层组 3 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.0.` | 单层层 0 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.1.` | 单层层 1 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.2.` | 单层层 2 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.3.` | 单层层 3 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.4.` | 单层层 4 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.5.` | 单层层 5 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.6.` | 单层层 6 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.7.` | 单层层 7 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.8.` | 单层层 8 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.9.` | 单层层 9 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.10.` | 单层层 10 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.11.` | 单层层 11 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.12.` | 单层层 12 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.13.` | 单层层 13 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.14.` | 单层层 14 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.15.` | 单层层 15 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.16.` | 单层层 16 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.17.` | 单层层 17 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.18.` | 单层层 18 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.19.` | 单层层 19 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.20.` | 单层层 20 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.21.` | 单层层 21 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.22.` | 单层层 22 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.23.` | 单层层 23 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.24.` | 单层层 24 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.25.` | 单层层 25 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.26.` | 单层层 26 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.27.` | 单层层 27 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.28.` | 单层层 28 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.29.` | 单层层 29 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.30.` | 单层层 30 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.31.` | 单层层 31 的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `modF.` | modF 组件的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `final_linear.` | 最终线性变换的混合权重（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 根据指定的混合权重，结合两个输入模型特征得到的合并模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/zh.md)

---
**Source fingerprint (SHA-256):** `e9d3d81b2a3f81b082f9dc9f662f4e51df66f1f077e2899a1fea9a7061c4a97b`
