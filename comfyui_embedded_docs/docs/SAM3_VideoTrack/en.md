> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/en.md)

## Overview

Track objects across video frames using SAM3's memory-based tracker. This node processes a sequence of video frames and maintains object identities across frames, using either initial masks or text prompts to define what to track.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Yes | Batched video frames | Video frames as batched images |
| `model` | MODEL | Yes | SAM3 model | The SAM3 model to use for tracking |
| `initial_mask` | MASK | No | One mask per object | Mask(s) for the first frame to track (one per object). Required if `conditioning` is not provided. |
| `conditioning` | CONDITIONING | No | Text conditioning | Text conditioning for detecting new objects during tracking. Required if `initial_mask` is not provided. |
| `detection_threshold` | FLOAT | No | 0.0 to 1.0 (default: 0.5) | Score threshold for text-prompted detection |
| `max_objects` | INT | No | 0 to unlimited (default: 0) | Max tracked objects (0=unlimited). Initial masks count toward this limit. |
| `detect_interval` | INT | No | 1 to unlimited (default: 1) | Run detection every N frames (1=every frame). Higher values save compute. |

**Note:** Either `initial_mask` or `conditioning` must be provided. If both are omitted, the node will raise an error.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `track_data` | SAM3TrackData | Tracking data containing object masks and metadata across all video frames |