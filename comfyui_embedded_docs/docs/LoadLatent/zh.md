# 加载Latent

LoadLatent 节点加载先前在输入目录中保存为 .latent 文件的潜在表示。它从所选文件中读取潜在张量数据，并在返回结果供其他节点使用之前进行必要的缩放调整。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
| --- | --- | --- | --- | --- |
| `latent` | 从输入目录中的可用文件中选择要加载的 .latent 文件 | COMBO | 是 | 输入目录中的所有 .latent 文件 |

注意：对于不包含 `latent_format_version_0` 标记的 .latent 文件，加载的潜在张量会乘以 1/0.18215，使其缩放与其他节点预期的格式相匹配。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `LATENT` | 返回所选文件中加载的潜在表示数据 | LATENT |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/zh.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
