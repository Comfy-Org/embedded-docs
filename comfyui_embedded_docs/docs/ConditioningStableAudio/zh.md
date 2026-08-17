# StableAudio条件

ConditioningStableAudio 节点会为音频生成的正向和负向 conditioning 输入添加时序信息。它设置开始时间和总时长参数，用于控制音频内容应在何时开始生成以及生成的持续时间。该节点通过附加音频特定的时序元数据来修改现有的 conditioning 数据。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `positive` | 要使用音频时序信息修改的正向 conditioning 输入 | CONDITIONING | Yes | - |
| `negative` | 要使用音频时序信息修改的负向 conditioning 输入 | CONDITIONING | Yes | - |
| `seconds_start` | 音频生成的开始时间（秒）（默认值：0.0） | FLOAT | Yes | 0.0 to 1000.0 |
| `seconds_total` | 音频生成的总时长（秒）（默认值：47.0） | FLOAT | Yes | 0.0 to 1000.0 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 已应用音频时序信息的修改后正向 conditioning | CONDITIONING |
| `negative` | 已应用音频时序信息的修改后负向 conditioning | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/zh.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
