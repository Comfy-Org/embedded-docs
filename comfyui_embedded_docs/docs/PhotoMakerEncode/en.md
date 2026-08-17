# PhotoMaker Encode

PhotoMakerEncode creates conditioning data for AI image generation by combining a reference image with a text prompt. It searches the text prompt for the word "photomaker" and, when found, uses the PhotoMaker model to apply the reference image's visual characteristics at that position in the prompt.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `photomaker` | The PhotoMaker model used for processing the reference image and generating image-based embeddings | PHOTOMAKER | Yes | - |
| `image` | The reference image that provides visual characteristics for conditioning | IMAGE | Yes | - |
| `clip` | The CLIP model used for text tokenization and encoding | CLIP | Yes | - |
| `text` | The text prompt for conditioning generation. Supports multiple lines and dynamic prompts (default: "photograph of photomaker") | STRING | Yes | - |

**Note:** The word "photomaker" must appear as a separate word in the text prompt (the match is case-sensitive) for image-based conditioning to be applied. When present, the image's characteristics are injected at that position in the prompt. If "photomaker" is not found, the node returns standard text conditioning without image influence.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `CONDITIONING` | The conditioning data containing image and text embeddings for guiding image generation, along with the pooled output from the CLIP text encoder | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerEncode/en.md)

---
**Source fingerprint (SHA-256):** `490a90c504ade253c2bb055e0efb1eb015ba6d7faf8f2370cac188871f678986`
