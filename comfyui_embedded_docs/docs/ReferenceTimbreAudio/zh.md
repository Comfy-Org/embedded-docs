# ReferenceTimbreAudio

此节点用于在“ace step 1.5”流程中设置参考音频音色。它接收一个 conditioning 输入和一个可选的音频潜空间表示，然后将该潜空间数据附加到 conditioning 上，以便工作流中的后续节点将其用作参考音频。如果未提供潜空间数据，则 conditioning 将原样返回。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要附加参考音频信息的 conditioning 数据。 | CONDITIONING | 是 |  |
| `latent` | 参考音频的可选潜空间表示。提供时，其样本会被添加到 conditioning 中。 | LATENT | 否 |  |

当提供 `latent` 时，其样本会被追加到 conditioning 的参考音频音色潜空间数据中。如果未提供 `latent`，则原始 conditioning 将原样传递。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `conditioning` | 修改后的 conditioning 数据。如果提供了可选的 `latent` 输入，则其中包含参考音频音色潜空间数据；如果未提供潜空间数据，则返回原始 conditioning 不变。 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/zh.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
