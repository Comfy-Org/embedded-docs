# LatentApplyOperation

The LatentApplyOperation node applies a specified operation to latent samples. It takes latent data and an operation as inputs, copies the input latent samples, applies the operation to the latent tensor, and returns the modified latent data. This node allows you to transform or manipulate latent representations in your workflow.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `samples` | The latent samples to be processed by the operation | LATENT | Yes | - |
| `operation` | The operation to apply to the latent samples | LATENT_OPERATION | Yes | - |

Note: This node is marked as experimental. The operation is applied to the latent tensor stored under the `samples` key of the latent structure. The input latent samples are copied before the operation is applied, so the original input latent data is not modified.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | The modified latent samples after applying the operation | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/en.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
