> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/en.md)

The ByteDance Text to Video node generates videos using ByteDance models through an API based on text prompts. It takes a text description and various video settings as input, then creates a video that matches the provided specifications. The node handles the API communication and returns the generated video as output.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | Yes | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-t2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | The ByteDance model to use for generation (default: `"seedance-1-0-pro-fast-251015"`). |
| `prompt` | STRING | Yes | - | The text prompt used to generate the video. |
| `resolution` | STRING | Yes | `"480p"`<br>`"720p"`<br>`"1080p"` | The resolution of the output video. |
| `aspect_ratio` | STRING | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | The aspect ratio of the output video. |
| `duration` | INT | Yes | 3 to 12 | The duration of the output video in seconds (default: 5). |
| `seed` | INT | No | 0 to 2147483647 | Seed to use for generation (default: 0). |
| `camera_fixed` | BOOLEAN | No | - | Specifies whether to fix the camera. The platform appends an instruction to fix the camera to your prompt, but does not guarantee the actual effect (default: False). |
| `watermark` | BOOLEAN | No | - | Whether to add an "AI generated" watermark to the video (default: False). |
| `generate_audio` | BOOLEAN | No | - | This parameter is ignored for any model except `seedance-1-5-pro-251215` (default: False). |

**Parameter Constraints:**

- The `prompt` parameter must contain at least 1 character after whitespace removal.
- The `prompt` parameter cannot contain the following text parameters: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- The `duration` parameter is limited to values between 3 and 12 seconds. For the `seedance-1-5-pro-251215` model, the minimum supported duration is 4 seconds.
- The `seed` parameter accepts values from 0 to 2,147,483,647.
- The `generate_audio` parameter only has an effect when the `model` is set to `seedance-1-5-pro-251215`; it is ignored for all other models.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | The generated video file |

---
**Source fingerprint (SHA-256):** `44ea3e40b99b337340cc39be1c5b6c903680591f1de49b1f2e82f398979355c5`
