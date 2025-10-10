> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/zh.md)

{heading_overview}

Pika Image to Video 节点将图像和文本提示发送到 Pika API 2.2 版本以生成视频。它根据提供的描述和设置将输入图像转换为视频格式。该节点负责处理 API 通信，并返回生成的视频作为输出。

{heading_inputs}

| 参数 | 数据类型 | 必需 | 范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要转换为视频的图像 |
| `prompt_text` | STRING | 是 | - | 指导视频生成的文本描述 |
| `negative_prompt` | STRING | 是 | - | 描述视频中应避免内容的文本 |
| `seed` | INT | 是 | - | 用于可重现结果的随机种子值 |
| `resolution` | STRING | 是 | - | 输出视频分辨率设置 |
| `duration` | INT | 是 | - | 生成视频的长度（以秒为单位） |

{heading_outputs}

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的视频文件 |