# Save Video

The Save Video node saves the input video to your ComfyUI output directory. You can choose the file name prefix, the container format, the video codec, and encoding options such as quality and color space. The node automatically handles file naming with counter increments and can embed workflow metadata in the saved file.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `video` | The video to save. | VIDEO | Yes | - |
| `filename_prefix` | The prefix for the file to save. This may include formatting information such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%` to include values from nodes (default: "video/ComfyUI"). | STRING | Yes | - |
| `format` | The output container. Auto preserves the source container when possible; MP4, MKV, and WebM select a specific container (default: "auto"). | DYNAMIC_COMBO | Yes | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | The output video codec. Auto preserves a compatible source stream. H.264 and AV1 re-encoding support SDR, HDR (HLG), and HDR PQ. Appears when a format is selected (default: "auto"). | DYNAMIC_COMBO | No | `"auto"`<br>`"h264"`<br>`"av1"` |

### H.264 Inputs

These inputs appear when `codec` is `"h264"`. This codec is available with the `auto`, `mp4`, and `mkv` formats.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic preserves compatible H.264 streams. Re-encode applies custom encoding options. | DYNAMIC_COMBO | No | `"auto"`<br>`"re-encode"` |
| `crf` | Lower values produce higher quality and larger files. Appears when `encoding` is `"re-encode"` (default: 23.0). | FLOAT | No | 0.0 to 51.0 |
| `color_space` | Auto uses sRGB for videos created from images and preserves recognized colors on loaded videos. sRGB writes SDR BT.709/sRGB. HDR writes 10-bit BT.2020/HLG; HDR PQ writes BT.2020/PQ. Other input pixels must already use the selected color space. Appears when `encoding` is `"re-encode"` (default: "auto"). | COMBO | No | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### AV1 Inputs

These inputs appear when `codec` is `"av1"`. This codec is available with the `auto`, `mp4`, `mkv`, and `webm` formats.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `encoding` | Automatic preserves compatible AV1 streams. Re-encode applies custom encoding options. | DYNAMIC_COMBO | No | `"auto"`<br>`"re-encode"` |
| `crf` | Lower values produce higher quality and larger files. Appears when `encoding` is `"re-encode"` (default: 30.0). | FLOAT | No | 0.0 to 63.0 |
| `color_space` | Auto uses sRGB for videos created from images and preserves recognized colors on loaded videos. sRGB writes SDR BT.709/sRGB. HDR writes 10-bit BT.2020/HLG; HDR PQ writes BT.2020/PQ. Other input pixels must already use the selected color space. Appears when `encoding` is `"re-encode"` (default: "auto"). | COMBO | No | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Note: The `webm` format only supports the `auto` and `av1` codecs. When `format` is `"auto"`, the source container is preserved when possible. When `color_space` is `"auto"`, no explicit color space is applied and the color space is determined automatically.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `video` | The input video, unchanged. | VIDEO |
| `ui` | A preview of the saved video file, including the file path and subfolder information for display in the UI. | PREVIEW_VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/en.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
