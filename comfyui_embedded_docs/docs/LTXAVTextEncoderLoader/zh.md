# LTXV音频文本编码器加载器

该节点为 LTXV 音频模型加载专用的文本编码器。它将文本编码器文件与检查点文件组合，创建一个可用于音频相关文本条件任务的 CLIP 模型。根据节点的配方描述，LTXV 音频文本编码器应为 Gemma 3 12B 模型或匹配的 Gemma 4 模型。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `text_encoder` | 要加载的 LTXV 文本编码器文件名。可用选项从 `text_encoders` 文件夹中加载。 | COMBO | 是 | 多个可用选项 |
| `ckpt_name` | 要加载的检查点文件名。可用选项从 `checkpoints` 文件夹中加载。 | COMBO | 是 | 多个可用选项 |
| `device` | 指定加载模型的设备。使用 `"cpu"` 强制加载到 CPU。默认行为（`"default"`）使用系统的自动设备放置（默认值：`"default"`）。 | COMBO | 否 | `"default"`<br>`"cpu"` |

**注意：** `text_encoder` 和 `ckpt_name` 参数协同工作。该节点加载两个指定文件以创建一个可用的完整 CLIP 模型。这两个文件必须与 LTXV 架构兼容。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `clip` | 加载的 LTXV CLIP 模型，可直接用于对音频生成所需的文本提示进行编码。 | CLIP |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/zh.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`
