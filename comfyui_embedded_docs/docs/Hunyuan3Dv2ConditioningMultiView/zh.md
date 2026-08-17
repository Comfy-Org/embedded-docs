# Hunyuan3Dv2条件多视角

Hunyuan3Dv2ConditioningMultiView 节点处理用于 3D 视频生成的多视角 CLIP 视觉嵌入。它接收可选的正面（front）、左面（left）、背面（back）和右面（right）视角嵌入，并在将每个提供的视角组合成单个 conditioning 序列之前，为每个视角添加位置编码。该节点从组合嵌入中输出正向 conditioning，并输出具有零值的负向 conditioning。

## 输入

| 参数 | 描述 | 数据类型 | 是否必需 | 范围 |
| --- | --- | --- | --- | --- |
| `front` | 前视图的 CLIP 视觉输出 | CLIP_VISION_OUTPUT | 否 | - |
| `left` | 左视图的 CLIP 视觉输出 | CLIP_VISION_OUTPUT | 否 | - |
| `back` | 后视图的 CLIP 视觉输出 | CLIP_VISION_OUTPUT | 否 | - |
| `right` | 右视图的 CLIP 视觉输出 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** 节点正常运行至少需要提供一个视角输入。节点仅处理包含有效 CLIP 视觉输出数据的视角。每个提供的视角根据其视角位置（正面、左面、背面、右面）接收位置编码，然后编码后的视图按相同顺序拼接。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `positive` | 包含具有位置编码的组合多视角嵌入的正向 conditioning | CONDITIONING |
| `negative` | 包含与正向 conditioning 形状相同的零值的负向 conditioning | CONDITIONING |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/zh.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
