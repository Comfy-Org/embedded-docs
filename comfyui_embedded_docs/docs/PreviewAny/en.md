# Preview as Text

The PreviewAny node accepts any input value and displays it as readable text in the interface. It is designed for inspecting and debugging values at any point in a workflow: strings are shown as-is, numbers and booleans are converted to text, and other objects are formatted as JSON. The converted text is also passed on as a string output so it can be used by other nodes.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `source` | The value to preview as text. Accepts any data type. Strings are passed through unchanged; numbers and booleans are converted to text; other values are serialized to JSON with indentation. If JSON serialization fails, the value's plain string representation is used, and if that also fails, the text "source exists, but could not be serialized." is displayed. | ANY | Yes | Any data type |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `UI Text Display` | Shows the input data converted to text in the user interface. The same text is also returned as a string output for further processing by other nodes. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/en.md)

---
**Source fingerprint (SHA-256):** `9572eac396aa27a83148a940e4bf37a9ec4e4a47e9526db8bb983611f9237536`
