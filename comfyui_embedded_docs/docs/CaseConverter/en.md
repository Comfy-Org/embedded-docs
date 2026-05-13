> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/en.md)

The Case Converter node transforms text strings into different letter case formats. It takes an input string and converts it based on the selected mode, producing an output string with the specified case formatting applied. The node supports four different case conversion options to modify the capitalization of your text.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | Yes | - | The text string to be converted to a different case format |
| `mode` | STRING | Yes | `"UPPERCASE"`<br>`"lowercase"`<br>`"Capitalize"`<br>`"Title Case"` | The case conversion mode to apply (default: `"UPPERCASE"`) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | STRING | The input string converted to the specified case format |

---
**Source fingerprint (SHA-256):** `2493daccd5bdd86ce3fb24c6658057f5e50c2d6ed7616785f40806826f9a60dc`
