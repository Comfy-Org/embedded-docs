# 随机噪波

RandomNoise 节点根据种子值生成随机噪声模式。它创建可复现的噪声，可用于各种图像处理和生成任务。相同的种子始终会产生相同的噪声模式，从而确保多次运行结果一致。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `noise_seed` | 用于生成随机噪声模式的种子值（默认值：0）。相同的种子始终会产生相同的噪声输出。已启用生成后控制，允许种子值在每次生成后被随机化、固定、递增或递减。 | INT | 是 | 0 to 18446744073709551615 |

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `noise` | 根据提供的种子值生成的随机噪声模式。 | NOISE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/zh.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
