# Bria 视频绿幕

此节点使用 Bria API 将视频的背景替换为纯色色度键屏幕。它处理输入视频并返回一个新视频，其中原始背景已被移除并替换为均匀的绿色或蓝色屏幕颜色。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要处理的输入视频 | VIDEO | 是 | 视频文件 |
| `green_shade` | 应用于前景后方的纯色色度键色调：broadcast_green（#00B140）、chroma_green（#00FF00）或 blue_screen（#0000FF） | COMBO | 是 | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | Seed 用于控制节点是否重新运行；无论 seed 如何，结果都是非确定性的（默认值：0） | INT | 是 | 0 至 2147483647 |

**注意：** 输入视频的时长不得超过 60 秒。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `video` | 处理后的视频，原始背景已被替换为所选色度键色调，并以 MP4（H.264）视频形式返回 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/zh.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
