# WanSCAILToVideo

The WanSCAILToVideo node prepares conditioning and an empty latent space for video generation. It processes optional inputs like reference images, pose videos, CLIP vision outputs, and previous frame chunks, embedding them into the positive and negative conditioning for a video model. The node outputs the modified conditioning and a blank latent tensor of the specified video dimensions.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | The positive conditioning input. | CONDITIONING | Yes | - |
| `negative` | The negative conditioning input. | CONDITIONING | Yes | - |
| `vae` | The VAE model used for encoding images and video frames. | VAE | Yes | - |
| `width` | The width of the output video in pixels (default: 512). Adjustable in steps of 32. | INT | Yes | 32 to MAX_RESOLUTION |
| `height` | The height of the output video in pixels (default: 896). Adjustable in steps of 32. | INT | Yes | 32 to MAX_RESOLUTION |
| `length` | The number of frames in the video (default: 81). Adjustable in steps of 4 starting from 1. | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | The number of videos to generate in a batch (default: 1). | INT | Yes | 1 to 4096 |
| `pose_strength` | Strength of the pose latent (default: 1.0). | FLOAT | Yes | 0.0 to 10.0 |
| `pose_start` | Start step of the pose conditioning (default: 0.0). | FLOAT | Yes | 0.0 to 1.0 |
| `pose_end` | End step of the pose conditioning (default: 1.0). | FLOAT | Yes | 0.0 to 1.0 |
| `video_frame_offset` | Cumulative output frame this chunk begins at. Wire from the previous chunk's video_frame_offset output (default: 0). | INT | Yes | 0 to MAX_RESOLUTION |
| `previous_frame_count` | Tail frames of previous_frames to anchor. SCAIL-2 trained at 5 (81-frame chunks, 76-frame step) (default: 5). | INT | Yes | 1 to MAX_RESOLUTION |
| `pose_video` | Video used for pose conditioning. Will be downscaled to half the resolution of the main video. | IMAGE | No | - |
| `pose_video_mask` | SCAIL-2 only. Colored per-identity SAM3 mask video at the same resolution as pose_video. | IMAGE | No | - |
| `replacement_mode` | SCAIL-2 only. False = Animation Mode (pose_video_mask should have black background). True = Replacement Mode (pose_video_mask should have white background). Default: False. | BOOLEAN | No | - |
| `reference_image` | Reference image. The first image is the primary reference (composite all identities onto it). SCAIL-2: extra batch images are used as additional views (back view, close-up, occluded background), each needing a matching reference_image_mask in that identity's color. | IMAGE | No | - |
| `reference_image_mask` | SCAIL-2 only. Colored reference mask, batch matching reference_image (first = primary reference mask, rest = identity masks for the additional reference_image). | IMAGE | No | - |
| `clip_vision_output` | CLIP vision features for conditioning. Model is trained with stretch resize to aspect ratio. | CLIP_VISION_OUTPUT | No | - |
| `previous_frames` | SCAIL-2 only. Full decoded output of the previous chunk. Only the last previous_frame_count are used as the extension anchor. | IMAGE | No | - |

**Note:**

- The `pose_video` and `pose_video_mask` inputs are sliced starting at `video_frame_offset`; if the video has no frames beyond that offset, it is ignored. They are then truncated together to the shorter of the two and capped at `length` frames. The `pose_video` is downscaled to half the resolution of the main video before encoding.
- The `reference_image_mask` input only applies when `reference_image` is also provided. Each image in the `reference_image` batch is encoded individually as a single-frame latent reference. In Replacement Mode (`replacement_mode=True`), reference images are composited on a black background using the reference image mask as an alpha matte.
- When `clip_vision_output` is provided, it is applied to both positive and negative conditioning.
- When `previous_frames` is provided, only the last `previous_frame_count` frames are used as the extension anchor. The output latent is partially filled with the encoding of these frames, a noise mask is included in the latent output, and `video_frame_offset` is adjusted by subtracting the number of kept frames (never below 0).

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | The modified positive conditioning, potentially containing embedded reference image latents, CLIP vision output, pose video latents, driving masks, reference masks, or previous frame latents. | CONDITIONING |
| `negative` | The modified negative conditioning, potentially containing embedded reference image latents, CLIP vision output, pose video latents, driving masks, reference masks, or previous frame latents. | CONDITIONING |
| `latent` | An empty latent tensor of shape `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. When previous_frames is provided, the latent is partially filled with encoded previous frames and a noise mask is included. | LATENT |
| `video_frame_offset` | Adjusted offset + length. Wire into the next chunk for sequential video generation. | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/en.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
