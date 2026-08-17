# LTXVImgToVideo

The LTXVImgToVideo node prepares a latent representation for generating a video from an input image. The image is resized to the requested width and height, encoded with the VAE, and placed in the first latent frames. A noise mask is created using `strength` to control how much of the original image content is preserved or modified, and the positive and negative conditioning are passed through unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Positive conditioning data provided as input and returned unchanged. | CONDITIONING | Yes | - |
| `negative` | Negative conditioning data provided as input and returned unchanged. | CONDITIONING | Yes | - |
| `vae` | VAE model used to encode the input image into latent space. | VAE | Yes | - |
| `image` | Input image that is resized and encoded to form the beginning of the video latent. | IMAGE | Yes | - |
| `width` | Output video width in pixels (default: 768, step: 32). | INT | Yes | 64 to MAX_RESOLUTION |
| `height` | Output video height in pixels (default: 512, step: 32). | INT | Yes | 64 to MAX_RESOLUTION |
| `length` | Number of frames in the generated video (default: 97, step: 8). | INT | Yes | 9 to MAX_RESOLUTION |
| `batch_size` | Number of videos to generate in one latent batch (default: 1). | INT | Yes | 1 to 4096 |
| `strength` | Controls how much of the encoded image content is preserved in the first latent frames. A value of 1.0 preserves the original image completely, while 0.0 allows maximum modification (default: 1.0). | FLOAT | Yes | 0.0 to 1.0 |

Note: `MAX_RESOLUTION` is the maximum resolution allowed by the ComfyUI installation.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Positive conditioning passed through without modification. | CONDITIONING |
| `negative` | Negative conditioning passed through without modification. | CONDITIONING |
| `latent` | Video latent containing the encoded input image at the start of the sequence, together with a noise mask based on `strength`. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/en.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
