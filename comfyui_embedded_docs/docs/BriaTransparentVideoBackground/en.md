# Bria Remove Video Background (Transparent)

This node removes the background from a video using Bria's AI service and returns the cut-out frames along with an alpha mask. Connect both outputs to a compositing node, or feed them to a Save WEBM node to write a transparent video.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `video` | The input video to process. Maximum duration is 60 seconds. | VIDEO | Yes | - |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0) | INT | Yes | 0 to 2147483647 |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The video frames with the background removed | IMAGE |
| `mask` | The alpha mask for the video frames, where 1 means transparent | MASK |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/en.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
