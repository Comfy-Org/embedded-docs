> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/en.md)

Encodes text and sets the resolution conditioning for PixArt Alpha. This node processes text input and adds width and height information to create conditioning data specifically for PixArt Alpha models. It does not apply to PixArt Sigma models.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Yes | 0 to MAX_RESOLUTION | The width dimension for resolution conditioning (default: 1024) |
| `height` | INT | Yes | 0 to MAX_RESOLUTION | The height dimension for resolution conditioning (default: 1024) |
| `text` | STRING | Yes | - | Text input to be encoded, supports multiline input and dynamic prompts |
| `clip` | CLIP | Yes | - | CLIP model used for tokenization and encoding |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Encoded conditioning data with text tokens and resolution information |

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
