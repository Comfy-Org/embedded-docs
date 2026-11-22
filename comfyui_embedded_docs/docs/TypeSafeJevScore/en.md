# TypeSafe Jev (Score)

The TypeSafe Jev (Score) node rates connected text, images, or both from 1 to 10 and compares the rating with a threshold. Connect `result` to an If/Else Switch node to act on the score, or read `score` to use the raw rating. This is an API node: it runs on Comfy's servers and needs a Comfy.org account with credits.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | Jev model to use. Only one model is currently available: `jev-1.14.0`. | COMBO | Yes | `"jev-1.14.0"` |
| `question` | What to rate, on a scale from 1 to 10. Say what 1 and 10 mean, as in the default (default: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Yes | 1 to 1000 characters |
| `threshold` | `result` is true when the score is at least this value (default: 5.0). | FLOAT | Yes | 1.0 to 10.0 (step 0.1) |
| `images` | The images the question is about. Up to 32 images in total; a batched input counts once per image. The long side of every image is capped by the total number of images: 1568 px for up to 4 images, 1024 px for up to 8, 768 px for up to 16 and 512 px for up to 32, so a larger batch means less detail in every image. | AUTOGROW | No | 0 to 32 images |
| `text` | The text the question is about, such as a prompt or an LLM response. | STRING | No | 0 to 3000 characters |

**Notes:**

- Connect text or at least one image; the node raises an error when both are empty.
- The score is reported from 1 to 10, and `result` is true when it is at least `threshold`.
- Billing is token-based; the price badge on the node shows the approximate rate per 1M tokens.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `result` | True when `score` is at least `threshold`. | BOOLEAN |
| `score` | The rating from 1 (worst) to 10 (best). | FLOAT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/en.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
