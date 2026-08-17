# StableZero123_Conditioning_Batched

The StableZero123_Conditioning_Batched node prepares the conditioning data needed to generate 3D views of an object with the Stable Zero123 model. It encodes an input image with a CLIP vision model and a VAE, combines the image features with camera elevation and azimuth angles for every item in a batch, and outputs positive and negative conditioning together with an empty latent. The batch increment inputs raise or lower the camera angle for each consecutive item in the batch.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `clip_vision` | The CLIP vision model used to encode the input image into image embeddings | CLIP_VISION | Yes | - |
| `init_image` | The initial input image to be processed and encoded | IMAGE | Yes | - |
| `vae` | The VAE model used to encode image pixels into the latent space | VAE | Yes | - |
| `width` | Target width of the processed image (default: 256) | INT | Yes | 16 to MAX_RESOLUTION (step 8) |
| `height` | Target height of the processed image (default: 256) | INT | Yes | 16 to MAX_RESOLUTION (step 8) |
| `batch_size` | Number of conditioning samples to generate in the batch (default: 1) | INT | Yes | 1 to 4096 |
| `elevation` | Starting camera elevation angle in degrees (default: 0.0) | FLOAT | Yes | -180.0 to 180.0 (step 0.1) |
| `azimuth` | Starting camera azimuth angle in degrees (default: 0.0) | FLOAT | Yes | -180.0 to 180.0 (step 0.1) |
| `elevation_batch_increment` | Amount added to the elevation angle for each consecutive item in the batch (default: 0.0, advanced parameter) | FLOAT | Yes | -180.0 to 180.0 (step 0.1) |
| `azimuth_batch_increment` | Amount added to the azimuth angle for each consecutive item in the batch (default: 0.0, advanced parameter) | FLOAT | Yes | -180.0 to 180.0 (step 0.1) |

**Note:** The `width` and `height` values must be multiples of 8 (the selection step of 8 enforces this) because the node divides them by 8 to build the latent dimensions. For each item in the batch, the `elevation` and `azimuth` values are increased by `elevation_batch_increment` and `azimuth_batch_increment`, so consecutive batch items receive step-by-step camera angles.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning combining the image embeddings, the camera embeddings, and the encoded input image used for concatenation during generation | CONDITIONING |
| `negative` | Negative conditioning using zero-initialized image embeddings and a zero latent for concatenation | CONDITIONING |
| `latent` | Empty latent tensor with dimensions (batch_size, 4, height/8, width/8) and batch index information | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/en.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
