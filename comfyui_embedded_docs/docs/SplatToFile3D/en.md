# Create 3D File (from Splat)

SplatToFile3D converts a gaussian splat into a File3D object that can be used with Save or Preview 3D nodes. You can choose the output file format. The node supports one item per batch only; if it receives more than one item, it uses the first and logs a warning.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `splat` | The gaussian splat data to serialize into a file. Only one item per batch is supported. If more than one item is provided, only the first is used. | SPLAT | Yes | - |
| `format` | The output file format for the 3D file. ply: standard 3D Gaussian Splat with full spherical harmonics. ksplat: mkkellogg SplatBuffer (level 0, uncompressed), base color only. spz: Niantic gzip-compressed (~10x smaller), base color only (default: "ply") | COMBO | Yes | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model_3d` | A File3D object containing the serialized gaussian splat data in the selected format, ready for saving or previewing | FILE3D |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/en.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
