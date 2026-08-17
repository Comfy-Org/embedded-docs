# LTXVAddGuide

LTXVAddGuide adds video conditioning guidance to latent sequences by encoding input images or videos and incorporating them as keyframes into the conditioning data. It processes the input through a VAE encoder and strategically places the resulting latents at specified frame positions while updating both positive and negative conditioning with keyframe information. The node handles frame alignment constraints and allows control over the strength of the conditioning influence.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning input to be modified with keyframe guidance | CONDITIONING | Yes | - |
| `negative` | Negative conditioning input to be modified with keyframe guidance | CONDITIONING | Yes | - |
| `vae` | VAE model used for encoding the input image/video frames | VAE | Yes | - |
| `latent` | Input latent sequence that will receive the conditioning frames | LATENT | Yes | - |
| `image` | Image or video to condition the latent video on. Must be 8*n + 1 frames. If the video is not 8*n + 1 frames, it will be cropped to the nearest 8*n + 1 frames. | IMAGE | Yes | - |
| `frame_idx` | Frame index to start the conditioning at. For single-frame images or videos with 1-8 frames, any frame_idx value is acceptable. For videos with 9+ frames, frame_idx must be divisible by 8, otherwise it will be rounded down to the nearest multiple of 8. Negative values are counted from the end of the video. (default: 0) | INT | No | -9999 to 9999 |
| `strength` | Strength of the conditioning influence, where 1.0 applies full conditioning and 0.0 applies no conditioning (default: 1.0) | FLOAT | No | 0.0 to 10.0 |
| `attention_mask` | Optional pixel-space spatial mask. Controls per-region conditioning influence via self-attention, multiplied by strength. | MASK | No | - |
| `iclora_parameters` | Optional IC-LoRA parameters from a Get IC-LoRA Parameters node. Used for adjusting guide processing as required by certain IC-LoRAs (e.g., those with a reference_downscale_factor > 1). When chained, each LTXVAddGuide uses only the parameters connected to it. | IC_LORA_PARAMETERS | No | - |

**Notes:**

- The input image/video must have a frame count following the 8*n + 1 pattern (e.g., 1, 9, 17, 25 frames). If the input exceeds this pattern, it will be automatically cropped to the nearest valid frame count.
- When using IC-LoRA parameters with a `reference_downscale_factor` greater than 1, the latent spatial dimensions (width and height) must be divisible by that factor. The node raises an error if this condition is not met.
- The guide must fit within the latent sequence: the starting frame index plus the number of guide frames cannot exceed the latent length, otherwise the node raises an error.
- The node does not support combined audio-video latents. Both the input `latent` and the encoded guide must use the standard 128-channel video latent format, otherwise the node raises an error.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning updated with keyframe guidance information | CONDITIONING |
| `negative` | Negative conditioning updated with keyframe guidance information | CONDITIONING |
| `latent` | Latent sequence with incorporated conditioning frames and updated noise mask | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/en.md)

---
**Source fingerprint (SHA-256):** `3e0d1422fbd1b5b3e4c69e641af2ecdb5ae8de3f4368b336917a0dce4286771e`
