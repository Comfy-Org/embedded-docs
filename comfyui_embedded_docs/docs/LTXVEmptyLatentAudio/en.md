# LTXV Empty Latent Audio

The LTXV Empty Latent Audio node creates a batch of empty (zero-filled) latent audio tensors. It uses the configuration from a provided Audio VAE model to determine the correct dimensions for the latent space, such as the number of channels and frequency bins. The number of audio latents is calculated from the frame count and frame rate using the Audio VAE model. This empty latent serves as a starting point for audio generation or manipulation workflows within ComfyUI.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `frames_number` | Number of frames. Default: 97. | INT | Yes | 1 to 1000 |
| `frame_rate` | Number of frames per second. Accepts float or integer values. Default: 25.0. | FLOAT (or INT) | Yes | 1.0 to 1000.0 |
| `batch_size` | The number of latent audio samples in the batch. Default: 1. | INT | Yes | 1 to 4096 |
| `audio_vae` | The Audio VAE model to get configuration from. | VAE | Yes | N/A |

**Note:** The `audio_vae` input is mandatory. The node will raise an error if it is not provided.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `Latent` | An empty latent audio tensor with the structure (batch_size, z_channels, num_audio_latents, audio_freq), configured to match the input Audio VAE. The output also includes a `type` field set to "audio". | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/en.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
