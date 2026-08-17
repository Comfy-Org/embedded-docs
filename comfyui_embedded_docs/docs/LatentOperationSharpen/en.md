# LatentOperationSharpen

The LatentOperationSharpen node applies a sharpening effect to latent representations using a Gaussian kernel. It works by normalizing the latent data, applying a convolution with a custom sharpening kernel, and then restoring the original luminance. This enhances the details and edges in the latent space representation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | The radius of the sharpening kernel. The full kernel size is calculated as twice this value plus one (default: 9). | INT | Yes | 1-31 |
| `sigma` | The standard deviation of the Gaussian kernel (default: 1.0). | FLOAT | Yes | 0.1-10.0 |
| `alpha` | The sharpening intensity factor that controls the strength of the effect (default: 0.1). | FLOAT | Yes | 0.0-5.0 |

All inputs are advanced parameters. This node is marked as experimental.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `operation` | A sharpening operation that can be applied to latent data. Applying it to a latent returns a sharpened version with the original luminance preserved. | LATENT_OPERATION |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/en.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
