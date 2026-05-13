> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/en.md)

The EmptyAceStepLatentAudio node creates empty latent audio samples of a specified duration. It generates a batch of silent audio latents filled with zeros, where the length is calculated based on the input seconds and audio processing parameters. This node is useful for initializing audio processing workflows that require latent representations.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Yes | 1.0 - 1000.0 | The duration of the audio in seconds (default: 120.0) |
| `batch_size` | INT | Yes | 1 - 4096 | The number of latent images in the batch (default: 1) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | LATENT | Returns empty latent audio samples with zeros. The output contains a `samples` tensor and a `type` field set to "audio". |

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
