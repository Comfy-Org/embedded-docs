# 模型融合（SD35_大）

ModelMergeSD35_Large 节点允许你通过调整不同模型组件的影响，将两个 Stable Diffusion 3.5 Large 模型融合在一起。它能够精确控制第二个模型的每个部分对最终合并模型的贡献程度，从嵌入层到联合块，再到最终层。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model1` | 用作合并基础的模型 | MODEL | Yes | - |
| `model2` | 需要将其组件融合到基础模型中的次要模型 | MODEL | Yes | - |
| `pos_embed.` | 控制 model2 的位置嵌入融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `x_embedder.` | 控制 model2 的 x 嵌入器融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `context_embedder.` | 控制 model2 的上下文嵌入器融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `y_embedder.` | 控制 model2 的 y 嵌入器融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `t_embedder.` | 控制 model2 的 t 嵌入器融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.0.` | 控制 model2 的联合块 0 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.1.` | 控制 model2 的联合块 1 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.2.` | 控制 model2 的联合块 2 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.3.` | 控制 model2 的联合块 3 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.4.` | 控制 model2 的联合块 4 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.5.` | 控制 model2 的联合块 5 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.6.` | 控制 model2 的联合块 6 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.7.` | 控制 model2 的联合块 7 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.8.` | 控制 model2 的联合块 8 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.9.` | 控制 model2 的联合块 9 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.10.` | 控制 model2 的联合块 10 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.11.` | 控制 model2 的联合块 11 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.12.` | 控制 model2 的联合块 12 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.13.` | 控制 model2 的联合块 13 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.14.` | 控制 model2 的联合块 14 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.15.` | 控制 model2 的联合块 15 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.16.` | 控制 model2 的联合块 16 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.17.` | 控制 model2 的联合块 17 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.18.` | 控制 model2 的联合块 18 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.19.` | 控制 model2 的联合块 19 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.20.` | 控制 model2 的联合块 20 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.21.` | 控制 model2 的联合块 21 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.22.` | 控制 model2 的联合块 22 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.23.` | 控制 model2 的联合块 23 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.24.` | 控制 model2 的联合块 24 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.25.` | 控制 model2 的联合块 25 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.26.` | 控制 model2 的联合块 26 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.27.` | 控制 model2 的联合块 27 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.28.` | 控制 model2 的联合块 28 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.29.` | 控制 model2 的联合块 29 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.30.` | 控制 model2 的联合块 30 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.31.` | 控制 model2 的联合块 31 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.32.` | 控制 model2 的联合块 32 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.33.` | 控制 model2 的联合块 33 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.34.` | 控制 model2 的联合块 34 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.35.` | 控制 model2 的联合块 35 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.36.` | 控制 model2 的联合块 36 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `joint_blocks.37.` | 控制 model2 的联合块 37 融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |
| `final_layer.` | 控制 model2 的最终层融合到合并模型中的程度（默认：1.0） | FLOAT | Yes | 0.0 to 1.0 |

**注意：** 所有混合参数均接受 0.0 到 1.0 之间的值，其中 0.0 表示 model2 对该特定组件没有贡献，1.0 表示 model2 完全贡献。它们以 0.01 的步长递增。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 根据指定的混合参数，融合了两个输入模型特征的最终合并模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/zh.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`
