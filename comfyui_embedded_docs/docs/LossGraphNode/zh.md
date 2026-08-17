# 绘制损失图

LossGraphNode 会创建一张训练损失值随时间变化的可视化图表，并将其作为预览图像显示。它接收来自训练过程的损失数据，生成一张折线图，展示损失在训练步骤中的变化情况。生成的图表包含坐标轴标签以及最小/最大损失值。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `loss` | 来自训练节点的损失映射。必须包含一个 `loss` 键，其值为用于绘制图表的损失值列表。 | LOSS_MAP | 是 | - |
| `filename_prefix` | 保存的损失图表图像的前缀。（默认值："loss_graph"） | STRING | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `ui.images` | 生成的损失图表图像，以预览形式显示。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/zh.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
