> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/zh.md)

{heading_overview}

此节点通过将 CLIP 模型的引导嵌入功能完全禁用，适用于 Flux 及类似模型。它接收条件数据作为输入，并通过将引导组件设置为 None 来移除该功能，从而在生成过程中有效关闭基于引导的条件控制。

{heading_inputs}

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 需要处理并移除引导功能的条件数据 |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 已禁用引导功能的修改后条件数据 |