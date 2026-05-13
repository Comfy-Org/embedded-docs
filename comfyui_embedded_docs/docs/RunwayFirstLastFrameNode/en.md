> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/en.md)

The Runway First-Last-Frame to Video node generates videos by uploading first and last keyframes along with a text prompt. It creates smooth transitions between the provided start and end frames using Runway's Gen-3 model. This is particularly useful for complex transitions where the end frame differs significantly from the start frame.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Yes | N/A | Text prompt for the generation (default: empty string) |
| `start_frame` | IMAGE | Yes | N/A | Start frame to be used for the video |
| `end_frame` | IMAGE | Yes | N/A | End frame to be used for the video. Supported for gen3a_turbo only. |
| `duration` | COMBO | Yes | `"5"`<br>`"10"` | Video duration in seconds (default: "5") |
| `ratio` | COMBO | Yes | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Aspect ratio for the generated video (default: "16:9") |
| `seed` | INT | No | 0 to 4294967295 | Random seed for generation. Set to 0 for random seed (default: 0). |

**Parameter Constraints:**

- The `prompt` must contain at least 1 character
- Both `start_frame` and `end_frame` must have maximum dimensions of 7999x7999 pixels
- Both `start_frame` and `end_frame` must have aspect ratios between 0.5 and 2.0
- The `end_frame` parameter is only supported when using the gen3a_turbo model

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | The generated video transitioning between the start and end frames |

---
**Source fingerprint (SHA-256):** `57b72c1143b7053272107403279e1f84919cbfe71c57ca4f4e21b4324f7a5346`
