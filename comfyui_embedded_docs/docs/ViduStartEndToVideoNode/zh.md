> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/zh.md)

# Vidu 起始帧到结束帧视频生成节点

Vidu 起始帧到结束帧视频生成节点通过在起始帧和结束帧之间生成帧来创建视频。它使用文本提示来引导视频生成过程，并支持具有不同分辨率和运动设置的各种视频模型。该节点在处理前会验证起始帧和结束帧具有兼容的宽高比。

## 输入

| 参数 | 数据类型 | 是否必需 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"viduq1"` | 模型名称 |
| `first_frame` | IMAGE | 是 | - | 起始帧 |
| `end_frame` | IMAGE | 是 | - | 结束帧 |
| `prompt` | STRING | 否 | - | 用于视频生成的文本描述 |
| `duration` | INT | 否 | 5-5 | 输出视频的时长（秒）（默认值：5，固定为5秒） |
| `seed` | INT | 否 | 0-2147483647 | 视频生成的种子（0表示随机）（默认值：0） |
| `resolution` | COMBO | 否 | `"1080p"` | 支持的值可能因模型和时长而异（默认值："1080p"） |
| `movement_amplitude` | COMBO | 否 | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | 画面中物体的运动幅度（默认值："auto"） |

**注意：** 起始帧和结束帧必须具有兼容的宽高比（验证容差为 min_rel=0.8，max_rel=1.25）。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的视频文件 |

---
**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`
