# WanFirstLastFrameToVideo

The WanFirstLastFrameToVideo node creates video conditioning by combining start and end frames with text prompts. It generates a latent representation for video generation by encoding the first and last frames, applying masks to guide the generation process, and incorporating CLIP vision features when available. This node prepares both positive and negative conditioning for video models to generate coherent sequences between specified start and end points.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive text conditioning for guiding the video generation | CONDITIONING | Yes | - |
| `negative` | Negative text conditioning for guiding the video generation | CONDITIONING | Yes | - |
| `vae` | VAE model used for encoding images to latent space | VAE | Yes | - |
| `width` | Output video width (default: 832, step: 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | Output video height (default: 480, step: 16) | INT | Yes | 16 to MAX_RESOLUTION |
| `length` | Number of frames in the video sequence (default: 81, step: 4) | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | Number of videos to generate simultaneously (default: 1) | INT | Yes | 1 to 4096 |
| `clip_vision_start_image` | CLIP vision features extracted from the start image | CLIP_VISION_OUTPUT | No | - |
| `clip_vision_end_image` | CLIP vision features extracted from the end image | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Starting frame image for the video sequence | IMAGE | No | - |
| `end_image` | Ending frame image for the video sequence | IMAGE | No | - |

**Note:** When both `start_image` and `end_image` are provided, the node creates a video sequence that transitions between these two frames. The `start_image` is cropped to the first `length` frames, and the `end_image` is cropped to the last `length` frames before processing. If only one of them is provided, the missing side is filled with neutral gray frames. The mask is set to 0 where the start and end frames are present and 1 elsewhere. The `clip_vision_start_image` and `clip_vision_end_image` parameters are optional; when both are provided, their CLIP vision features are concatenated and applied to both positive and negative conditioning. When only one is provided, its features are used alone.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning with applied video frame encoding and CLIP vision features | CONDITIONING |
| `negative` | Negative conditioning with applied video frame encoding and CLIP vision features | CONDITIONING |
| `latent` | Empty latent tensor with dimensions matching the specified video parameters | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/en.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
