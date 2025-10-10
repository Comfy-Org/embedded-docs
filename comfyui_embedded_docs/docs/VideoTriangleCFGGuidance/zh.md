> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh.md)

{heading_overview}

VideoTriangleCFGGuidance 节点对视频模型应用三角形无分类器引导缩放模式。它使用在最小 CFG 值和原始条件缩放值之间振荡的三角波函数，随时间调整条件缩放比例。这种动态引导模式有助于提升视频生成的一致性和质量。

{heading_inputs}

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要应用三角形 CFG 引导的视频模型 |
| `min_cfg` | FLOAT | 是 | 0.0 - 100.0 | 三角形模式的最小 CFG 缩放值（默认值：1.0） |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 应用了三角形 CFG 引导的修改后模型 |