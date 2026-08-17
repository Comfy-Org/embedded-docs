# WanMoveTrackToVideo

The WanMoveTrackToVideo node prepares conditioning and latent data for video generation. It encodes a starting image sequence into latent space using a VAE and can optionally incorporate motion tracking information to guide object movement in the generated video. The node outputs modified positive and negative conditioning along with an empty latent tensor ready for a video generation model.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | The positive conditioning input to be modified. | CONDITIONING | Yes | - |
| `negative` | The negative conditioning input to be modified. | CONDITIONING | Yes | - |
| `vae` | The VAE model used to encode the starting image into the latent space. | VAE | Yes | - |
| `tracks` | Optional motion tracking data containing object paths. | TRACKS | No | - |
| `strength` | Strength of the track conditioning. Only has an effect when `tracks` is provided and the value is greater than 0.0. (default: 1.0) | FLOAT | Yes | 0.0 - 100.0 |
| `width` | The width of the output video. Set in increments of 16. (default: 832) | INT | Yes | 16 - MAX_RESOLUTION |
| `height` | The height of the output video. Set in increments of 16. (default: 480) | INT | Yes | 16 - MAX_RESOLUTION |
| `length` | The number of frames in the video sequence. Set in increments of 4. (default: 81) | INT | Yes | 1 - MAX_RESOLUTION |
| `batch_size` | The batch size for the latent output. (default: 1) | INT | Yes | 1 - 4096 |
| `start_image` | The starting image or image sequence to encode with the VAE. | IMAGE | Yes | - |
| `clip_vision_output` | Optional CLIP vision model output to add to the conditioning. | CLIP_VISION_OUTPUT | No | - |

Note: Track-based motion is applied only when `tracks` is provided and `strength` is greater than 0.0. Otherwise, the conditioning receives the unmodified encoded starting image. The `start_image` is used to create a latent image and a mask for the conditioning; if it is not available, the node only passes through the conditioning and outputs an empty latent.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | The modified positive conditioning, potentially containing `concat_latent_image`, `concat_mask`, and `clip_vision_output`. | CONDITIONING |
| `negative` | The modified negative conditioning, potentially containing `concat_latent_image`, `concat_mask`, and `clip_vision_output`. | CONDITIONING |
| `latent` | An empty latent tensor with dimensions shaped by the `batch_size`, `length`, `height`, and `width` inputs. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/en.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
