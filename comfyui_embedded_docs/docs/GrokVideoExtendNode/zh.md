# Grok 视频扩展

Grok Video Extend 节点使用 AI 模型为现有视频创建无缝续接。您提供一段短视频和一段描述接下来应发生内容的文本提示，该节点将生成一段衔接原始视频的新视频片段。

## 输入

### 通用输入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | 用于视频扩展的模型。 | DYNAMIC_COMBO | 是 | `"grok-imagine-video"` |
| `prompt` | 描述视频接下来应发生内容的文本。 | STRING | 是 | N/A |
| `video` | 要扩展的源视频。MP4 格式，时长 2-15 秒。 | VIDEO | 是 | N/A |
| `seed` | 用于决定节点是否应重新运行的种子；无论种子为何，实际结果都是不确定的（默认值：0）。 | INT | 否 | 0 至 2147483647 |

### grok-imagine-video 输入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `duration` | 扩展的时长（秒）（默认值：8）。 | INT | 是 | 2 至 10 |

**参数约束：**
*   `video` 输入必须是长度在 2 至 15 秒之间的 MP4 文件，且文件大小不能超过 50MB。
*   `prompt` 必须至少包含一个字符（空白字符会被去除）。
*   `model` 参数是一个动态组合。选择 "grok-imagine-video" 选项后会显示嵌套的 `duration` 参数。

## 输出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | 新生成的视频扩展片段。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/zh.md)

---
**Source fingerprint (SHA-256):** `bfaf56dd12afab13c820345587db9ee871db87d60b8dc003f00f035513dbdf61`
