# TypeSafe Jev (Pick Image)

The TypeSafe Jev (Pick Image) node picks one image out of a batch. Connect `index` to Get Image from Batch to keep the picked image, or read `confidence` to decide whether the pick is good enough. This is an API node and requires a Comfy.org account and API key.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | Jev model to use. Only one model is currently available: `jev-1.14.0`. | COMBO | Yes | `"jev-1.14.0"` |
| `question` | Which image to pick. Connect the prompt to `text` to pick the image that matches it best (default: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Yes | 1 to 1000 characters |
| `images` | The images to choose from. A batched input counts once per image, so every image in the batch is a candidate. | IMAGE | Yes | 2 to 32 images |
| `text` | The text the question is about, such as the prompt the images were made from. | STRING | No | 0 to 3000 characters |

**Notes:**

- The node raises an error when fewer than 2 or more than 32 images are connected.
- `index` counts from 0, which is the position Get Image from Batch expects.
- Billing is token-based; the price badge on the node shows the approximate rate per 1M tokens.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `index` | Position of the picked image in the batch, starting at 0. | INT |
| `confidence` | How sure Jev is, from 0 (no clear winner) to 1 (certain). | FLOAT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/en.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
