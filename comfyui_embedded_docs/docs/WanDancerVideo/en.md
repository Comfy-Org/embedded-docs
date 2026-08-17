# WanDancerVideo

WanDancerVideo prepares the conditioning data and an empty latent tensor for video generation with the WanDancer model. It takes positive and negative conditioning and optionally combines them with a starting image, a mask, CLIP vision embeddings, and audio features to control the generated video.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | The positive conditioning to guide video generation. | CONDITIONING | Yes |  |
| `negative` | The negative conditioning to guide video generation. | CONDITIONING | Yes |  |
| `vae` | The VAE used to encode the start image into the latent space. | VAE | Yes |  |
| `width` | The width of the generated video in pixels (default: 480). | INT | Yes | 16 to MAX_RESOLUTION (step: 16) |
| `height` | The height of the generated video in pixels (default: 832). | INT | Yes | 16 to MAX_RESOLUTION (step: 16) |
| `length` | The number of frames in the generated video. Should stay 149 for WanDancer (default: 149). | INT | Yes | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | The CLIP vision embeds for the first frame. | CLIP_VISION_OUTPUT | No |  |
| `clip_vision_output_ref` | The CLIP vision embeds for the reference image. | CLIP_VISION_OUTPUT | No |  |
| `start_image` | The initial image(s) to be encoded, can be any number of frames. | IMAGE | No |  |
| `mask` | Image conditioning mask for the start image(s). White is kept, black is generated. Used for the local generations. | MASK | No |  |
| `audio_encoder_output` | The output from an audio encoder, providing audio features, FPS, and audio inject scale for audio-conditioned generation. | AUDIO_ENCODER_OUTPUT | No |  |

**Note on Parameter Constraints:**
- When `start_image` is provided, it is resized to `width` × `height`, limited to `length` frames, and encoded into a latent that is attached to both conditionings together with a concat mask.
- `mask` only takes effect when `start_image` is also provided. In the mask, white areas are kept and black areas are generated. When `mask` is not provided, the start image area is used as a conditioning guide and the remaining frames are generated.
- `clip_vision_output_ref` is applied only when `clip_vision_output` is provided.
- `audio_encoder_output` attaches audio features, FPS, and an audio inject scale (default 1.0) to both conditionings.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | The positive conditioning with any additional data (concat latent, CLIP vision, audio) attached. | CONDITIONING |
| `negative` | The negative conditioning with any additional data (concat latent, CLIP vision, audio) attached. | CONDITIONING |
| `latent` | An empty latent tensor with dimensions matching the specified video length, height, and width. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/en.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
