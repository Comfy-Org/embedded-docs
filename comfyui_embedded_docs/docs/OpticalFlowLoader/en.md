# Load Optical Flow Model

## Overview

Loads an optical flow model from the `models/optical_flow/` folder. Currently, only torchvision's RAFT-large format is supported, which is the model used by the VOIDWarpedNoise node. ComfyUI does not download optical flow weights automatically; you must place the checkpoint file manually in the `models/optical_flow/` directory.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model_name` | Optical flow model to load. Files must be placed in the `optical_flow` folder. Today only torchvision's `raft_large.pth` is supported. | COMBO | Yes | List of files in `models/optical_flow/` folder |

The selected file must be a torchvision RAFT-large checkpoint. The node checks that the file contains the expected RAFT keys (`feature_encoder.*`, `context_encoder.*`, and `update_block.*`) and raises a ValueError if the format is not recognized.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `OPTICAL_FLOW` | The loaded optical flow model, wrapped in a ModelPatcher for use with other nodes. | OPTICAL_FLOW |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/en.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
