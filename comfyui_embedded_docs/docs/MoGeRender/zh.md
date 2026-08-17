# MoGe 渲染

## 概述
此节点接收一个 `MOGE_GEOMETRY` 数据包（由 MoGe 深度/法线估计节点生成），并将其渲染为标准图像格式。您可以选择输出深度图、彩色深度图、法线图或蒙版。

## 输入
| 参数 | 描述 | 数据类型 | 是否必填 | 范围 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 来自 MoGe 估计节点的几何数据包。 | MOGE_GEOMETRY | 是 | N/A |
| `output` | 要从几何数据渲染的图像类型。DirectX 与 OpenGL 控制法线图绿色通道的约定。DirectX：绿色 = -Y 向下（Unreal）。OpenGL：绿色 = +Y 向上（Blender、Substance、Unity、glTF）。（默认：`"depth"`） | COMBO | 是 | `"depth"`<br>`"depth_colored"`<br>`"normal_opengl"`<br>`"normal_directx"`<br>`"mask"` |

**注意：** 所选的 `output` 模式决定了 `moge_geometry` 中必须存在哪些数据：
- `depth` 和 `depth_colored` 需要深度数据。深度会使用 0.1/99.9 百分位裁剪转换为归一化视差（1/depth）图。
- `normal_opengl` 和 `normal_directx` 需要法线数据，或可从中推导出法线的点数据。如果两者均不存在，节点将引发错误。
- `mask` 需要蒙版数据。

## 输出
| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| IMAGE | 以一批 RGB 张量形式呈现的渲染图像。内容取决于 `output` 模式：灰度深度图、彩色深度图、法线图或蒙版。 | IMAGE |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeRender/zh.md)

---
**Source fingerprint (SHA-256):** `ca602f7a7d6eb1b1d00986459621d94ecf9331266ff1d3ce7bb759d24448a346`
