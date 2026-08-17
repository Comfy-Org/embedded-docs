# Set Reference Audio

This node sets a reference audio timbre for use in the "ace step 1.5" process. It takes a conditioning input and an optional latent representation of the audio, then attaches that latent data to the conditioning so later nodes in the workflow can use it as the reference audio. If no latent is provided, the conditioning is returned unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `conditioning` | The conditioning data to which the reference audio information will be attached. | CONDITIONING | Yes |  |
| `latent` | An optional latent representation of the reference audio. When provided, its samples are added to the conditioning. | LATENT | No |  |

When `latent` is provided, its samples are appended to the conditioning's reference audio timbre latents. If no `latent` is provided, the original conditioning is passed through unchanged.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `conditioning` | The modified conditioning data, now containing the reference audio timbre latents if the optional `latent` input was provided. If no latent is provided, the original conditioning is returned unchanged. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/en.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
