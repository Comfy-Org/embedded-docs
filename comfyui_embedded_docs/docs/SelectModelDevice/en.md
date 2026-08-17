# Select Model Device

The SelectModelDevice node lets you choose which device (CPU or a specific GPU) a diffusion model runs on. Depending on the selected option, it restores the loader's original device, pins the model to the CPU, or moves it to a specific GPU, and it automatically handles conflicts with other multi-GPU nodes.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The diffusion model to place on a specific device. | MODEL | Yes |  |
| `device` | The target device for the model. Options are dynamically generated based on available GPUs. (default: "default") | COMBO | Yes | `"default"`<br>`"cpu"`<br>`"gpu:N"` for each available GPU (e.g. `"gpu:0"`, `"gpu:1"`, ...) |

**Parameter Details:**
- `"default"`: Restores the device assigned by the model loader, even if a previous SelectModelDevice node changed it.
- `"cpu"`: Pins both the load and offload device to the CPU.
- `"gpu:N"`: Pins the load device to the Nth available GPU (e.g., `"gpu:0"` for the first GPU). The offload device is restored to the loader's original choice.

**Important Notes:**
- Unknown `"gpu:N"` values are accepted at validation time so portable workflows do not fail on machines with fewer GPUs. At runtime, a device that is not available causes the model to be passed through unchanged with a log message.
- If the requested device does not exist on the current machine (e.g., a workflow created on a 2-GPU machine is opened on a 1-GPU machine), the node passes the model through unchanged and logs a message instead of failing.
- If the model is already on the requested device, the node takes a fast path and does not reload the model.
- When the requested device differs from the current one, a fresh model is created using the loader's reload factory, so the returned model has independent weights on the new device. Loaders that do not support this cause the node to pass the model through unchanged with a warning.
- If the workflow already has MultiGPU CFG Split applied and the chosen GPU matches one of the existing multigpu clones, that clone is removed so two patchers do not end up bound to the same device.
- Placing this node *after* a node that has already consumed the model (e.g., a KSampler) is not recommended, as any state changed by the prior node will be observed if the device matches the original.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The diffusion model, now placed on the selected device. If the device was invalid or unavailable, the model is passed through unchanged. | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/en.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
