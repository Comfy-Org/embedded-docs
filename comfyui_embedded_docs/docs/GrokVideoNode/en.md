# Grok Video

The Grok Video node generates a short video from a text description. It can create a video from scratch using a prompt, or animate a single input image, optionally guided by a prompt. The node sends a request to an external API and returns the generated video.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model to use for video generation. | COMBO | Yes | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | Text description of the desired video. Optional for grok-imagine-video-1.5 when an input image is provided. | STRING | Yes | - |
| `resolution` | The resolution of the output video. 1080p is only available for grok-imagine-video-1.5. | COMBO | Yes | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | The aspect ratio of the output video (default: "auto"). | COMBO | Yes | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | The duration of the output video in seconds (default: 6). | INT | Yes | 1 to 15 |
| `seed` | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0). | INT | Yes | 0 to 2147483647 |
| `image` | Optional starting image. If omitted, the video is generated from the text prompt alone. | IMAGE | No | - |

**Note:**
- The "1080p" resolution is only available with the `grok-imagine-video-1.5` model. Selecting it with `grok-imagine-video` raises an error.
- Only one input image is supported. Providing multiple images raises an error.
- The `prompt` is required unless the model is set to `grok-imagine-video-1.5` and an input image is provided. When required, the prompt must be at least 1 character long after stripping whitespace.
- The `seed` only determines whether the node re-runs; the generated results are nondeterministic regardless of the seed value.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/en.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
