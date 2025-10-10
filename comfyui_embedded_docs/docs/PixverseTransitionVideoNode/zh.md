> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/zh.md)

基于提示词和输出尺寸生成视频。此节点使用 PixVerse API 在两个输入图像之间创建过渡视频，允许您指定视频质量、时长、运动风格和生成参数。

## 输入参数

| 参数 | 数据类型 | 必填 | 取值范围 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `first_frame` | IMAGE | 是 | - | 视频过渡的起始图像 |
| `last_frame` | IMAGE | 是 | - | 视频过渡的结束图像 |
| `prompt` | STRING | 是 | - | 视频生成的提示词（默认：空字符串） |
| `quality` | COMBO | 是 | PixVerseQuality 枚举中可用的质量选项<br>默认：res_540p | 视频质量设置 |
| `duration_seconds` | COMBO | 是 | PixVerseDuration 枚举中可用的时长选项 | 视频时长（秒） |
| `motion_mode` | COMBO | 是 | PixVerseMotionMode 枚举中可用的运动模式选项 | 过渡的运动风格 |
| `seed` | INT | 是 | 0 到 2147483647 | 视频生成的随机种子（默认：0） |
| `negative_prompt` | STRING | 否 | - | 图像中不希望出现的元素的可选文本描述（默认：空字符串） |

**注意：** 使用 1080p 质量时，运动模式会自动设置为 normal，时长限制为 5 秒。对于非 5 秒的时长，运动模式也会自动设置为 normal。

## 输出结果

| 输出名称 | 数据类型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的过渡视频 |