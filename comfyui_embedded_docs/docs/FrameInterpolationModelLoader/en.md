# Load Frame Interpolation Model

## Overview

This node loads a frame interpolation model from a file and prepares it for use in the workflow. It automatically detects the model type (FILM or RIFE) and configures the model for optimal performance on your hardware.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model_name` | Select a frame interpolation model to load. Models must be placed in the 'frame_interpolation' folder. | COMBO | Yes | List of model files in the `frame_interpolation` folder |

Note: If the selected file is not a recognized FILM or RIFE frame interpolation model, the node raises an error.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | The loaded and configured frame interpolation model, ready for use in other nodes. | INTERP_MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/en.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
