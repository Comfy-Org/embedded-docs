# WanSoundImageToVideo

The WanSoundImageToVideo node prepares video generation from images with optional audio conditioning. It takes positive and negative conditioning prompts along with a VAE model to build the conditioning inputs and an empty latent tensor, and can incorporate reference images, audio encoding, control videos, and motion references to guide the video generation process.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning prompts that guide what content should appear in the generated video | CONDITIONING | Yes | - |
| `negative` | Negative conditioning prompts that specify what content should be avoided in the generated video | CONDITIONING | Yes | - |
| `vae` | VAE model used for encoding and decoding the video latent representations | VAE | Yes | - |
| `width` | Width of the output video in pixels (default: 832, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION (step: 16) |
| `height` | Height of the output video in pixels (default: 480, must be divisible by 16) | INT | Yes | 16 to MAX_RESOLUTION (step: 16) |
| `length` | Number of frames in the generated video (default: 77, must be divisible by 4) | INT | Yes | 1 to MAX_RESOLUTION (step: 4) |
| `batch_size` | Number of videos to generate simultaneously (default: 1) | INT | Yes | 1 to 4096 |
| `audio_encoder_output` | Optional audio encoding that can influence the video generation based on sound characteristics. When provided, the audio features are interpolated and used to condition the video generation. | AUDIOENCODEROUTPUT | No | - |
| `ref_image` | Optional reference image that provides visual guidance for the video content. The image is upscaled to match the specified width and height, then encoded into a latent representation. Only the first image in the input batch is used. | IMAGE | No | - |
| `control_video` | Optional control video that guides the motion and structure of the generated video. The video is upscaled and encoded, then used to condition the output. Only the first `length` frames are used. | IMAGE | No | - |
| `ref_motion` | Optional motion reference that provides guidance for movement patterns in the video. If the input has more than 73 frames, only the last 73 are used. If fewer than 73 frames are provided, the sequence is padded with neutral frames. | IMAGE | No | - |

**Note:** The optional inputs (`audio_encoder_output`, `ref_image`, `control_video`, `ref_motion`) can be used independently or combined. Control-video conditioning is always applied; when no `control_video` is provided, an empty (zero) control video is used.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Processed positive conditioning modified for video generation. When the corresponding optional inputs are provided, it includes audio embeddings, reference latents, motion references, and control video conditioning. | CONDITIONING |
| `negative` | Processed negative conditioning modified for video generation. When the corresponding optional inputs are provided, it includes audio embeddings (set to zero), reference latents, motion references, and control video conditioning. | CONDITIONING |
| `latent` | Empty latent tensor that serves as the starting point for video generation. The latent has shape [batch_size, 16, latent_t, height/8, width/8], where latent_t = ((length - 1) // 4) + 1. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/en.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
