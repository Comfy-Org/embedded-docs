# Sonilo Text to Music

The Sonilo Text to Music node generates music from a text description using Sonilo's AI model. You provide a prompt describing the music you want, and the node sends a request to the Sonilo service to create an audio file. You can also specify the target duration of the generated music.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt describing the music to generate. Must contain between 1 and 1000 characters. | STRING | Yes | 1 to 1000 characters |
| `duration` | Target duration in seconds. Maximum: 6 minutes. Default: 30. | INT | No | 1 to 360 |
| `seed` | Seed for reproducibility. Currently ignored by the Sonilo service but kept for graph consistency. Default: 0. | INT | No | 0 to 18446744073709551615 |

**Note:** The `seed` input is provided for workflow consistency but does not currently affect the output of the Sonilo service.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | The generated music as an audio file. | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/en.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
