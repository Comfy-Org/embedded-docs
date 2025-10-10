> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/zh.md)

{heading_overview}

此节点为编辑模型设置引导隐变量。它接收条件数据和一个可选的隐变量输入，然后修改条件数据以包含参考隐变量信息。如果模型支持，您可以链接多个 ReferenceLatent 节点来设置多个参考图像。

{heading_inputs}

| 参数名 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 将被修改以包含参考隐变量信息的条件数据 |
| `latent` | LATENT | 否 | - | 用作编辑模型参考的可选隐变量数据 |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | CONDITIONING | 包含参考隐变量信息的已修改条件数据 |