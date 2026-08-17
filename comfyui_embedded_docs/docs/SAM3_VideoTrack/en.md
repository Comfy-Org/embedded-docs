# Run SAM3 Video Track

Track objects across video frames using SAM3's memory-based tracker. This node processes a sequence of video frames and maintains object identities across frames, using either initial masks or text prompts to define what to track.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `images` | Video frames as batched images | IMAGE | Yes | Batched video frames |
| `model` | The SAM3 model to use for tracking | MODEL | Yes | SAM3 model |
| `initial_mask` | Mask(s) for the first frame to track (one per object). Required if `conditioning` is not provided. | MASK | No | One mask per object |
| `conditioning` | Text conditioning for detecting new objects during tracking. Required if `initial_mask` is not provided. | CONDITIONING | No | Text conditioning |
| `detection_threshold` | Score threshold for text-prompted detection (default: 0.5). | FLOAT | Yes | 0.0 to 1.0 |
| `max_objects` | Max tracked objects. Initial masks count toward this limit. 0 uses the internal cap of 64 (default: 4). | INT | Yes | 0 to 64 |
| `detect_interval` | Run detection every N frames (1=every frame). Higher values save compute (default: 1). | INT | Yes | 1 or higher |

**Note:** Either `initial_mask` or `conditioning` must be provided. If both are omitted, the node will raise an error. When both are provided, the initial masks define the objects to track from the first frame and the text prompts detect additional objects during tracking.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `track_data` | Tracking data containing object masks and metadata across all video frames, including the original frame dimensions. | SAM3_TRACK_DATA |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_VideoTrack/en.md)

---
**Source fingerprint (SHA-256):** `ef584628b334997a001a857a7deffb7eda34db8fa50e3d734a07b5e92566d48d`
