# WAN上下文窗口（手动）

Wan Context Windows (Manual) 节点允许您为类似 Wan 的二维处理模型手动配置上下文窗口。它通过在采样时指定窗口长度、重叠、调度方法和融合技术来应用上下文窗口设置，让您能够控制模型如何处理不同的上下文区域。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 采样时要应用上下文窗口的模型。 | MODEL | 是 | - |
| `context_length` | 上下文窗口的实际帧长度。必须满足 4*n + 1。（默认值：81） | INT | 是 | 1 to 16384 (step 4) |
| `context_overlap` | 上下文窗口在实际帧中的重叠长度。（默认值：30） | INT | 是 | 0 or greater |
| `context_schedule` | 上下文窗口的步进相关调度算法。（默认值："uniform_standard"） | COMBO | 是 | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | 上下文窗口的步幅；仅适用于 uniform 调度。（默认值：1） | INT | 是 | 1 or greater |
| `closed_loop` | 是否闭合上下文窗口循环；仅适用于 looped 调度。（默认值：False） | BOOLEAN | 是 | True or False |
| `fuse_method` | 用于融合上下文窗口的方法。（默认值："pyramid"） | COMBO | 是 | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | 是否应用 FreeNoise 噪声重排，可改善窗口混合效果。（默认值：True） | BOOLEAN | 是 | True or False |
| `retain_first_frame` | 在每个上下文窗口中保留第一个 I2V 帧（可能有助于保留初始参考）。（默认值：False） | BOOLEAN | 是 | True or False |
| `split_conds_to_windows` | 是否根据区域索引将 ConditionCombine 创建的多个 conditioning 拆分到每个窗口。（默认值：False） | BOOLEAN | 是 | True or False |

**注意：** `context_stride` 仅影响 uniform 调度，`closed_loop` 仅适用于 looped 调度。`context_length` 应遵循 4n + 1 的模式。该节点在应用前会将 `context_length` 和 `context_overlap` 从实际帧转换为模型单位，并强制 `context_length` 最小为 1，`context_overlap` 最小为 0。`context_stride`、`closed_loop`、`freenoise` 和 `split_conds_to_windows` 输入为高级选项。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已应用上下文窗口配置的模型。 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/zh.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
