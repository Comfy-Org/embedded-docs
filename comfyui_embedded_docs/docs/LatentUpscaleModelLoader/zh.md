# 加载Latent放大模型

LatentUpscaleModelLoader 节点用于加载专门放大潜在表示的模型。它从系统指定文件夹中读取模型文件，并自动检测其类型（720p、1080p 或其他），以实例化和配置正确的内部模型架构。加载后的模型即可供其他节点用于潜在空间超分辨率任务。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model_name` | 要加载的潜在放大模型文件的名称。可用选项会根据 ComfyUI 的 `latent_upscale_models` 目录中的文件动态填充。 | COMBO | 是 | `latent_upscale_models` 文件夹中的所有文件 |

注意：节点会根据文件内容自动检测模型架构。包含 720p HunyuanVideo 超分辨率层的模型会作为 720p 模型加载；包含 1080p 风格上采样层的模型会作为 1080p 模型加载；包含其他层结构的模型会作为 LatentUpsampler 模型加载。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 已加载的潜在放大模型，已配置并可随时使用。 | LATENT_UPSCALE_MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/zh.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
