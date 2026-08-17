# 修剪视频Latent

TrimVideoLatent 节点用于从视频潜空间表示的起始处移除帧。它接收一个潜空间视频样本，从开头修剪掉指定数量的帧，并返回视频的剩余部分。这样可以通过移除起始帧来缩短视频序列。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `samples` | 待修剪的输入潜空间视频表示，包含视频帧 | LATENT | 是 | - |
| `trim_amount` | 要从视频开头移除的帧数（默认值：0） | INT | 是 | 0 to 99999 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `output` | 从开头移除指定数量帧后的潜空间视频表示 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/zh.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
