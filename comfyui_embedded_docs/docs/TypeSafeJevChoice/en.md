# TypeSafe Jev (Choice)

The TypeSafe Jev (Choice) node picks one of your own options for connected text, images, or both. Connect `choice` to a Branch node whose inputs carry the option names, or use `option_index` to switch on the position of the chosen option. A Branch node takes at most 32 inputs, so a list with more options than that can only be routed by `option_index`. This is an API node: it runs on Comfy's servers and needs a Comfy.org account with credits.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | Jev model to use. Only one model is currently available: `jev-1.14.0`. | COMBO | Yes | `"jev-1.14.0"` |
| `question` | The question the options answer. With several image sockets, use their names, for example `Which season is shown in image_1?` (default: `What style is the image?`). | STRING | Yes | 1 to 1000 characters |
| `options` | The options to choose from, one per line. Leading and trailing whitespace is trimmed from each line, and options must be unique ignoring case, so a repeated option or two options that differ only in case are rejected. Add an option such as `other` for inputs that fit none of them (default: `photo`, `illustration`, `3d render`, `anime`, `sketch` and `other`, one per line). | STRING | Yes | 2 to 50 options, up to 40 characters each |
| `images` | The images the question is about. Up to 32 images in total; a batched input counts once per image. The long side of every image is capped by the total number of images: 1568 px for up to 4 images, 1024 px for up to 8, 768 px for up to 16 and 512 px for up to 32, so a larger batch can reduce the detail in every image. | AUTOGROW | No | 0 to 32 images |
| `text` | The text the question is about, such as a prompt or an LLM response. | STRING | No | 0 to 3000 characters |

**Notes:**

- Connect text or at least one image; the node raises an error when both are empty.
- The node raises an error when fewer than 2 or more than 50 options are given, when an option is longer than 40 characters, or when two options are the same ignoring case.
- `option_index` counts from 0, so the first option in the list has index 0.
- Billing is token-based; the price badge on the node shows the approximate rate per 1M tokens.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `choice` | The chosen option, with leading and trailing whitespace trimmed. A Branch input whose name keeps those spaces will not match. | STRING |
| `option_index` | Position of the chosen option in the options list, starting at 0. | INT |
| `confidence` | How sure Jev is, from 0 (no clear winner) to 1 (certain). | FLOAT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/en.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
