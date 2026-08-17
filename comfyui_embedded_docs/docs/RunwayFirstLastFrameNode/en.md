# Runway First-Last-Frame to Video

The Runway First-Last-Frame to Video node generates videos by uploading first and last keyframes along with a text prompt. It creates smooth transitions between the provided start and end frames using Runway's Gen-3 model. This is particularly useful for complex transitions where the end frame differs significantly from the start frame.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for the generation (default: empty string) | STRING | Yes | N/A |
| `start_frame` | Start frame to be used for the video | IMAGE | Yes | N/A |
| `end_frame` | End frame to be used for the video. Supported for gen3a_turbo only. | IMAGE | Yes | N/A |
| `duration` | Video duration in seconds (default: "5") | COMBO | Yes | `"5"`<br>`"10"` |
| `ratio` | Aspect ratio for the generated video (default: "768:1280") | COMBO | Yes | `"768:1280"`<br>`"1280:768"` |
| `seed` | Random seed for generation. Set to 0 for random seed (default: 0). | INT | No | 0 to 4294967295 |

**Parameter Constraints:**

- The `prompt` must contain at least 1 character
- Both `start_frame` and `end_frame` must have maximum dimensions of 7999x7999 pixels
- Both `start_frame` and `end_frame` must have aspect ratios between 0.5 and 2.0
- The `end_frame` parameter is only supported when using the gen3a_turbo model

**Note:** This node is marked as deprecated. Review Runway's best practices for creating with keyframes on Gen-3 before use: https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video transitioning between the start and end frames | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/en.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
