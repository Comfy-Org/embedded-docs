# Load CLIP (Triple)

The TripleCLIPLoader node loads three text encoder models at the same time and combines them into a single CLIP model. This is useful for advanced text encoding scenarios where multiple text encoders are needed, such as in SD3 workflows that require clip-l, clip-g, and t5 models working together.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | The first text encoder model to load from the available text encoders | COMBO | Yes | All text encoder files in the text_encoders folder |
| `clip_name2` | The second text encoder model to load from the available text encoders | COMBO | Yes | All text encoder files in the text_encoders folder |
| `clip_name3` | The third text encoder model to load from the available text encoders | COMBO | Yes | All text encoder files in the text_encoders folder |

**Note:** All three text encoder parameters must be selected from the available text encoder models in your system. The node loads all three models in the given order and combines them into a single CLIP model for processing. For SD3 workflows, use clip-l, clip-g, and t5 as the three encoders.

## Outputs

| Output Name | Description | Data Type |
|-----------|-------------|-----------|
| `CLIP` | A combined CLIP model containing all three loaded text encoders | CLIP |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/en.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
