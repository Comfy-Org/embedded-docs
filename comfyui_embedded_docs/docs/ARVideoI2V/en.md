# ARVideoI2V

## Overview

This node prepares an image-to-video generation setup for AR (Auto-Regressive) video models. It takes a starting image, encodes it into the latent space using a VAE, and stores the encoded image in the model's configuration. This allows the video sampling process to use the image as the first frame, effectively seeding the generation without needing a separate image-to-video model architecture.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The AR video model to be used for generation. | MODEL | Yes | - |
| `vae` | The VAE model used to encode the starting image into latent space. | VAE | Yes | - |
| `start_image` | The initial image that will serve as the first frame of the generated video. | IMAGE | Yes | - |
| `width` | The width of the generated video frames (default: 832). | INT | Yes | 16 to 8192 (step: 16) |
| `height` | The height of the generated video frames (default: 480). | INT | Yes | 16 to 8192 (step: 16) |
| `length` | The total number of frames in the generated video (default: 81). | INT | Yes | 1 to 1024 (step: 4) |
| `batch_size` | The number of video sequences to generate in a single batch (default: 1). | INT | Yes | 1 to 64 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `MODEL` | The cloned model with the encoded start image stored in its configuration for video generation. | MODEL |
| `LATENT` | An empty latent tensor with shape [batch_size, 16, lat_t, height/8, width/8], where lat_t = ((length - 1) // 4) + 1 is the number of latent frames derived from the requested video length. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/en.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
