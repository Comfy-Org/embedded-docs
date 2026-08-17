# Sonilo 文本生成音乐

Sonilo Text to Music 节点使用 Sonilo 的 AI 模型，根据文本描述生成音乐。您提供一个描述所需音乐的提示词，节点会向 Sonilo 服务发送请求以创建音频文件。您还可以指定生成音乐的目标时长。

## 输入
| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用于描述要生成音乐的文本提示词。必须包含 1 到 1000 个字符。 | STRING | 是 | 1 to 1000 characters |
| `duration` | 目标时长（秒）。最大：6 分钟。默认值：30。 | INT | 否 | 1 to 360 |
| `seed` | 用于可复现性的种子。目前被 Sonilo 服务忽略，但为保持图一致性而保留。默认值：0。 | INT | 否 | 0 to 18446744073709551615 |

**注意：** `seed` 输入用于工作流一致性，但当前不影响 Sonilo 服务的输出。

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `audio` | 生成的音乐音频文件。 | AUDIO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/zh.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
