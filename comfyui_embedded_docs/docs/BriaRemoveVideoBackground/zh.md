# Bria 移除视频背景

此节点使用 Bria AI 服务从视频中移除背景。它处理输入视频，并将原始背景替换为您选择的纯色。该操作通过外部 API 执行，结果以新视频文件的形式返回。

## 输入

| 参数 | 描述 | 数据类型 | 是否必填 | 取值范围 |
|-----------|-------------|-----------|----------|-------|
| `video` | 将从中移除背景的输入视频文件。 | VIDEO | 是 | 不适用 |
| `background_color` | 输出视频的背景颜色。 | COMBO | 是 | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `seed` | 种子控制节点是否应重新运行；无论种子如何，结果都是非确定性的。（默认值：0） | INT | 是 | 0 到 2147483647 |

**注意：** 输入视频的时长必须为 60 秒或更短。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `output` | 已处理过的视频文件，背景已被移除并替换为所选颜色。输出视频编码为 MP4（H.264）。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/zh.md)

---
**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`
