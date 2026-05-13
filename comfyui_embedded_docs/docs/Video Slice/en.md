> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/en.md)

The Video Slice node allows you to extract a specific segment from a video. You can define a start time and a duration to trim the video, or simply skip the beginning frames. If the requested duration is longer than the remaining video, the node can either return what's available or raise an error.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Yes | - | The input video to be sliced. |
| `start_time` | FLOAT | No | -1e5 to 1e5 | Start time in seconds (default: 0.0). |
| `duration` | FLOAT | No | 0.0 and above | Duration in seconds, or 0 for unlimited duration (default: 0.0). |
| `strict_duration` | BOOLEAN | No | - | If True, when the specified duration is not possible, an error will be raised (default: False). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | The trimmed video segment. |

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
