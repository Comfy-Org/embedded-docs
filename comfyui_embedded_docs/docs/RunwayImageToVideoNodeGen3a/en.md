> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/en.md)

The Runway Image to Video (Gen3a Turbo) node generates a video from a single starting frame using Runway's Gen3a Turbo model. It takes a text prompt and an initial image frame, then creates a video sequence based on the specified duration and aspect ratio. This node connects to Runway's API to process the generation remotely.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Yes | N/A | Text prompt for the generation (default: "") |
| `start_frame` | IMAGE | Yes | N/A | Start frame to be used for the video |
| `duration` | COMBO | Yes | `"5"`<br>`"10"` | Video duration in seconds (default: "5") |
| `ratio` | COMBO | Yes | `"1280x720"`<br>`"720x1280"`<br>`"1920x1080"`<br>`"1080x1920"`<br>`"1080x1080"` | Aspect ratio of the generated video (default: "1280x720") |
| `seed` | INT | No | 0 to 4294967295 | Random seed for generation (default: 0) |

**Parameter Constraints:**

- The `start_frame` must have dimensions not exceeding 7999x7999 pixels.
- The `start_frame` must have an aspect ratio between 0.5 and 2.0.
- The `prompt` must contain at least one character (cannot be empty).

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | The generated video sequence |

---
**Source fingerprint (SHA-256):** `4f3270ce070ce50580699292e21c5f9e3b1a56dd8ac981f67a9026ef6fc8ed76`
