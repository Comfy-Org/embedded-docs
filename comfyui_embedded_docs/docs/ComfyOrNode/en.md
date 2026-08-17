# Or

The ComfyOrNode performs a logical OR operation on a set of input values. It returns `true` if any of the provided values are considered truthy according to Python's standard truthiness rules.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `value` | A value to evaluate for truthiness. You can provide multiple values by adding more inputs. The node returns `true` if any of these values is truthy. | ANY | Yes | Minimum 1 value; multiple values accepted |

**Note:** The node accepts a minimum of 1 input value. You can add more inputs as needed using the autogrow feature.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `BOOLEAN` | Returns `true` if any of the input values is truthy; returns `false` if all input values are falsy. | BOOLEAN |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/en.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
