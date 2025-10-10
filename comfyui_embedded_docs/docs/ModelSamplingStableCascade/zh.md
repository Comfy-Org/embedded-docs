> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh.md)

{heading_overview}

ModelSamplingStableCascade 节点通过使用偏移值调整采样参数，对模型应用稳定级联采样。它会创建一个经过修改的输入模型版本，该版本具有用于稳定级联生成的自定义采样配置。

{heading_inputs}

| 参数 | 数据类型 | 必需 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要应用稳定级联采样的输入模型 |
| `shift` | FLOAT | 是 | 0.0 - 100.0 | 应用于采样参数的偏移值（默认值：2.0） |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 应用了稳定级联采样后的修改模型 |