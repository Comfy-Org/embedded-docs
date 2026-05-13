> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/zh.md)

根据文本提示和多种生成参数生成视频。此节点通过 PixVerse API 创建视频内容，支持控制宽高比、质量、时长、运动风格等。

## 输入

| 参数 | 数据类型 | 是否必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 视频生成的提示词（默认值：""） |
| `aspect_ratio` | COMBO | 是 | PixverseAspectRatio 中的选项 | 生成视频的宽高比 |
| `quality` | COMBO | 是 | PixverseQuality 中的选项 | 视频质量设置（默认值：PixverseQuality.res_540p） |
| `duration_seconds` | COMBO | 是 | PixverseDuration 中的选项 | 生成视频的时长（秒） |
| `motion_mode` | COMBO | 是 | PixverseMotionMode 中的选项 | 视频生成的运动风格 |
| `seed` | INT | 是 | 0 到 2147483647 | 视频生成的随机种子（默认值：0） |
| `negative_prompt` | STRING | 否 | - | 对图像中不希望出现的元素的可选文本描述（默认值：""） |
| `pixverse_template` | CUSTOM | 否 | - | 用于影响生成风格的可选模板，由 PixVerse 模板节点创建 |

**注意：** 使用 1080p 质量时，运动模式会自动设置为普通，时长限制为 5 秒。对于非 5 秒的时长，运动模式也会自动设置为普通。

## 输出

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的视频文件 |

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
