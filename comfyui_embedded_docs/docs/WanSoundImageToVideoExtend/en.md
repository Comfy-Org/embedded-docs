# WanSoundImageToVideoExtend

The WanSoundImageToVideoExtend node extends an existing video latent by generating additional frames, optionally guided by audio, a reference image, and a control video. It takes a starting video latent and produces a longer video sequence, using the provided conditioning and audio cues to influence the new content.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positive conditioning prompts that guide what the video should include | CONDITIONING | Yes | - |
| `negative` | Negative conditioning prompts that specify what the video should avoid | CONDITIONING | Yes | - |
| `vae` | Variational Autoencoder used for encoding and decoding video frames | VAE | Yes | - |
| `length` | Total number of frames to generate for the video sequence (default: 77, step: 4) | INT | Yes | 1 to MAX_RESOLUTION |
| `video_latent` | Initial video latent representation that serves as the starting point for extension. The width, height, batch size, and frame offset are derived from this latent. The last 19 frames of this latent are also used as reference motion for the new sequence. | LATENT | Yes | - |
| `audio_encoder_output` | Optional audio embeddings that can influence video generation based on sound characteristics. When provided, the audio is interpolated and used to create an audio embedding bucket that is added to the conditioning. | AUDIO_ENCODER_OUTPUT | No | - |
| `ref_image` | Optional reference image that provides visual guidance for the video generation. The image is upscaled to match the target dimensions and encoded into a latent, which is then added to both positive and negative conditioning. Only the first image of the batch is used. | IMAGE | No | - |
| `control_video` | Optional control video that can guide the motion and style of the generated video. The video is upscaled, encoded, and added to both positive and negative conditioning. The control video is truncated to the specified `length`. | IMAGE | No | - |

Note: When `audio_encoder_output` is provided, the audio embeddings are added to the positive conditioning, while the negative conditioning receives the same embeddings set to zero. The frame offset derived from `video_latent` determines where in the audio sequence the new frames begin. If the audio sequence does not contain enough frames to cover the requested extension, no audio conditioning is applied.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | Processed positive conditioning with video context applied, including audio embeddings, reference latents, reference motion, and control video if provided | CONDITIONING |
| `negative` | Processed negative conditioning with video context applied, including audio embeddings (zeroed out), reference latents, reference motion, and control video if provided | CONDITIONING |
| `latent` | Generated video latent representation containing the extended video sequence, initialized as zeros with dimensions derived from the input `video_latent` and the target `length` | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/en.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
