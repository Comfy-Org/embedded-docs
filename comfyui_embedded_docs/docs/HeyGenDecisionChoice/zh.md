# HeyGen Decision (Choice)

为你所连接的文本、图像、音频或视频，从你自己定义的选项中选择一个，并返回被选中的选项、其位置以及置信度。将 `choice` 连接到输入携带相同选项名称的 Branch 节点，或依据 `option_index` 进行路由。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型。`heygen-decision-1-turbo` 比 `heygen-decision-1` 更快且成本更低（默认：`"heygen-decision-1"`）。 | COMBO | 是 | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | 这些选项所回答的问题，最多 5000 个字符（默认："What style is the image?"）。 | STRING | 是 | 1 到 5000 个字符 |
| `options` | 每行一个选项，按原样使用，每个最多 128 个字符。对于不属于任何选项的输入，请添加诸如 `other` 之类的选项（默认：`photo`、`illustration`、`3d render`、`anime`、`sketch`、`other`）。 | STRING | 是 | 2 到 255 个选项 |
| `images` | 要分类的图像，总数最多 4 张，批次的每一帧也计入其中。它们会按套接字顺序依次编号为 `image_1` 到 `image_4`。 | IMAGE | 否 | 最多 4 张图像 |
| `audio_1` | 要分类的音频，最长 30 分钟。 | AUDIO | 否 | 最多 30 分钟 |
| `video_1` | 要分类的视频，最长 60 秒。 | VIDEO | 否 | 最多 60 秒 |
| `text` | 问题所针对的文本，例如提示词或 LLM 回复，最多 20000 个字符。 | STRING | 否 | 最多 20000 个字符 |

请提供 2 到 255 个选项，不得重复，也不得仅大小写不同，否则该节点会报错。至少连接一个待分类的输入，并在问题中通过套接字名称指代它们，例如「image_1 中显示的是哪个季节？」。

## 输出

| 输出名 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `choice` | 被选中的选项，与 `options` 中书写的内容完全一致。 | STRING |
| `option_index` | 被选中选项在 `options` 中的位置，从 0 开始。 | INT |
| `confidence` | 对该选择的置信度，介于 0 和 1 之间。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/zh.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
