> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/en.md)

## Overview

Loads a background removal model from a file. This node prepares the model for use in removing backgrounds from images.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `bg_removal_name` | STRING | Yes | List of available model files | The model used to remove backgrounds from images. Select from the list of available background removal model files. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `bg_model` | BACKGROUND_REMOVAL | The loaded background removal model, ready to be used by other nodes for processing images. |