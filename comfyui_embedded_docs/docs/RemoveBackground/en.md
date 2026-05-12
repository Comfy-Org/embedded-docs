> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/en.md)

## Overview

The Remove Background node uses a background removal model to generate a mask that separates the foreground subject from the background of an input image. It takes an image and a background removal model, then produces a mask highlighting the main subject.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | N/A | Input image to remove the background from |
| `bg_removal_model` | BACKGROUND_REMOVAL_MODEL | Yes | N/A | Background removal model used to generate the mask |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `mask` | MASK | Generated foreground mask that highlights the main subject of the input image |