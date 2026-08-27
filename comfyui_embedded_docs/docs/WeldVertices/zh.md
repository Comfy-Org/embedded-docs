# WeldVertices

Weld Vertices 合并 3D 网格中重合的顶点，使原本具有独立角点的面最终共享相同的顶点。它使用基于网格边界框的容差进行网格量化来对邻近顶点分组，并对每个合并组中的顶点颜色取平均值。当网格以未焊接状态导入时（即每个面都有自己的顶点且没有共享边），此节点非常有用。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 输入 3D 网格，其重合顶点将被合并。 | MESH | 是 | - |
| `epsilon_rel` | 焊接容差（边界框对角线的比例）。1e-5 用于浮点去重；1e-3 用于视觉上接近但不同的顶点。默认值：1e-5。 | FLOAT | 是 | 0.0 to unlimited |
| `epsilon_abs` | 绝对焊接容差（大于 0 时覆盖 `epsilon_rel`）。默认值：0.0。 | FLOAT | 是 | 0.0 to unlimited |

注意：当 `epsilon_abs` 大于 0 时，它优先于 `epsilon_rel`，相对容差将被忽略。当 `epsilon_abs` 为 0 时，使用相对容差 `epsilon_rel`。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `mesh` | 焊接后的网格，包含合并的顶点、更新后的面索引以及平均后的顶点颜色（如果输入网格带有颜色）。 | MESH |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/zh.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
