# TextEncodeZImageOmni

The TextEncodeZImageOmni node is an advanced conditioning node that encodes a text prompt along with optional reference images into a conditioning format suitable for image generation models. It can process up to three images, optionally encoding them with a vision encoder and/or a VAE to produce reference latents, and integrates these visual references with the text prompt using a specific template structure.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `clip` | The CLIP model used for tokenizing and encoding the text prompt. | CLIP | Yes |  |
| `image_encoder` | An optional vision encoder model. If provided, it will be used to encode the input images, and the resulting embeddings will be added to the conditioning. | CLIPVision | No |  |
| `prompt` | The text prompt to be encoded. This field supports multiline input and dynamic prompts. | STRING | Yes |  |
| `auto_resize_images` | When enabled (default: True), input images will be automatically resized based on their pixel area before being passed to the VAE for encoding. This is an advanced setting. | BOOLEAN | No |  |
| `vae` | An optional VAE model. If provided, it will be used to encode the input images into latent representations, which are added to the conditioning as reference latents. | VAE | No |  |
| `image1` | The first optional reference image. | IMAGE | No |  |
| `image2` | The second optional reference image. | IMAGE | No |  |
| `image3` | The third optional reference image. | IMAGE | No |  |

**Note:** The node can accept a maximum of three images (`image1`, `image2`, `image3`). The `image_encoder` and `vae` inputs are only utilized if at least one image is provided. When `auto_resize_images` is True and a `vae` is connected, images are resized to have a total pixel area close to 1024x1024 pixels, with dimensions rounded to multiples of 8, before encoding. If no images are provided, the node encodes the text prompt without any visual references.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `CONDITIONING` | The final conditioning output, which contains the encoded text prompt and may include encoded image embeddings and/or reference latents if images were provided. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/en.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
