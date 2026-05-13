> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/zh.md)

## 概述

Vidu 文本转视频生成节点可根据文本描述创建视频。它利用 Vidu 视频生成模型，将您的文本提示转换为视频内容，并支持自定义时长、宽高比和视觉风格等设置。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 说明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `viduq1` | 模型名称 |
| `prompt` | STRING | 是 | - | 用于视频生成的文本描述 |
| `duration` | INT | 否 | 5-5 | 输出视频的时长（秒），默认值：5 |
| `seed` | INT | 否 | 0-2147483647 | 视频生成的随机种子（0 表示随机），默认值：0 |
| `aspect_ratio` | COMBO | 否 | `16:9`<br>`9:16`<br>`1:1` | 输出视频的宽高比 |
| `resolution` | COMBO | 否 | `1080p` | 支持的分辨率可能因模型和时长而异 |
| `movement_amplitude` | COMBO | 否 | `auto`<br>`small`<br>`medium`<br>`large` | 画面中物体的运动幅度 |

**注意：** `prompt` 字段为必填项，不能为空。`duration` 参数当前固定为 5 秒。

## 输出

| 输出名称 | 数据类型 | 说明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根据文本提示生成的视频 |

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
