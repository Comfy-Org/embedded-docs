# Kling Text to Video

The Kling Text to Video Node converts text prompts into short video clips using the Kling video generation service. You provide positive and negative prompts along with settings such as aspect ratio, configuration scale, and generation mode, and the node returns the generated video with its identifier and duration.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Positive text prompt describing the desired video content. Multiline input. Cannot be empty. | STRING | Yes | Maximum 2500 characters |
| `negative_prompt` | Negative text prompt describing what to avoid in the video. Multiline input. Can be left empty. | STRING | Yes | Maximum 2500 characters |
| `cfg_scale` | Configuration scale value that controls how closely the video follows the prompt (default: 1.0). | FLOAT | No | 0.0 to 1.0 |
| `aspect_ratio` | Video aspect ratio setting (default: "16:9"). | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | The configuration to use for the video generation following the format: mode / duration / model_name (default: "pro mode / 5s duration / kling-v2-5-turbo"). The 5s mode costs USD 0.35, the 10s mode costs USD 0.70. | COMBO | No | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video output. | VIDEO |
| `video_id` | Unique identifier for the generated video. | STRING |
| `duration` | Duration information for the generated video. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/en.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
