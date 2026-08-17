# AutogrowPrefixTestNode

The AutogrowPrefixTestNode is a logic node designed to test the autogrow input feature. It accepts a dynamic number of float inputs, combines their values into a comma-separated string, and outputs that string.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `autogrow` | A dynamic input group that accepts float values. The group can hold between 1 and 10 float inputs, and the node processes all provided values. | FLOAT | Yes | 1 to 10 inputs |

**Note:** The `autogrow` input is a special dynamic input that can be expanded to add more float inputs up to a maximum of 10. The minimum is 1 input. The `min` and `max` values in this node define the allowed number of inputs in the group, not the value range of each individual float.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | A single string containing all the input float values, separated by commas. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/en.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
