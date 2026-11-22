# TypeSafe Jev (Yes/No)

The TypeSafe Jev (Yes/No) node asks a yes or no question about connected text, images, or both and returns the answer as a boolean. Connect `result` to an If/Else Switch node to route the workflow, or read `probability` to act on how sure the model is. This is an API node: it runs on Comfy's servers and needs a Comfy.org account with credits.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | Jev model to use. Only one model is currently available: `jev-1.14.0`. | COMBO | Yes | `"jev-1.14.0"` |
| `question` | The yes or no question the connected text and images answer. Ask it so that yes is the case you act on; with several image sockets, use their names, for example `Does image_2 show the same person as image_1?` (default: `Is there a person in the image?`). | STRING | Yes | 1 to 1000 characters |
| `threshold` | The answer is yes when the probability of yes is at least this value (default: 0.5). | FLOAT | Yes | 0.01 to 0.99 (step 0.01) |
| `images` | The images the question is about. Up to 32 images in total; a batched input counts once per image. The long side of every image is capped by the total number of images: 1568 px for up to 4 images, 1024 px for up to 8, 768 px for up to 16 and 512 px for up to 32, so a larger batch can reduce the detail in every image. | AUTOGROW | No | 0 to 32 images |
| `text` | The text the question is about, such as a prompt or an LLM response. | STRING | No | 0 to 3000 characters |

**Notes:**

- Connect text or at least one image; the node raises an error when both are empty.
- `result` is true when `probability` is at least `threshold`, and `answer` returns the same verdict as `yes` or `no`.
- Billing is token-based; the price badge on the node shows the approximate rate per 1M tokens.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `result` | The answer as a boolean: true when the probability of yes is at least `threshold`. | BOOLEAN |
| `answer` | The answer as the text `yes` or `no`. | STRING |
| `probability` | Probability of yes, from 0 (definitely no) to 1 (definitely yes). | FLOAT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/en.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
