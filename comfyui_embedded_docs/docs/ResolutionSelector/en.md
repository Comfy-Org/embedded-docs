> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/en.md)

The Resolution Selector node calculates the pixel width and height for an image based on a chosen aspect ratio and a target total resolution in megapixels. It is useful for generating consistent dimensions for other nodes, such as the Empty Latent Image node. The output dimensions are always rounded to the nearest multiple of 8.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | Yes | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | The aspect ratio for the output dimensions (default: `"SQUARE"`). |
| `megapixels` | FLOAT | Yes | 0.1 - 16.0 | Target total megapixels. 1.0 MP ≈ 1024×1024 for a square aspect ratio (default: 1.0). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `width` | INT | The calculated width in pixels, which is a multiple of 8. |
| `height` | INT | The calculated height in pixels, which is a multiple of 8. |