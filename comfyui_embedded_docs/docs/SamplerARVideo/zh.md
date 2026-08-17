# 采样器 AR 视频

The Sampler AR Video 节点为自回归视频模型（例如使用因果强制或自强制技术的模型）提供了一种专门的采样方法。它直接在工作流中管理与自回归（AR）循环相关的所有参数，使配置模型如何逐步生成视频帧变得简单。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | 每个自回归块的帧数。值为 1 表示模型一次生成一帧（逐帧），值为 3 表示模型一次生成三帧（逐块）。此设置必须与检查点的训练模式匹配。默认值：1。 | INT | 是 | 1 到 64 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `SAMPLER` | 一个配置好的采样器对象，使用 "ar_video" 采样函数并带有指定的自回归参数。 | SAMPLER |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/zh.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
