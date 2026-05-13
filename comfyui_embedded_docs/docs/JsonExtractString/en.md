> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/en.md)

The JsonExtractString node reads a text string containing JSON data and extracts the value associated with a specific key. It converts the extracted value into a string. If the JSON is invalid, the key is not found, or the value is null, the node returns an empty string.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `json_string` | STRING | Yes | N/A | The text containing the JSON data to be parsed. |
| `key` | STRING | Yes | N/A | The specific key whose string value you want to extract from the JSON object. |

**Note:** The node only extracts values from JSON objects (dictionaries). If the parsed JSON is not an object or if the specified key does not exist within it, the output will be an empty string.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | STRING | The string value extracted from the JSON for the specified key, or an empty string if the extraction fails. |

---
**Source fingerprint (SHA-256):** `f05e2d9fd4888870a844c85ac7543d6c38c1c56f2ef22a402fc93ee716743612`
