# Post-Process SeedVR2 Output

This node aligns the generated image with the original resized image and applies optional color correction. It takes the output of a SeedVR2 upscaling process and adjusts it to match the colors and dimensions of the original reference image.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | The generated image to process. | IMAGE | Yes | - |
| `original_resized_images` | The original resized image before pre-processing, used as reference. | IMAGE | Yes | - |
| `color_correction_method` | Method to match the generated image colors to the original image. lab: transfer color in CIELAB space, preserving detail (most faithful). wavelet: transfer low-frequency color, keeping upscaled high-frequency detail. adain: match per-channel mean/std (fastest, global tint). none: skip color transfer (geometry alignment only). (default: "lab") | COMBO | Yes | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Note:** The output is cropped to the smaller height and width of the generated and reference images, and the final dimensions are rounded down to even numbers. If the reference image has an alpha channel (4 channels), it is preserved and applied to the output. Both inputs can be 4D or 5D image tensors, and the output uses the same dimensionality as the generated image input.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The aligned, color-corrected image. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/en.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
