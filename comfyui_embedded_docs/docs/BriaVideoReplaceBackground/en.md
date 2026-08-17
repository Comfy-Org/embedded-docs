# Bria Video Replace Background

Replace a video's background with a supplied image or video using Bria. The output keeps the foreground's resolution and frame rate; a background with a different aspect ratio is stretched to fit, so match it for undistorted results.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `video` | Foreground video whose background is replaced. | VIDEO | Yes | - |
| `background_image` | Background image to composite behind the foreground. Provide either a background image or a background video, not both. | IMAGE | No | - |
| `background_video` | Background video to composite behind the foreground. Provide either a background image or a background video, not both. | VIDEO | No | - |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0) | INT | Yes | 0 to 2147483647 |

**Note:** You must provide exactly one of `background_image` or `background_video` — not both and not neither. Both the foreground and background videos must be 60 seconds or shorter. If a background image is supplied, its alpha (transparency) channel is removed before upload.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `video` | The resulting video with the background replaced. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/en.md)

---
**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`
