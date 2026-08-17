# WanTrackToVideo

The WanTrackToVideo node uses motion tracking data (point trajectories) to guide video generation. It processes the tracks, optionally combines them with a starting image, and produces conditioned positive and negative outputs plus a latent tensor for the Wan video model. When no valid tracks are provided, it falls back to standard image-to-video conversion.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning for video generation | CONDITIONING | Yes | - |
| `negative` | Negative conditioning for video generation | CONDITIONING | Yes | - |
| `vae` | VAE model used for encoding video frames | VAE | Yes | - |
| `tracks` | JSON-formatted tracking data as a multiline string (default: "[]") | STRING | Yes | - |
| `width` | Output video width in pixels (default: 832, step: 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | Output video height in pixels (default: 480, step: 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `length` | Number of frames in the output video (default: 81, step: 4) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | Number of videos to generate simultaneously (default: 1) | INT | Yes | 1 to 4096 |
| `temperature` | Advanced temperature parameter for motion patching (default: 220.0, step: 0.1) | FLOAT | Yes | 1.0 to 1000.0 |
| `topk` | Advanced top-k value for motion patching (default: 2) | INT | Yes | 1 to 10 |
| `start_image` | Starting image used for the first frame of video generation | IMAGE | Yes | - |
| `clip_vision_output` | CLIP vision output for additional conditioning | CLIP_VISION_OUTPUT | No | - |

**Notes:**
- The `tracks` input expects a JSON string or list of JSON strings containing point tracking data. If `tracks` is empty or cannot be parsed, the node falls back to WanImageToVideo behavior.
- When `start_image` is present, it is resized to match `width` and `height` and used as the first frame of the video sequence.
- When `clip_vision_output` is provided, it is added to both the positive and negative conditioning.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning with motion track and optional image information applied | CONDITIONING |
| `negative` | Negative conditioning with motion track and optional image information applied | CONDITIONING |
| `latent` | Zero-filled latent tensor sized for the requested video dimensions, length, and batch size | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/en.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
