# Pre-Process SeedVR2 Input

This node pads a resized image to prepare it for the SeedVR2 model. It removes the alpha channel during processing, which is later restored by the companion Post-Process SeedVR2 Output node using the original resized image.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `resized_images` | The resized image to process. | IMAGE | Yes | - |

Note: The input can be a single image or a sequence of frames (for example, frames from a video). Its shorter edge must be at least 2 pixels. During processing, the alpha channel (if present) is removed, pixel values are clamped to [0, 1], and the width and height are padded to multiples of 16. Frame sequences are padded so their length follows the pattern 1, 5, 9, 13, ... frames.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The padded image for VAE encoding. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Preprocess/en.md)

---
**Source fingerprint (SHA-256):** `f4fa433d299feba40696f27ff365c59988e5102112f09536724b5db5b09416bb`
