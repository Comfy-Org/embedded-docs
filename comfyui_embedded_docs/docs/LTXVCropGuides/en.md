# LTXVCropGuides

The LTXVCropGuides node processes conditioning and latent inputs for video generation by removing keyframe information and adjusting the latent dimensions. It crops the latent image and noise mask to exclude keyframe sections while clearing keyframe indices from both positive and negative conditioning inputs. This prepares the data for video generation workflows that don't require keyframe guidance.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | The positive conditioning input containing guidance information for generation | CONDITIONING | Yes | - |
| `negative` | The negative conditioning input containing guidance information for what to avoid in generation | CONDITIONING | Yes | - |
| `latent` | The latent representation containing image samples and noise mask data | LATENT | Yes | - |

Note: If the positive conditioning contains no keyframe indices, the node returns the positive, negative, and latent inputs unchanged.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | The processed positive conditioning with keyframe indices and guide attention entries cleared | CONDITIONING |
| `negative` | The processed negative conditioning with keyframe indices and guide attention entries cleared | CONDITIONING |
| `latent` | The cropped latent representation with adjusted samples and noise mask, where keyframe sections have been removed | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/en.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
