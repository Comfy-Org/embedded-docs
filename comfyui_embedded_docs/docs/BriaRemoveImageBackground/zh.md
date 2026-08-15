# Bria 移除图像背景

此节点使用 Bria RMBG 2.0 服务移除图像背景。它将图像发送到外部 API 进行处理，并返回移除背景后的结果。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要移除背景的输入图像。 | IMAGE | 是 | - |
| `moderation` | 审核设置。当设置为 `"true"` 时，将提供额外的审核选项。 | COMBO | 否 | `"false"`<br>`"true"` |
| `visual_input_moderation` | 对输入图像启用视觉内容审核。此参数仅在 `moderation` 设置为 `"true"` 时可用。默认值：`False`。 | BOOLEAN | 否 | - |
| `visual_output_moderation` | 对输出图像启用视觉内容审核。此参数仅在 `moderation` 设置为 `"true"` 时可用。默认值：`True`。 | BOOLEAN | 否 | - |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。默认值：`0`。 | INT | 否 | 0 到 2147483647 |

**注意：** `visual_input_moderation` 和 `visual_output_moderation` 参数依赖于 `moderation` 参数。它们仅在 `moderation` 设置为 `"true"` 时生效。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `image` | 已处理并移除背景后的图像。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/zh.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
