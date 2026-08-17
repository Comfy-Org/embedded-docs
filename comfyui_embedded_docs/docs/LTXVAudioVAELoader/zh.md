# LTXV音频VAE加载器

LTXV Audio VAE Loader 节点从检查点文件加载预训练的音频变分自编码器（VAE）模型。它读取指定的检查点，加载其权重和元数据，并准备模型以供 ComfyUI 中的音频生成或处理工作流使用。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 要加载的音频 VAE 检查点。这是一个下拉列表，其中包含你的 ComfyUI `checkpoints` 目录中找到的所有文件。 | COMBO | 是 | `checkpoints` 文件夹中的所有文件（动态填充）。<br>*示例：`"audio_vae.safetensors"`* |

注意：如果选择的检查点文件无法找到或不包含有效的音频 VAE，节点将引发错误。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `Audio VAE` | 加载的音频变分自编码器模型，可连接到其他音频处理节点。 | VAE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/zh.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
