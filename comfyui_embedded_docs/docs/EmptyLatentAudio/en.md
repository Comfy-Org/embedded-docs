> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/en.md)

The EmptyLatentAudio node creates an empty latent tensor for audio processing. It generates a blank audio latent representation with a specified duration and batch size, which can be used as a starting point for audio generation or processing workflows. The node automatically calculates the appropriate latent dimensions based on the audio duration and sample rate.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Yes | 1.0 - 1000.0 | The duration of the audio in seconds (default: 47.6) |
| `batch_size` | INT | Yes | 1 - 4096 | The number of latent images in the batch (default: 1) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Returns an empty latent tensor for audio processing with the specified duration and batch size. The tensor has a shape of [batch_size, 64, length], where length is calculated from the audio duration and sample rate. |

---
**Source fingerprint (SHA-256):** `004f730131b179fe5ac072afe81b2e01a3937fceca5a260b4ae66f92774e96d9`
