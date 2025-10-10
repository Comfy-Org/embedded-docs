> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/zh.md)

{heading_overview}

ConditioningStableAudio 节点为音频生成的正负条件输入添加时序信息。它设置开始时间和总时长参数，有助于控制音频内容的生成起始时间和持续时间。该节点通过附加音频特定的时序元数据来修改现有条件数据。

{heading_inputs}

| 参数 | 数据类型 | 必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 需要添加音频时序信息的正条件输入 |
| `negative` | CONDITIONING | 是 | - | 需要添加音频时序信息的负条件输入 |
| `seconds_start` | FLOAT | 是 | 0.0 至 1000.0 | 音频生成的起始时间（单位：秒，默认值：0.0） |
| `seconds_total` | FLOAT | 是 | 0.0 至 1000.0 | 音频生成的总时长（单位：秒，默认值：47.0） |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已应用音频时序信息的修改后正条件 |
| `negative` | CONDITIONING | 已应用音频时序信息的修改后负条件 |