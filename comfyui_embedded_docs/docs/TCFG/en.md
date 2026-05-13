> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/en.md)

TCFG (Tangential Damping CFG) refines the unconditional (negative) predictions to better align with the conditional (positive) predictions during the sampling process. This technique improves output quality by applying tangential damping to the unconditional guidance, based on the research paper 2503.18137. The node modifies the model's sampling behavior by adjusting how unconditional predictions are processed during classifier-free guidance.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | - | The model to apply tangential damping CFG to |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `patched_model` | MODEL | The modified model with tangential damping CFG applied |

---
**Source fingerprint (SHA-256):** `de6b4deb8a42f05dff90e393bff1e0b4b8ed58887586ca81c236e1a780be5776`
