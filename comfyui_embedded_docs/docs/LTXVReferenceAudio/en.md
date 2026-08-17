# LTXV Reference Audio (ID-LoRA)

The LTXV Reference Audio node sets a reference audio clip for ID-LoRA speaker identity transfer in audio generation. It encodes the clip into the conditioning so the generated audio adopts the speaker's voice characteristics, and optionally patches the model with identity guidance, which runs an extra forward pass without the reference to amplify the speaker identity effect.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to be patched with identity guidance. | MODEL | Yes | - |
| `positive` | The positive conditioning input. | CONDITIONING | Yes | - |
| `negative` | The negative conditioning input. | CONDITIONING | Yes | - |
| `reference_audio` | Reference audio clip whose speaker identity to transfer. ~5 seconds recommended (training duration). Shorter or longer clips may degrade voice identity transfer. | AUDIO | Yes | - |
| `audio_vae` | LTXV Audio VAE for encoding. | VAE | Yes | - |
| `identity_guidance_scale` | Strength of identity guidance. Runs an extra forward pass without reference each step to amplify speaker identity. Set to 0 to disable (no extra pass). (default: 3.0) | FLOAT | No | 0.0 - 100.0 |
| `start_percent` | Start of the sigma range where identity guidance is active. (default: 0.0) | FLOAT | No | 0.0 - 1.0 |
| `end_percent` | End of the sigma range where identity guidance is active. (default: 1.0) | FLOAT | No | 0.0 - 1.0 |

Note: Identity guidance is only active for sigma values within the range defined by `start_percent` and `end_percent`; outside that range the denoised output is left unchanged. The reference audio is added to both the positive and negative conditioning. If the reference audio sample rate differs from the audio VAE's sample rate, the audio is resampled automatically to match the VAE.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The model patched with the identity guidance function. | MODEL |
| `positive` | The positive conditioning, now containing the encoded reference audio data. | CONDITIONING |
| `negative` | The negative conditioning, now containing the encoded reference audio data. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/en.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
