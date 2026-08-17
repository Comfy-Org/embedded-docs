# 分辨率 Bucket

此节点按分辨率组织潜在变量列表及其对应的条件数据。它将具有相同高度和宽度的项分组在一起，为每个唯一分辨率创建单独的批次。此过程有助于准备高效训练所需的数据，因为它允许模型同时处理多个相同尺寸的项。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `latents` | 按分辨率分桶的潜在变量字典列表 | LATENT | Yes | N/A |
| `conditioning` | 条件列表的列表（必须与 `latents` 长度匹配） | CONDITIONING | Yes | N/A |

**注意：** `latents` 列表中的项数必须与 `conditioning` 列表中的项数完全匹配。每个潜在变量字典可以包含一批样本，相应的条件列表必须包含与该批次匹配数量的条件项。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `latents` | 按分辨率分桶后的潜在变量字典列表，每个分辨率桶一个 | LATENT |
| `conditioning` | 条件列表的列表，每个分辨率桶一个 | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/zh.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
