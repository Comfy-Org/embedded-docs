# 应用ControlNet

此节点将 ControlNet 引导应用于 Stable Diffusion 3 条件。它接收正向和负向条件输入以及 ControlNet 模型和图像，然后通过可调整的强度和时序参数应用控制引导，以影响生成过程。

**注意：** 此节点已被标记为已弃用，并可能在未来的版本中移除。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 要应用 ControlNet 引导的正向条件 | CONDITIONING | 是 | - |
| `negative` | 要应用 ControlNet 引导的负向条件 | CONDITIONING | 是 | - |
| `control_net` | 用于引导的 ControlNet 模型 | CONTROL_NET | 是 | - |
| `vae` | 流程中使用的 VAE 模型 | VAE | 是 | - |
| `image` | ControlNet 将用作引导的输入图像 | IMAGE | 是 | - |
| `strength` | ControlNet 效果的强度（默认值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `start_percent` | 生成过程中 ControlNet 开始应用的起始点（默认值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `end_percent` | 生成过程中 ControlNet 停止应用的结束点（默认值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

**注意：** 当 `strength` 设置为 0 时，节点会返回未更改的正向和负向条件，而不应用 ControlNet。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 应用了 ControlNet 引导的修改后正向条件 | CONDITIONING |
| `negative` | 应用了 ControlNet 引导的修改后负向条件 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/zh.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
