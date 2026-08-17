# 上下文窗口（手动）

The Context Windows (Manual) 节点允许您在采样期间手动为模型配置上下文窗口。它会创建具有指定长度、重叠和调度模式的重叠上下文片段，以可管理的数据块处理数据，同时保持片段之间的连续性。该节点提供了用于控制上下文窗口应用方式的高级选项，包括噪声混洗、条件保留、噪声 latent 保留以及因果窗口修复。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 在采样期间应用上下文窗口的模型。 | MODEL | 是 | - |
| `context_length` | 上下文窗口的长度（默认：16）。 | INT | 否 | 1+ |
| `context_overlap` | 上下文窗口的重叠长度（默认：4）。 | INT | 否 | 0+ |
| `context_schedule` | 上下文窗口的步进依赖调度算法（默认：STATIC_STANDARD）。 | COMBO | 否 | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | 上下文窗口的步幅；仅适用于均匀调度（默认：1）。 | INT | 否 | 1+ |
| `closed_loop` | 是否闭合上下文窗口循环；仅适用于循环调度（默认：False）。 | BOOLEAN | 否 | - |
| `fuse_method` | 用于融合上下文窗口的方法（默认：PYRAMID）。 | COMBO | 否 | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | 要应用上下文窗口的维度（默认：0）。 | INT | 否 | 0-5 |
| `freenoise` | 是否应用 FreeNoise 噪声混洗以改善窗口融合（默认：False）。 | BOOLEAN | 否 | - |
| `cond_retain_index_list` | 每个窗口的条件张量中要保留的 latent 索引列表。对于 concat 风格的 I2V 模型（例如 Wan I2V、HunyuanVideo I2V、Cosmos I2V、SVD），编码后的起始图像位于 c_concat 条件通道中；将此设置为 '0' 将在每个窗口的 sub-pos 0 位置保留该起始图像内容（默认：""）。 | STRING | 否 | - |
| `split_conds_to_windows` | 是否根据区域索引将多个条件（由 ConditionCombine 创建）拆分到每个窗口（默认：False）。 | BOOLEAN | 否 | - |
| `latent_retain_index_list` | 每个窗口的噪声 latent 本身要保留的 latent 索引列表。用于参考内容（例如起始图像）直接存在于噪声 latent 中，而不是存在于单独的条件通道中的工作流（例如 LTXV、AnimateDiff 等 inplace 风格的 I2V）。与 `cond_retain_index_list` 相互独立（默认：""）。 | STRING | 否 | - |
| `causal_window_fix` | 是否为非 0 索引的上下文窗口添加因果修复帧（causal fix frame）（默认：True）。 | BOOLEAN | 否 | - |

**参数约束：**

- `context_stride` 仅在选择了均匀调度时使用。
- `closed_loop` 仅适用于循环调度。
- `dim` 必须介于 0 到 5 之间（含端点）。
- `cond_retain_index_list` 需要一个以逗号分隔的整数索引字符串（例如："0,1,2"）。
- `latent_retain_index_list` 需要一个以逗号分隔的整数索引字符串（例如："0,1,2"），并且与 `cond_retain_index_list` 相互独立。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 在采样期间应用了上下文窗口的模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/zh.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
