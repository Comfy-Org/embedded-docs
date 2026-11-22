# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) 节点从一批图像中挑选一张图像。将同一图像批次连同 `index` 一起连接到 Get Image from Batch，以保留所挑选的图像；或读取 `confidence` 来判断该选择是否足够好。这是一个 API 节点：它在 Comfy 的服务器上运行，并且需要一个带有积分的 Comfy.org 账户。

## 输入

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 Jev 模型。目前只有一个模型可用：`jev-1.14.0`。 | COMBO | 是 | `"jev-1.14.0"` |
| `question` | 要挑选哪张图像。将提示词连接到 `text`，以挑选与其最匹配的图像（默认：`Which image best matches the prompt in text? If there is no text, which image has the best quality?`）。 | STRING | 是 | 1 到 1000 个字符 |
| `images` | 可供选择的图像。批处理输入中的每张图像都计为一次，因此批次中的每张图像都是候选对象。上传前，每张图像的长边会根据批次大小受到限制：最多 4 张图像时为 1568 像素，最多 8 张时为 1024 像素，最多 16 张时为 768 像素，最多 32 张时为 512 像素，因此批次越大，每张图像的细节越少。 | IMAGE | 是 | 2 到 32 张图像 |
| `text` | 问题所针对的文本，例如生成这些图像所用的提示词。 | STRING | 否 | 0 到 3000 个字符 |

**说明：**

- 当连接的图像少于 2 张或多于 32 张时，节点会报错。
- `index` 从 0 开始计数，这正是 Get Image from Batch 所期望的位置。
- 计费基于 token；节点上的价格徽章显示每 100 万 token 的近似费率。

## 输出

| 输出名 | 描述 | 数据类型 |
| --- | --- | --- |
| `index` | 所挑选图像在批次中的位置，从 0 开始。 | INT |
| `confidence` | Jev 的确定程度，从 0（没有明显胜出者）到 1（确定）。 | FLOAT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/zh.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
