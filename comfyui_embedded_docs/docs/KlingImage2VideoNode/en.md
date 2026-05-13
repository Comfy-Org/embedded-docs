> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/en.md)

The Kling Image to Video Node generates a video from a starting reference image using text prompts. It takes an image as the first frame and creates a video sequence based on positive and negative text descriptions, with configurable options for model, duration, aspect ratio, and generation mode.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Yes | - | The reference image used to generate the video. |
| `prompt` | STRING | Yes | - | Positive text prompt. |
| `negative_prompt` | STRING | Yes | - | Negative text prompt. |
| `model_name` | COMBO | Yes | `"kling-v2-master"`<br>`"kling-v2-1-master"`<br>`"kling-v2-5-turbo"`<br>`"kling-v2-1"`<br>`"kling-v1-6"`<br>`"kling-v1-5"`<br>`"kling-v1-4"`<br>`"kling-v1-0"` | The model used for video generation (default: `"kling-v2-master"`). |
| `cfg_scale` | FLOAT | Yes | 0.0 to 1.0 | Controls how closely the video follows the prompt. Higher values mean stronger adherence (default: 0.8). |
| `mode` | COMBO | Yes | `"std"`<br>`"pro"` | The generation mode. `"std"` is standard quality, `"pro"` is higher quality (default: `"std"`). |
| `aspect_ratio` | COMBO | Yes | `"16:9"`<br>`"9:16"`<br>`"1:1"` | The aspect ratio of the generated video (default: `"16:9"`). |
| `duration` | COMBO | Yes | `"5"`<br>`"10"` | The duration of the generated video in seconds (default: `"5"`). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | The generated video output. |
| `video_id` | STRING | Unique identifier for the generated video. |
| `duration` | STRING | Duration information for the generated video. |

---
**Source fingerprint (SHA-256):** `2f82997307265dba6714733523e265d1e0a25fd7491b043f05d7d000b7b9b2f3`
