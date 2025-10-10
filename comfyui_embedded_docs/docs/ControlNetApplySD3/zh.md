> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/zh.md)

{heading_overview}

该节点将 ControlNet 引导应用于 Stable Diffusion 3 的条件输入。它接收正向和负向条件输入，以及 ControlNet 模型和图像，然后通过可调节的强度和时间参数来应用控制引导，从而影响生成过程。

**注意：** 此节点已被标记为弃用，可能在未来的版本中被移除。

{heading_inputs}

| 参数 | 数据类型 | 必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 要应用 ControlNet 引导的正向条件输入 |
| `negative` | CONDITIONING | 是 | - | 要应用 ControlNet 引导的负向条件输入 |
| `control_net` | CONTROL_NET | 是 | - | 用于引导的 ControlNet 模型 |
| `vae` | VAE | 是 | - | 过程中使用的 VAE 模型 |
| `image` | IMAGE | 是 | - | ControlNet 将用作引导的输入图像 |
| `strength` | FLOAT | 是 | 0.0 - 10.0 | ControlNet 效果的强度（默认值：1.0） |
| `start_percent` | FLOAT | 是 | 0.0 - 1.0 | ControlNet 开始应用的生成过程起始点（默认值：0.0） |
| `end_percent` | FLOAT | 是 | 0.0 - 1.0 | ControlNet 停止应用的生成过程结束点（默认值：1.0） |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 应用了 ControlNet 引导的修改后正向条件输入 |
| `negative` | CONDITIONING | 应用了 ControlNet 引导的修改后负向条件输入 |