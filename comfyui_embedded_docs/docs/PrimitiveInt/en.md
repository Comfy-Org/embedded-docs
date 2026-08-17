# Int

The PrimitiveInt node provides a simple way to work with integer values in your workflow. It takes an integer input and outputs the same value, making it useful for passing integer parameters between nodes or setting specific numeric values for other operations.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `value` | The integer value to output (default: 0) | INT | Yes | -9223372036854775807 to 9223372036854775807 |

Note: The `value` parameter is set to a fixed control-after-generate behavior, so the value does not change automatically after each generation.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | The input integer value passed through unchanged | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/en.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
