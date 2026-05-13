> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/en.md)

## Overview

This node loads a frame interpolation model from a file and prepares it for use in the workflow. It automatically detects the model type (FILM or RIFE) and configures the model for optimal performance on your hardware.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Yes | List of model files in the `frame_interpolation` folder | Select a frame interpolation model to load. Models must be placed in the 'frame_interpolation' folder. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `FRAME_INTERPOLATION_MODEL` | MODEL | The loaded and configured frame interpolation model, ready for use in other nodes. |

---
**Source fingerprint (SHA-256):** `497c20d5123bcbfd321dc4a659250ce3e0903e55c3a0274d3ed45710d75573d9`
