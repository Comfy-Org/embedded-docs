> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/zh.md)

{heading_overview}

通过使用另一组跳过层的 CFG 负向提示来增强对细节结构的引导。这个通用版本的 SkipLayerGuidance 可用于所有 DiT 模型，其灵感来源于扰动注意力引导。原始实验性实现是为 SD3 创建的。

{heading_inputs}

| 参数 | 数据类型 | 必需 | 范围 | 描述 |
|------|-----------|------|------|-------------|
| `model` | MODEL | 是 | - | 要应用跳过层引导的模型 |
| `double_layers` | STRING | 是 | - | 要跳过的双块层的逗号分隔层号（默认："7, 8, 9"） |
| `single_layers` | STRING | 是 | - | 要跳过的单块层的逗号分隔层号（默认："7, 8, 9"） |
| `scale` | FLOAT | 是 | 0.0 - 10.0 | 引导缩放因子（默认：3.0） |
| `start_percent` | FLOAT | 是 | 0.0 - 1.0 | 引导应用的起始百分比（默认：0.01） |
| `end_percent` | FLOAT | 是 | 0.0 - 1.0 | 引导应用的结束百分比（默认：0.15） |
| `rescaling_scale` | FLOAT | 是 | 0.0 - 10.0 | 重新缩放因子（默认：0.0） |

**注意：** 如果 `double_layers` 和 `single_layers` 都为空（不包含任何层号），节点将返回原始模型而不应用任何引导。

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|----------|-----------|-------------|
| `model` | MODEL | 应用了跳过层引导的修改后模型 |