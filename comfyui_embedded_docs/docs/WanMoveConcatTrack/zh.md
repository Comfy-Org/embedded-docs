# WanMove合并轨道

WanMoveConcatTrack 节点将两组运动跟踪数据合并为一个更长的序列。它通过沿着各自维度连接输入轨迹中的轨迹路径和可见性掩码来工作。如果只提供一个轨迹输入，则直接将该数据原样传递。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `tracks_1` | 要连接的第一组运动跟踪数据。 | TRACKS | 是 |  |
| `tracks_2` | 可选的第二组运动跟踪数据。如果未提供，`tracks_1` 将直接传递到输出。 | TRACKS | 否 |  |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `tracks` | 连接后的运动跟踪数据，包含来自输入的合并后的 `track_path` 和 `track_visibility`。 | TRACKS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/zh.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
