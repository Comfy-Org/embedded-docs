# InstructPixToPixConditioning

The InstructPixToPixConditioning node prepares conditioning data for InstructPix2Pix image editing by combining an input image with positive and negative text-prompt conditioning. It encodes the image with the VAE into a latent representation, attaches that latent to both conditioning sets, and creates a zero-filled latent with matching dimensions. If the image width or height is not a multiple of 8 pixels, the image is cropped automatically before encoding.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning data containing text prompts and settings for desired image characteristics. | CONDITIONING | Yes | - |
| `negative` | Negative conditioning data containing text prompts and settings for undesired image characteristics. | CONDITIONING | Yes | - |
| `vae` | VAE model used to encode the input image into a latent representation. | VAE | Yes | - |
| `pixels` | Input image to be processed and encoded into latent space. | IMAGE | Yes | - |

**Note:** The input image is automatically cropped to a multiple of 8 pixels in both width and height, rounding down, to ensure compatibility with the VAE encoding process.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning data with the encoded image latent attached. | CONDITIONING |
| `negative` | Negative conditioning data with the encoded image latent attached. | CONDITIONING |
| `latent` | Zero-filled latent tensor with the same dimensions as the encoded image. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InstructPixToPixConditioning/en.md)

---
**Source fingerprint (SHA-256):** `e9a5a05cdeafe9337ca2033111f1ad4f7314fa33d71a4764f62919857efc79f4`
