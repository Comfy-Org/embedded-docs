# Normalize Image Colors

This node normalizes an input image by subtracting a specified mean value from each pixel and then dividing the result by a specified standard deviation. This is a common preprocessing step to standardize pixel values and prepare image data for further processing.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image` | The input image to be normalized. | IMAGE | Yes | - |
| `mean` | Mean value for normalization (default: 0.5). | FLOAT | No | 0.0 - 1.0 |
| `std` | Standard deviation for normalization (default: 0.5). | FLOAT | No | 0.001 - 1.0 |

Note: The normalization is applied to the entire image batch at once, and any batch size is supported.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `image` | The resulting image after the normalization process has been applied. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/en.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
