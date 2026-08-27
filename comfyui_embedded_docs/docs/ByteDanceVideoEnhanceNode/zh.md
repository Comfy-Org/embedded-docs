# ByteDanceVideoEnhanceNode

此节点使用 ByteDance vCube 对视频进行放大和修复。它可以将分辨率提升至 8K，去除压缩伪影和噪点，增强色彩和清晰度，并可选择进行帧插值以获得更高帧率。视频将上传到 vCube 服务，使用所选增强预设进行处理，并作为增强后的视频文件返回。

## 输入

### 通用输入

始终显示以下输入。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|------|------|---------|------|------|
| `video` | 要增强的视频。源分辨率最高必须为 2560x1440（2K）；输出大小由分辨率输入设置。 | VIDEO | 是 | 最大 2560x1440（2K） |
| `tool_version` | 'standard' 在速度和质量之间取得平衡，包含 10 多种增强算法。'professional' 使用 30 多种算法进行电影级修复，耗时约 3 倍，费用高 10 倍。 | DYNAMIC_COMBO | 是 | "standard"<br>"professional" |
| `resolution` | 输出分辨率。短边设置为所选级别，长边保持源纵横比。'source' 保持源大小，'custom' 以像素为单位设置短边。宽高比超过约 2.2:1 的源按高一档分辨率计费。 | DYNAMIC_COMBO | 是 | "720p"<br>"1080p"<br>"2k"<br>"4k"<br>"8k"<br>"source"<br>"custom" |
| `fps` | 输出帧率。高于源帧率可启用 AI 帧插值；低于源帧率则丢帧。'source' 保持源帧率，最高 120 fps。超过 30 fps 费用为 2 倍，超过 60 fps 为 4 倍。（默认值："source"） | COMBO | 是 | "source"（默认）<br>最高 120 fps 的数字帧率 |
| `bitrate_level` | 交付文件的目标比特率，按输出分辨率和帧率缩放。（默认值："medium"） | COMBO | 是 | "low"<br>"medium"<br>"high" |

### 标准输入

当 `tool_version` 设置为 "standard" 时显示。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|------|------|---------|------|------|
| `scene` | 针对内容调校的预设：'aigc' 用于 AI 生成片段，'common' 用于普通视频，'ugc' 用于压缩的手机短片，'short_series' 用于含人脸剧集，'old_film' 用于有划痕或闪烁的档案素材。（默认值："aigc"） | COMBO | 是 | "aigc"<br>"common"<br>"ugc"<br>"short_series"<br>"old_film" |
| `enhance_style` | 'hd' 应用更锐利的增强效果；'natural' 降低强度，呈现更柔和、更少锐化的外观。（默认值："hd"） | COMBO | 是 | "hd"<br>"natural" |

### 专业输入

当 `tool_version` 设置为 "professional" 时显示。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|------|------|---------|------|------|
| `enhance_style` | 'hd' 应用更锐利的增强效果；'natural' 降低强度，呈现更柔和、更少锐化的外观。（默认值："hd"） | COMBO | 是 | "hd"<br>"natural" |

### 自定义分辨率输入

当 `resolution` 设置为 "custom" 时显示。

| 参数 | 描述 | 数据类型 | 必填 | 范围 |
|------|------|---------|------|------|
| `short_side` | 输出短边的像素值；长边保持源纵横比。（默认值：1080） | INT | 是 | 默认 1080；受 vCube 最小和最大短边限制约束 |

### 注意事项

- 源视频最大必须为 2560x1440（2K）。大于此分辨率的视频将被拒绝，必须在增强前缩小。
- 源视频时长受 vCube 服务支持的最大时长限制。
- 当 `tool_version` 为 "standard" 时，`scene` 和 `enhance_style` 均可用。为 "professional" 时，仅 `enhance_style` 可用。
- 当 `resolution` 为 "custom" 时，必须提供 `short_side` 值。分辨率预设和 "source" 不使用 `short_side`。
- 当 `resolution` 为 "source" 时，输出保持源分辨率。
- 当 `fps` 为 "source" 时，输出帧率与源帧率一致，最高 120 fps。

## 输出

| 输出名称 | 描述 | 数据类型 |
|---------|------|---------|
| `video` | 增强后的视频，已按请求的分辨率和帧率进行放大和修复。 | VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/zh.md)

---
**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`
