# ByteDance Seedance 2.5 Text to Video

This node generates a video from a text description using ByteDance's Seedance 2.5 or 2.0 models. It sends your prompt to the selected model, waits for the video to be processed, and returns the final result.

## Inputs

The `model` parameter is a dynamic combo. When you select a model, it reveals several model-specific inputs that must be filled in, including the text prompt, resolution, aspect ratio, duration, and audio generation setting.

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model to use for video generation. Seedance 2.5 is the newest model, generating videos up to 30 seconds with mp4/mov output; Seedance 2.0 offers maximum quality with 1080p/4k; Fast is for speed optimization; Mini is the fastest, lowest-cost generation. | DYNAMIC_COMBO | Yes | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0). | INT | No | 0 to 2147483647 |
| `watermark` | Whether to add a watermark to the video (default: False). This is an advanced setting. | BOOLEAN | No | True / False |

### Seedance 2.5 Inputs

These inputs appear when `model` is set to `Seedance 2.5`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for video generation. Put spoken lines in double quotes to steer the generated dialogue (default: empty). | STRING | Yes | Any text |
| `resolution` | Resolution of the output video (default: "720p"). | COMBO | Yes | `"480p"`<br>`"720p"` |
| `ratio` | Aspect ratio of the output video (default: "16:9"). | COMBO | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duration of the output video in seconds (default: 5). | INT | Yes | 4 to 30 |
| `generate_audio` | Enable audio generation for the output video (default: True). | BOOLEAN | No | True / False |
| `output_format` | Container format of the output video (default: "mp4"). | COMBO | Yes | `"mp4"` |

### Seedance 2.0 Inputs

These inputs appear when `model` is set to `Seedance 2.0`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for video generation (default: empty). | STRING | Yes | Any text |
| `resolution` | Resolution of the output video. | COMBO | Yes | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Aspect ratio of the output video (default: "16:9"). | COMBO | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duration of the output video in seconds (default: 7). | INT | Yes | 4 to 15 |
| `generate_audio` | Enable audio generation for the output video (default: True). | BOOLEAN | No | True / False |

### Seedance 2.0 Fast and Seedance 2.0 Mini Inputs

These inputs appear when `model` is set to `Seedance 2.0 Fast` or `Seedance 2.0 Mini`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for video generation (default: empty). | STRING | Yes | Any text |
| `resolution` | Resolution of the output video. | COMBO | Yes | `"480p"`<br>`"720p"` |
| `ratio` | Aspect ratio of the output video (default: "16:9"). | COMBO | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duration of the output video in seconds (default: 7). | INT | Yes | 4 to 15 |
| `generate_audio` | Enable audio generation for the output video (default: True). | BOOLEAN | No | True / False |

**Note:** The `prompt` must contain at least 1 character after removing whitespace, otherwise the task fails validation. Duration limits depend on the model: Seedance 2.5 supports 4 to 30 seconds, while Seedance 2.0, Seedance 2.0 Fast, and Seedance 2.0 Mini support 4 to 15 seconds. Resolution options also differ by model: Seedance 2.5 supports 480p and 720p; Seedance 2.0 supports 480p, 720p, 1080p, and 4k; Seedance 2.0 Fast and Seedance 2.0 Mini support only 480p and 720p.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `video` | The generated video file. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/en.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`
