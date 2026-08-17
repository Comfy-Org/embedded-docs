# 视频三角形CFG引导

VideoTriangleCFGGuidance 节点对视频模型应用三角形无分类器引导缩放模式。它使用三角波函数在最小 CFG 值与原始条件缩放之间振荡，随时间调整条件缩放。这形成了动态引导模式，有助于提高视频生成的一致性和质量。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `model` | 要应用三角形 CFG 引导的视频模型 | MODEL | 是 | - |
| `min_cfg` | 三角形模式的最小 CFG 缩放值（默认值：1.0） | FLOAT | 是 | 0.0 - 100.0 |

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `model` | 应用了三角形 CFG 引导后的修改后模型 | MODEL |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
