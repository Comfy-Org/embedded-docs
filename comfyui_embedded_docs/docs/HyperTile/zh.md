# 超分块HyperTile

HyperTile 节点对扩散模型中的注意力机制应用分块技术，以优化图像生成期间的内存使用。它将潜在空间划分为更小的块并分别处理，然后重新组合结果。这使得在不耗尽内存的情况下处理更大的图像尺寸成为可能。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用 HyperTile 优化的扩散模型 | MODEL | 是 | - |
| `tile_size` | 处理的目标块大小（默认值：256）。实际块大小会向下取整为 8 的倍数，最小为 32。 | INT | 否 | 1 - 2048 |
| `swap_size` | 节点随机选择如何分割图像时所考虑的候选块分割数量。较大的值允许分割时有更多变化（默认值：2） | INT | 否 | 1 - 128 |
| `max_depth` | 应用分块的最大深度级别（分辨率层级）。值为 0 时仅在最高分辨率下应用分块（默认值：0） | INT | 否 | 0 - 10 |
| `scale_depth` | 启用后，在更深的深度级别下，块大小会按比例缩放。这有助于在较低分辨率下保持质量（默认值：False） | BOOLEAN | 否 | True / False |

注意：`scale_depth` 仅在 `max_depth` 大于 0 时生效，因为在最高分辨率级别（深度 0）下，块大小永远不会缩放。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用 HyperTile 优化的模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/zh.md)

---
**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`
