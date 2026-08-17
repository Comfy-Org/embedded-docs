# WanAnimateToVideo

This experimental node prepares Wan video generation by combining a reference image with optional pose, face, and background videos. It builds conditioning data and an empty latent video tensor for subsequent generation, and it returns frame-offset information that helps extend existing videos in chunks.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning for guiding the generation toward desired content. | CONDITIONING | Yes | - |
| `negative` | Negative conditioning for steering the generation away from unwanted content. | CONDITIONING | Yes | - |
| `vae` | VAE model used for encoding and decoding image data. | VAE | Yes | - |
| `width` | Output video width in pixels (default: 832, step: 16). | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | Output video height in pixels (default: 480, step: 16). | INT | Yes | 16 to MAX_RESOLUTION |
| `length` | Number of frames to generate (default: 77, step: 4). | INT | Yes | 1 to MAX_RESOLUTION |
| `batch_size` | Number of videos to generate in one batch (default: 1). | INT | Yes | 1 to 4096 |
| `clip_vision_output` | Optional CLIP vision model output used as additional conditioning for both positive and negative conditioning. | CLIP_VISION_OUTPUT | No | - |
| `reference_image` | Reference image used as the starting point for generation. If not provided, a black image (all zeros) is used. | IMAGE | No | - |
| `face_video` | Video providing facial expression guidance. When processed, it is resized to 512x512 and normalized to the range -1.0 to 1.0. | IMAGE | No | - |
| `pose_video` | Video providing pose and motion guidance. If it is shorter than `length`, it is padded with its last frame. | IMAGE | No | - |
| `continue_motion_max_frames` | Maximum number of frames to continue from a previous motion. Only the last this many frames of `continue_motion` are used (default: 5, step: 4). | INT | Yes | 1 to MAX_RESOLUTION |
| `background_video` | Background video to composite with the generated content. | IMAGE | No | - |
| `character_mask` | Mask defining character regions for selective processing. If the mask has only one frame, it is repeated across all frames. | MASK | No | - |
| `continue_motion` | Previous motion sequence used to maintain temporal consistency when extending a video. Only the last `continue_motion_max_frames` frames are used. | IMAGE | No | - |
| `video_frame_offset` | The amount of frames to seek in all the input videos. Used for generating longer videos by chunk. Connect to the video_frame_offset output of the previous node for extending a video. (default: 0, step: 1) | INT | Yes | 0 to MAX_RESOLUTION |

**Parameter Constraints:**

- When `pose_video` is provided, a shorter pose video is padded with its last frame to match `length`. The source contains a `trim_to_pose_video` flag, currently disabled, that would instead shorten the output to match the pose video length.
- `face_video` is resized to 512x512 and normalized to the range -1.0 to 1.0.
- `continue_motion` is limited to the last `continue_motion_max_frames` frames. When `continue_motion` is used, `video_frame_offset` is reduced by the number of frames taken, but never below 0.
- Input videos (`face_video`, `pose_video`, `background_video`, `character_mask`) are offset by `video_frame_offset`. If the offset is greater than or equal to their length, the input is ignored, except for a single-frame `character_mask`, which is always repeated.
- When `clip_vision_output` is provided, it is applied to both positive and negative conditioning.
- If `reference_image` is not provided, a black image (all zeros) is used as the reference.
- If `continue_motion` is not provided, gray frames with pixel value 0.5 are used for the motion portion.
- `width` and `height` use a step of 16; the corresponding latent dimensions are `width / 8` and `height / 8`.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Modified positive conditioning that always includes the concatenated latent image and concatenated mask. If `clip_vision_output`, `pose_video`, or `face_video` are provided, their values are also added. | CONDITIONING |
| `negative` | Modified negative conditioning that always includes the concatenated latent image and concatenated mask. If `clip_vision_output`, `pose_video`, or `face_video` are provided, their values are also added; the face video pixels are set to -1.0. | CONDITIONING |
| `latent` | Empty latent tensor initialized to zeros, with shape `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Number of latent frames to trim from the beginning, corresponding to the reference image latent frames. | INT |
| `trim_image` | Number of image frames to trim from the beginning, corresponding to reference motion frames. | INT |
| `video_frame_offset` | Updated frame offset for chunked video generation, equal to the adjusted input offset plus the generated length. | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/en.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
