# Concat AV Latent

The LTXVConcatAVLatent node merges a video latent and an audio latent into a single joint latent for use with audio-visual models such as LTXV or MiniMax H3. It bundles the `samples` from both inputs together, and if either input includes a `noise_mask`, those masks are bundled as well. If the video latent is already an AV latent, the node keeps its video stream and replaces its audio stream with the provided audio latent.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `video_latent` | Latent representation of the video data. | LATENT | Yes |  |
| `audio_latent` | Latent representation of the audio data to combine with the video latent. | LATENT | Yes |  |

**Note about audio length:** When `video_latent` is already an AV latent, `audio_latent` must match the embedded audio stream in all dimensions except one. The node trims or zero-pads the audio along that dimension to fit the existing stream length. The padded tail is left unmasked so the model can generate it.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `latent` | A latent containing the paired video and audio `samples`. If either input provides a `noise_mask`, the output also contains a paired `noise_mask`; a missing mask is replaced with ones. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/en.md)

---
**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`
