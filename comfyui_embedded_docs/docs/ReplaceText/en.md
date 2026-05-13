> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/en.md)

The Replace Text node performs a simple text substitution. It searches for a specified piece of text within the input and replaces every occurrence with a new piece of text. The operation is applied to all text inputs provided to the node.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Yes | - | The text to process. |
| `find` | STRING | Yes | - | Text to find (default: empty string). |
| `replace` | STRING | Yes | - | Text to replace with (default: empty string). |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `text` | STRING | The processed text with all occurrences of the `find` text replaced by the `replace` text. |

---
**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`
