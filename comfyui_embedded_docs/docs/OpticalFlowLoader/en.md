> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/en.md)

## Overview

Loads an optical flow model from the `models/optical_flow/` folder. Currently, only torchvision's RAFT-large format is supported, which is the model used by the VOIDWarpedNoise node. ComfyUI does not download optical flow weights automatically; you must place the checkpoint file manually in the `models/optical_flow/` directory.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Yes | List of files in `models/optical_flow/` folder | Optical flow model to load. Files must be placed in the `optical_flow` folder. Today only torchvision's `raft_large.pth` is supported. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `OPTICAL_FLOW` | MODEL | The loaded optical flow model, wrapped in a ModelPatcher for use with other nodes. |

---
**Source fingerprint (SHA-256):** `94bab0bb7e2b9d9b3f343337799eccc744f79275b72a6fad9681b408b4a0820b`
