# LatentApplyOperationCFG

The LatentApplyOperationCFG node applies a latent operation to modify the conditioning guidance process in a model. It works by intercepting the conditioning outputs during the classifier-free guidance (CFG) sampling process and applying the specified operation to the latent representations before they are used for generation.

When the model produces two conditioning outputs (for example, positive and negative conditioning), the operation is applied to the difference between them, and the second conditioning is then added back. When there is only one conditioning output, the operation is applied to it directly. This node is marked as experimental.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to which the CFG operation will be applied | MODEL | Yes | - |
| `operation` | The latent operation to apply during the CFG sampling process | LATENT_OPERATION | Yes | - |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with the CFG operation applied to its sampling process | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/en.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
