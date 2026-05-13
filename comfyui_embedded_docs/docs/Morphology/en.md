> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/en.md)

The Morphology node applies various morphological operations to images, which are mathematical operations used to process and analyze shapes in images. It can perform operations like erosion, dilation, opening, closing, and more using a customizable kernel size to control the effect strength.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to process |
| `operation` | STRING | Yes | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | The morphological operation to apply (default: "erode") |
| `kernel_size` | INT | Yes | 3-999 | The size of the structuring element kernel (default: 3). Must be an odd number. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The processed image after applying the morphological operation |

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
