# 插值扩展Sigmas

`ExtendIntermediateSigmas` 节点接收现有的 sigma 值序列，并在它们之间插入额外的中间 sigma 值。您可以指定要添加的额外步数、插值所使用的间距方式，以及可选的起始和结束 sigma 边界，以控制扩展在 sigma 序列中的发生范围。

## 输入
| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `sigmas` | 要扩展的输入 sigma 序列，附加中间值 | SIGMAS | 是 | - |
| `steps` | 在现有 sigma 值之间插入的中间步数；当步数为 N 时，在每一对符合条件的 sigma 之间插入 N-1 个中间 sigma 值（默认值：2） | INT | 是 | 1 to 100 |
| `start_at_sigma` | 扩展的上 sigma 边界——仅扩展低于此值的 sigma（默认值：-1.0，表示无穷大） | FLOAT | 是 | -1.0 to 20000.0 |
| `end_at_sigma` | 扩展的下 sigma 边界——仅扩展高于此值的 sigma（默认值：12.0） | FLOAT | 是 | 0.0 to 20000.0 |
| `spacing` | 用于分配中间 sigma 值的插值方法："linear" 均匀分布，"cosine" 和 "sine" 采用曲线间距（默认值："linear"） | COMBO | 是 | `"linear"`<br>`"cosine"`<br>`"sine"` |

**注意：**该节点仅在当前 sigma 小于或等于 `start_at_sigma` 且大于或等于 `end_at_sigma` 的现有 sigma 对之间插入中间 sigma。当 `start_at_sigma` 设置为 -1.0 时，它被视为无穷大，因此仅应用 `end_at_sigma` 下边界。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `sigmas` | 已扩展的 sigma 序列，其中插入了额外的中间值 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/zh.md)

---
**Source fingerprint (SHA-256):** `d761e82ce055bc56a551d3e446117febb2cdbd6c0286ef620d0a078c96f047ba`
