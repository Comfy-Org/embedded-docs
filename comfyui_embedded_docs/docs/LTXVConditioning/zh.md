> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/zh.md)

{heading_overview}

LTXVConditioning 节点用于为视频生成模型的正负条件输入添加帧率信息。该节点接收现有的条件数据，并将指定的帧率值应用于两组条件数据，使其适用于视频模型处理。

{heading_inputs}

| 参数 | 数据类型 | 必需 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 将接收帧率信息的正条件输入 |
| `negative` | CONDITIONING | 是 | - | 将接收帧率信息的负条件输入 |
| `frame_rate` | FLOAT | 否 | 0.0 - 1000.0 | 要应用于两组条件数据的帧率值（默认值：25.0） |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已应用帧率信息的正条件数据 |
| `negative` | CONDITIONING | 已应用帧率信息的负条件数据 |