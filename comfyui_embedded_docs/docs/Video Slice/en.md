# Trim Video

The Video Slice node allows you to extract a specific segment from a video. You can define a start time and a duration to trim the video, or simply skip the beginning frames. If the requested duration is longer than the remaining video, the node can either return what's available or raise an error.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `video` | The input video to be sliced. | VIDEO | Yes | - |
| `start_time` | Start time in seconds (default: 0.0). | FLOAT | No | -1e5 to 1e5 |
| `duration` | Duration in seconds, or 0 for unlimited duration (default: 0.0). | FLOAT | No | 0.0 and above |
| `strict_duration` | If True, when the specified duration is not possible, an error will be raised (default: False). | BOOLEAN | No | - |

Note: When `duration` is 0, the node slices from `start_time` to the end of the video. If the requested segment cannot be created — for example, because `start_time` is beyond the end of the video — the node raises an error.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `video` | The trimmed video segment. | VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/en.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
