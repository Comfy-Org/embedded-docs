# Kling Image(First Frame) to Video

The Kling Image to Video Node generates a video from a starting reference image using text prompts. It uses the image as the first frame and creates a video sequence based on positive and negative text descriptions, with configurable options for model, duration, generation mode, and aspect ratio.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `start_frame` | The reference image used to generate the video. Must be at least 300x300 pixels with an aspect ratio between 1:2.5 and 2.5:1. | IMAGE | Yes | - |
| `prompt` | Positive text prompt. Maximum 500 characters. | STRING | Yes | - |
| `negative_prompt` | Negative text prompt. Maximum 500 characters. May be left empty. | STRING | Yes | - |
| `model_name` | The model used for video generation (default: `"kling-v2-5-turbo"`). | COMBO | Yes | `"kling-v2-5-turbo"` |
| `cfg_scale` | Controls how closely the video follows the prompt. Higher values mean stronger adherence (default: 0.8). | FLOAT | Yes | 0.0 to 1.0 |
| `mode` | The generation mode (default: `"pro"`). | COMBO | Yes | `"pro"` |
| `aspect_ratio` | The aspect ratio of the generated video (default: `"16:9"`). | COMBO | Yes | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | The duration of the generated video in seconds (default: `"5"`). | COMBO | Yes | `"5"`<br>`"10"` |

Note: The positive prompt must not be empty. Both the positive and negative prompts are limited to 500 characters. The input image must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video. | VIDEO |
| `video_id` | Unique identifier for the generated video. | STRING |
| `duration` | Duration of the generated video. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/en.md)

---
**Source fingerprint (SHA-256):** `f4a461819bc05f92d867bddcc78a66ad7beaa10707ef8cae3e7eb9e6f72c890a`
