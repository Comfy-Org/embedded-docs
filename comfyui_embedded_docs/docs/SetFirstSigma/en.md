# SetFirstSigma

The SetFirstSigma node modifies a sequence of sigma values by replacing the first sigma value in the sequence with a custom value. It takes an existing sigma sequence and a new sigma value as inputs, then returns a new sigma sequence where only the first element has been changed while keeping all other sigma values unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `sigmas` | The input sequence of sigma values to be modified | SIGMAS | Yes | - |
| `sigma` | The new sigma value to set as the first element in the sequence (default: 136.0) | FLOAT | Yes | 0.0 to 20000.0 |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sigmas` | The modified sigma sequence with the first element replaced by the custom sigma value | SIGMAS |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/en.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
