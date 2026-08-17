# Bria 移除视频背景（透明）

此节点使用 Bria 的 AI 服务移除视频背景，并返回抠出的帧以及 alpha 遮罩。将两个输出连接到合成节点，或将它们馈送到 Save WEBM 节点以写入透明视频。

## 输入
| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要处理的输入视频。最大时长为 60 秒。 | VIDEO | 是 | - |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是不确定的（默认值：0） | INT | 是 | 0 到 2147483647 |

## 输出
| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `images` | 移除背景后的视频帧 | IMAGE |
| `mask` | 视频帧的 alpha 遮罩，其中 1 表示透明 | MASK |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/zh.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
