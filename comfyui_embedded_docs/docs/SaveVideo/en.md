> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/en.md)

The SaveVideo node saves input video content to your ComfyUI output directory. It allows you to specify the filename prefix, video format, and codec for the saved file. The node automatically handles file naming with counter increments and can include workflow metadata in the saved video.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Yes | - | The video to save. |
| `filename_prefix` | STRING | No | - | The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes (default: "video/ComfyUI"). |
| `format` | COMBO | No | `"auto"`<br>`"mp4"`<br>`"webm"`<br>`"mkv"`<br>`"gif"` | The format to save the video as (default: "auto"). |
| `codec` | COMBO | No | `"auto"`<br>`"h264"`<br>`"h265"`<br>`"vp9"`<br>`"av1"`<br>`"prores"` | The codec to use for the video (default: "auto"). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| *No outputs* | - | This node does not return any output data. |

---
**Source fingerprint (SHA-256):** `506ddc8820924688cccb9fd838ff9c0f5217a38f708f28f15a060be9325cea61`
