# Wan 2.7 Text to Video

This node generates a video from a text description using the Wan 2.7 model. It sends your request to an external API, which processes the prompt and returns a video file. You can optionally provide an audio clip to influence the video's motion and timing.

## Inputs

The inputs include common settings and model-specific settings that appear when the `wan2.7-t2v` model is selected.

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The specific model to use for video generation. | DYNAMIC_COMBO | Yes | `"wan2.7-t2v"` |
| `audio` | Audio for driving video generation (e.g., lip sync, beat-matched motion). Duration: 1.5s-60s. If not provided, the model automatically generates matching background music or sound effects. | AUDIO | No | - |
| `seed` | Seed to use for generation (default: 0). | INT | No | 0 to 2147483647 |
| `prompt_extend` | Whether to enhance the prompt with AI assistance (default: True). | BOOLEAN | No | True<br>False |
| `watermark` | Whether to add an AI-generated watermark to the result (default: False). | BOOLEAN | No | True<br>False |

### wan2.7-t2v Inputs

These settings appear when the `wan2.7-t2v` model is selected.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt describing the elements and visual features. Supports English and Chinese. | STRING | Yes | - |
| `negative_prompt` | Negative prompt describing what to avoid. | STRING | No | - |
| `resolution` | The resolution of the output video. | COMBO | Yes | `"720P"`<br>`"1080P"` |
| `ratio` | The aspect ratio of the output video. | COMBO | Yes | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | The length of the video in seconds (default: 5). | INT | Yes | 2 to 15 |

**Note:** The `prompt` input must not be empty. The `audio` input is optional; if provided, its duration must be between 1.5 and 60 seconds. If omitted, the model automatically generates matching audio. When `negative_prompt` is left empty, it is not sent to the API. `prompt_extend` and `watermark` are advanced options.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video file. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/en.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
