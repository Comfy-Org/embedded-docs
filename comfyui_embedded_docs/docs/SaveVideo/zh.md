# 保存视频

Save Video 节点将输入视频保存到您的 ComfyUI 输出目录。您可以选择文件名前缀、容器格式、视频编解码器以及质量和色彩空间等编码选项。该节点会自动处理带计数器递增的文件命名，并可在保存的文件中嵌入工作流元数据。

## 输入

### 通用输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `视频` | 要保存的视频。 | VIDEO | 是 | - |
| `文件名前缀` | 要保存文件的前缀。可包含格式化信息，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以包含来自节点的值（默认值："video/ComfyUI"）。 | STRING | 是 | - |
| `格式` | 输出容器。Auto 尽可能保留源容器；MP4、MKV 和 WebM 选择特定容器（默认值："auto"）。 | DYNAMIC_COMBO | 是 | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `编码器` | 输出视频编解码器。Auto 保留兼容的源流。H.264 和 AV1 重新编码支持 SDR、HDR (HLG) 和 HDR PQ。当选择了格式时出现（默认值："auto"）。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 输入

当 `codec` 为 `"h264"` 时，这些输入会出现。此编解码器可用于 `auto`、`mp4` 和 `mkv` 格式。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `encoding` | 自动保留兼容的 H.264 流。重新编码则应用自定义编码选项。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 数值越低，质量越高，文件越大。当 `encoding` 为 `"re-encode"` 时出现（默认值：23.0）。 | FLOAT | 否 | 0.0 到 51.0 |
| `color_space` | Auto 对从图像创建的视频使用 sRGB，并保留已加载视频上可识别的颜色。sRGB 写入 SDR BT.709/sRGB。HDR 写入 10-bit BT.2020/HLG；HDR PQ 写入 BT.2020/PQ。其他输入像素必须已使用所选色彩空间。当 `encoding` 为 `"re-encode"` 时出现（默认值："auto"）。 | COMBO | 否 | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### AV1 输入

当 `codec` 为 `"av1"` 时，这些输入会出现。此编解码器可用于 `auto`、`mp4`、`mkv` 和 `webm` 格式。

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
| --- | --- | --- | --- | --- |
| `encoding` | 自动保留兼容的 AV1 流。重新编码则应用自定义编码选项。 | DYNAMIC_COMBO | 否 | `"auto"`<br>`"re-encode"` |
| `crf` | 数值越低，质量越高，文件越大。当 `encoding` 为 `"re-encode"` 时出现（默认值：30.0）。 | FLOAT | 否 | 0.0 到 63.0 |
| `color_space` | Auto 对从图像创建的视频使用 sRGB，并保留已加载视频上可识别的颜色。sRGB 写入 SDR BT.709/sRGB。HDR 写入 10-bit BT.2020/HLG；HDR PQ 写入 BT.2020/PQ。其他输入像素必须已使用所选色彩空间。当 `encoding` 为 `"re-encode"` 时出现（默认值："auto"）。 | COMBO | 否 | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

注意：`webm` 格式仅支持 `auto` 和 `av1` 编解码器。当 `format` 为 `"auto"` 时，尽可能保留源容器。当 `color_space` 为 `"auto"` 时，不应用显式色彩空间，而由系统自动确定色彩空间。

## 输出

| 输出名称 | 描述 | 数据类型 |
| --- | --- | --- |
| `video` | 输入视频，未做更改。 | VIDEO |
| `ui` | 已保存视频文件的预览，包括文件路径和子文件夹信息，用于在界面中显示。 | PREVIEW_VIDEO |

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
