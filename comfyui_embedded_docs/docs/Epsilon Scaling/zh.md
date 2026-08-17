# Epsilon缩放

此节点实现了研究论文《Elucidating the Exposure Bias in Diffusion Models》（arxiv.org/abs/2308.15321v6）中的 Epsilon Scaling 方法。其工作原理是在采样过程中缩放预测噪声，以帮助减少曝光偏差，从而提升生成图像的质量。本实现采用了论文中推荐的“均匀调度”（uniform schedule），因其兼具实用性和有效性。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 将应用 epsilon scaling 补丁的模型。 | MODEL | 是 | - |
| `scaling_factor` | 预测噪声的缩放因子。值大于 1.0 会降低预测噪声，而值小于 1.0 会增加预测噪声（默认值：1.005）。 | FLOAT | 是 | 0.5 - 1.5 (step: 0.001) |

注意：`scaling_factor` 受保护，避免值为零，以防止除以零。UI 强制最小值为 0.5，因此正常使用中不会出现这种情况。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 输入模型的打过补丁的副本，其采样过程应用了 epsilon scaling 函数。原始模型保持不变。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/zh.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
