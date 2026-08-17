# Beta采样调度器

BetaSamplingScheduler 节点会创建一系列噪声水平（sigma），用于控制图像生成过程中采样阶段的噪声去除方式。它采用 beta 调度算法，并通过 `alpha` 和 `beta` 设置来调整噪声调度的形状。生成的 sigma 会传递给采样器，以指导去噪过程。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 用于采样的模型，提供模型采样对象。 | MODEL | 是 | - |
| `steps` | 要为其生成 sigma 的采样步数（默认值：20）。 | INT | 是 | 1 to 10000 |
| `alpha` | beta 调度器的 Alpha 参数，控制调度曲线（默认值：0.6）。高级参数。 | FLOAT | 是 | 0.0 to 50.0 |
| `beta` | beta 调度器的 Beta 参数，控制调度曲线（默认值：0.6）。高级参数。 | FLOAT | 是 | 0.0 to 50.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `SIGMAS` | 用于采样过程的噪声水平（sigma）序列。 | SIGMAS |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/zh.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
