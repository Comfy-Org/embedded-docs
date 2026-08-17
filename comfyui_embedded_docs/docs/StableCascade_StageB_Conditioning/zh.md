# Stable Cascade_B阶段_条件

StableCascade_StageB_Conditioning 节点通过将现有 conditioning 信息与 Stage C 的先前潜在表示相结合，为 Stable Cascade Stage B 生成准备 conditioning 数据。它修改每个 conditioning 条目以包含来自 Stage C 的潜在样本，使生成过程能够利用先前信息以获得更连贯的输出。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要使用 Stage C 先前信息修改的 conditioning 数据 | CONDITIONING | 是 | - |
| `stage_c` | 来自 Stage C 的潜在表示，包含用于 conditioning 的先前样本 | LATENT | 是 | - |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `CONDITIONING` | 整合了 Stage C 先前信息的修改后 conditioning 数据 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/zh.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
