# ByteDance Seedance 2.0 Reference to Video

This node generates, edits, or extends videos using ByteDance's Seedance 2.5 or 2.0 AI models. You describe the video in a text prompt and can add reference images, videos, and audio to guide the result. It supports multimodal reference inputs, video editing, and video extension.

## Inputs

Selecting a `model` determines which of the parameters below are available. `video_editing` and `output_format` appear only when Seedance 2.5 is selected.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The AI model used to generate the video. Seedance 2.5 is the newest model with videos up to 30 seconds and mp4/mov output; Seedance 2.0 is for maximum quality and 1080p/4k; Fast is for speed optimization; Mini is for the fastest, lowest-cost generation. Selecting a model reveals the model-specific inputs listed below. | COMBO | Yes | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0). | INT | Yes | 0 to 2147483647 |
| `watermark` | Whether to add a watermark to the video (default: False). | BOOLEAN | Yes | `True`<br>`False` |
| `prompt` | Text prompt for video generation. For Seedance 2.5, put spoken lines in double quotes to steer the generated dialogue. Must contain at least one non-whitespace character. | STRING | Yes | Any text |
| `resolution` | Resolution of the output video. Seedance 2.5, 2.0 Fast, and 2.0 Mini offer 480p and 720p; Seedance 2.0 also offers 1080p and 4k (Seedance 2.5 default: 720p). | COMBO | Yes | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Aspect ratio of the output video (Seedance 2.5 default: `"16:9"`; Seedance 2.0 models default: `"adaptive"`). | COMBO | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duration of the output video in seconds (Seedance 2.5: 4-30, default 5; Seedance 2.0 models: 4-15, default 7). | INT | Yes | 4 to 30 (Seedance 2.5)<br>4 to 15 (Seedance 2.0)<br>Step: 1 |
| `generate_audio` | Enable audio generation for the output video (default: True). | BOOLEAN | Yes | `True`<br>`False` |
| `video_editing` | Seedance 2.5 only. Enable when the prompt edits a connected reference video, for example replacing an object in it. The output then keeps the source clip's own length and aspect ratio, and the duration and ratio widgets are ignored. Leave disabled to generate a new video, or to extend one to the duration you set (default: False). | BOOLEAN | Yes | `True`<br>`False` |
| `output_format` | Seedance 2.5 only. Container format of the output video (default: `"mp4"`). | COMBO | Yes | `"mp4"` |
| `reference_images` | Reference images that guide the video generation. Images are auto-downscaled to a maximum side of 6000 pixels and must be at least 300x300 pixels with an aspect ratio between 0.4 and 2.5. | IMAGE | No | Up to 30 (Seedance 2.5)<br>Up to 9 (Seedance 2.0) |
| `reference_videos` | Reference videos that guide the video generation; used for video editing and extension. | VIDEO | No | Up to 10 (Seedance 2.5)<br>Up to 3 (Seedance 2.0) |
| `reference_audios` | Reference audio clips that guide the video generation. | AUDIO | No | Up to 10 (Seedance 2.5)<br>Up to 3 (Seedance 2.0) |
| `auto_downscale` | Automatically downscale reference videos that exceed the model's pixel budget for the selected resolution. Aspect ratio is preserved; videos already within limits are untouched (default: True). | BOOLEAN | No | `True`<br>`False` |
| `auto_upscale` | Automatically upscale reference videos that are below the model's minimum pixel count for the selected resolution. Aspect ratio is preserved; videos already meeting the minimum are untouched. Note: upscaling a low-resolution source does not add real detail and may produce lower-quality generations (default: False). | BOOLEAN | No | `True`<br>`False` |
| `reference_assets` | IDs of previously created Seedance virtual-library assets (Image, Video, or Audio) to use as references. Each asset must exist and have an Active status. In the prompt, assets can be referred to as asset1, asset 2, etc.; the node replaces these tokens with labels such as Image 2. | STRING | No | Up to 30 (Seedance 2.5)<br>Up to 9 (Seedance 2.0) |

**Important Constraints:**

* At least one reference is required. For Seedance 2.0, 2.0 Fast, and 2.0 Mini, you must provide at least one image or video reference (via `reference_images`, `reference_videos`, or an image/video `reference_assets` entry). Seedance 2.5 additionally accepts audio-only references.
* Reference counts are model-dependent: Seedance 2.5 allows up to 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios`, and 30 `reference_assets`; Seedance 2.0 models allow up to 9 images, 3 videos, 3 audio clips, and 9 assets. Totals are counted across direct inputs and asset references combined and are validated before generation.
* Each reference video must be at least 1.8 seconds long, and each reference audio clip must be at least 1.8 seconds long. The total duration of all reference videos and of all reference audios must stay within the selected model's limit (15.1 seconds for the Seedance 2.0 models).
* Reference videos must also meet the model's pixel-count limits for the selected resolution. With `auto_downscale` enabled (default), oversized videos are automatically resized; with `auto_upscale` enabled, undersized videos are enlarged. If either automatic adjustment is disabled, videos outside the corresponding limit raise an error.
* When `video_editing` is enabled on Seedance 2.5, the `duration` and `ratio` inputs are ignored; the output matches the reference video's own length and aspect ratio.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `video` | The generated video file. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/en.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
