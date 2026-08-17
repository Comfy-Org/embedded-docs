# Save WEBM

The SaveWEBM node saves a sequence of images as a WEBM video file. It encodes the input images into a video using either the VP9 or AV1 codec with configurable frame rate and quality settings, and saves the file to the output directory. Prompt and workflow metadata are embedded in the video file when available.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | The sequence of images to encode into the video. RGBA images are saved with their alpha channel as transparency (vp9 codec only). | IMAGE | Yes | - |
| `filename_prefix` | Prefix for the output filename; a counter and the .webm extension are appended automatically (default: "ComfyUI") | STRING | No | - |
| `codec` | Video codec used for encoding | COMBO | Yes | "vp9"<br>"av1" |
| `fps` | Frame rate for the output video (default: 24.0) | FLOAT | No | 0.01-1000.0 |
| `crf` | Higher crf means lower quality with a smaller file size, lower crf means higher quality higher filesize (default: 32.0) | FLOAT | No | 0-63.0 |

**Alpha channel note:** The alpha channel of RGBA images is only preserved when using the vp9 codec. When using the av1 codec, the alpha channel is ignored and only the RGB data is encoded.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The input image sequence, passed through unchanged | IMAGE |
| `ui` | Video preview showing the saved WEBM file | PREVIEW |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/en.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
