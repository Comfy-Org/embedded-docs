> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/en.md)

## Overview

Selects specific tracked objects from a SAM3 tracking session by their index numbers and combines them into a single output mask. This allows you to choose which objects to keep and which to ignore from the tracking results.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `track_data` | SAM3TRACKDATA | Yes | N/A | The tracking data output from a SAM3 tracker node, containing the packed masks and original image size. |
| `object_indices` | STRING | No | Any comma-separated list of integers | Comma-separated object indices to include in the output mask (e.g., '0,2,3'). If left empty, all tracked objects are included. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `masks` | MASK | A single binary mask for each frame, where selected objects are combined into one mask. If no objects are selected or no tracking data exists, returns a zero mask. |

---
**Source fingerprint (SHA-256):** `2da82effc4cdc6655d0d37e281858bf33f7b62d9056629ec810e3ff9b2e7b5a6`
