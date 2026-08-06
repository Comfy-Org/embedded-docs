# Empty Qwen Image Layered Latent

The Empty Qwen Image Layered Latent node creates a blank, multi-layered latent for the Qwen-Image-Layered model. It generates a tensor filled with zeros, sized for a batch, a stack of layers, and the spatial dimensions you request. This empty latent is the starting point of a layered generation, in the same way an empty latent image is the starting point of an ordinary one.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `width` | The width of the latent image to create. The value must be divisible by 16. (default: 640) | INT | Yes | 16 to MAX_RESOLUTION |
| `height` | The height of the latent image to create. The value must be divisible by 16. (default: 640) | INT | Yes | 16 to MAX_RESOLUTION |
| `layers` | How many layers the image is decomposed into. The model also regenerates the full image, so the latent is allocated with `layers + 1` slots and a decoded generation gives you `layers + 1` images. Setting this to `0` is allowed and gives you the full image on its own. (default: 3) | INT | Yes | 0 to MAX_RESOLUTION |
| `batch_size` | The number of latent samples to generate in a batch. (default: 1) | INT | No | 1 to 4096 |

**Note:** The `width` and `height` parameters are internally divided by 8 to determine the spatial dimensions of the output latent tensor.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | A latent tensor filled with zeros. Its shape is `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Why there is one more slot than layers

Qwen-Image-Layered is an image generation model that regenerates the full image as well as the layers, so the third axis of the latent holds `layers + 1` entries. Set `layers` to 2 and you get the full image plus 2 layers. Set it to 0 and you get the full image only.

- **The first image is the full image, not a layer.** It repeats content you already have, so discard it when you only want the layers.
- **Compositing all of the layers together recreates the full image.** Stacking them is a useful check that the decomposition worked.
- **Layer order is positional.** The layers sit on the temporal axis of the latent, the same axis video models use for frames. LatentCutToBatch with `dim` set to `t` moves that axis into the batch dimension, so after VAE Decode each layer is a separate image and its order is its index in the batch. There is no z-index field and no per-layer metadata carrying that order, so reordering or filtering the batch reorders the layers.
- The Qwen-Image-Layered VAE decodes to 4 channels, so decoded layers carry an alpha channel.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/en.md)

---
**Source fingerprint (SHA-256):** `fe97966663c534dd347aa49a908a8026f2c34716631f1d17be97d74eacc3574e`
