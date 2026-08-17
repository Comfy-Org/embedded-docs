# Separate AV Latent

The LTXVSeparateAVLatent node takes a combined audio-visual latent representation and splits it into two separate latents: one for video and one for audio. It works with any audio-visual model, such as LTXV or MiniMax H3.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `av_latent` | The combined audio-visual latent representation to be separated. | LATENT | Yes | N/A |

**Note:** The input latent's `samples` tensor is expected to have at least two elements along the first dimension (batch dimension). The first element is used for the video latent, and the second element is used for the audio latent. If a `noise_mask` is present, it is split in the same way.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `video_latent` | The latent representation containing the separated video data. | LATENT |
| `audio_latent` | The latent representation containing the separated audio data. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/en.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
