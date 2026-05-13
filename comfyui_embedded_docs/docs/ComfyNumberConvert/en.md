> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/en.md)

The Number Convert node transforms various input data types into numeric values. It accepts a single input of type integer, float, string, or boolean and produces two outputs: a floating-point number and an integer. This is useful for converting text or logical values into a format that can be used by other mathematical or processing nodes in your workflow.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `value` | INT, FLOAT, STRING, BOOLEAN | Yes | N/A | The value to be converted into numeric outputs. Accepts an integer, a floating-point number, a text string, or a true/false boolean. |

**Note:** When the input is a string, it must not be empty and must contain a valid representation of a number (e.g., `"123"`, `"3.14"`). The node will raise an error for empty strings, text that cannot be parsed as a number, or values that are not finite (like `"inf"` or `"nan"`). For boolean inputs, `true` converts to 1.0 (FLOAT) and 1 (INT), while `false` converts to 0.0 (FLOAT) and 0 (INT). For float inputs, the integer output is obtained by truncating the decimal portion.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | The input value converted to a floating-point number. |
| `INT` | INT | The input value converted to an integer. For float inputs, this performs a truncation. |

---
**Source fingerprint (SHA-256):** `961fbea05b22c68f768f9ecaae2ee455b1913afe4a65d8c0e6b6497b1e24ce72`
