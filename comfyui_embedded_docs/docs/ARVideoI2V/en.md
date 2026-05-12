> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/en.md)

## Overview

This node prepares an image-to-video generation setup for AR (Auto-Regressive) video models. It takes a starting image, encodes it into the latent space using a VAE, and stores the encoded image in the model's configuration. This allows the video sampling process to use the image as the first frame, effectively seeding the generation without needing a separate image-to-video model architecture.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | - | The AR video model to be used for generation. |
| `vae` | VAE | Yes | - | The VAE model used to encode the starting image into latent space. |
| `start_image` | IMAGE | Yes | - | The initial image that will serve as the first frame of the generated video. |
| `width` | INT | Yes | 16 to 8192 (step: 16) | The width of the generated video frames (default: 832). |
| `height` | INT | Yes | 16 to 8192 (step: 16) | The height of the generated video frames (default: 480). |
| `length` | INT | Yes | 1 to 1024 (step: 4) | The total number of frames in the generated video (default: 81). |
| `batch_size` | INT | Yes | 1 to 64 | The number of video sequences to generate in a single batch (default: 1). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `MODEL` | MODEL | The cloned model with the encoded start image stored in its configuration for video generation. |
| `LATENT` | LATENT | An empty latent tensor with the correct dimensions for the video generation process. |