> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/en.md)

Generate music from video using Sonilo's AI model. This node analyzes the content of an input video and creates a matching piece of music. It uses an external AI service to process the video and generate the audio.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Yes | - | Input video to generate music from. Maximum duration: 6 minutes. |
| `prompt` | STRING | No | - | Optional text prompt to guide music generation. Leave empty for best quality - the model will fully analyze the video content. (default: empty string) |
| `seed` | INT | No | 0 to 18446744073709551615 | Seed for reproducibility. Currently ignored by the Sonilo service but kept for graph consistency. (default: 0) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | The generated music as an audio file. |

---
**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`
