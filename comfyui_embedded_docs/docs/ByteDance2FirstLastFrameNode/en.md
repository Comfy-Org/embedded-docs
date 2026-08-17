# ByteDance Seedance 2.5 First-Last-Frame to Video

This node generates a video from a required first frame image and an optional last frame image using ByteDance Seedance 2.5 or Seedance 2.0 models. The first frame defines the beginning of the clip, the last frame (when provided) defines the ending, and a text prompt describes the motion. The selected model controls the available resolutions, durations, and output format options.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model used for video generation. Seedance 2.5 is the newest model with videos up to 30 seconds and mp4/mov output; Seedance 2.0 offers maximum quality and 1080p/4k; Fast is optimized for speed; Mini is the fastest, lowest-cost generation. Selecting a model reveals its specific inputs below. | DYNAMIC_COMBO | Yes | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | First frame image for the video. One of `first_frame` or `first_frame_asset_id` is required. | IMAGE | No | - |
| `last_frame` | Last frame image for the video. | IMAGE | No | - |
| `first_frame_asset_id` | Seedance asset_id to use as the first frame. Mutually exclusive with the `first_frame` image input. Default is an empty string. | STRING | No | - |
| `last_frame_asset_id` | Seedance asset_id to use as the last frame. Mutually exclusive with the `last_frame` image input. Default is an empty string. | STRING | No | - |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. Default is 0. | INT | No | 0 to 2147483647 |
| `watermark` | Whether to add a watermark to the video. Default is False. | BOOLEAN | No | - |

### Seedance 2.5 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for video generation. Put spoken lines in double quotes to steer the generated dialogue. Default is an empty string. | STRING | Yes | - |
| `resolution` | Resolution of the output video. Default is "720p". | COMBO | Yes | `"480p"`<br>`"720p"` |
| `duration` | Duration of the output video in seconds (4-30). Default is 5. | INT | Yes | 4 to 30 |
| `generate_audio` | Enable audio generation for the output video. Default is True. | BOOLEAN | Yes | - |
| `output_format` | Container format of the output video. Default is "mp4". | COMBO | Yes | `"mp4"` |

### Seedance 2.0 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for video generation. Default is an empty string. | STRING | Yes | - |
| `resolution` | Resolution of the output video. | COMBO | Yes | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Aspect ratio of the output video. Default is "adaptive". | COMBO | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duration of the output video in seconds (4-15). Default is 7. | INT | Yes | 4 to 15 |
| `generate_audio` | Enable audio generation for the output video. Default is True. | BOOLEAN | Yes | - |

### Shared by Seedance 2.0 Fast and Seedance 2.0 Mini

These two models expose the same inputs as Seedance 2.0, except that only 480p and 720p resolutions are available.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt for video generation. Default is an empty string. | STRING | Yes | - |
| `resolution` | Resolution of the output video. | COMBO | Yes | `"480p"`<br>`"720p"` |
| `ratio` | Aspect ratio of the output video. Default is "adaptive". | COMBO | Yes | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duration of the output video in seconds (4-15). Default is 7. | INT | Yes | 4 to 15 |
| `generate_audio` | Enable audio generation for the output video. Default is True. | BOOLEAN | Yes | - |

**Constraints and limitations:**

*   The `prompt` is required and must contain at least one non-whitespace character (leading and trailing whitespace is ignored).
*   You must provide exactly one first-frame source: either the `first_frame` image or the `first_frame_asset_id`. Providing both raises an error, and providing neither raises an error.
*   The `last_frame` image and `last_frame_asset_id` are mutually exclusive. Both can be omitted.
*   Asset IDs must reference existing Seedance assets with an Active status. If an asset is not active or is not an Image asset, an error is raised.
*   Local images must have an aspect ratio between 0.4 and 2.5 (2:5 to 5:2).
*   For Seedance 2.0 models, local images must be at least 300x300 pixels. They are automatically resized to the exact supported output dimensions for the selected resolution and ratio, and the request is submitted with the ratio "adaptive". When `ratio` is "adaptive", the output aspect ratio is derived from the first frame's own aspect ratio, snapped to the nearest supported ratio. When asset IDs are used instead of local images, the selected `ratio` value is applied directly.
*   For Seedance 2.5, and for any model when asset IDs are used, images are automatically downscaled to a maximum side of 6000 pixels and must be between 300 and 6000 pixels in each dimension.
*   Seedance 2.5 always keeps the first frame's own aspect ratio, so no `ratio` input is shown for this model.
*   Duration limits differ by model: Seedance 2.5 supports 4 to 30 seconds, while Seedance 2.0, 2.0 Fast, and 2.0 Mini support 4 to 15 seconds.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | The generated video. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/en.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`
