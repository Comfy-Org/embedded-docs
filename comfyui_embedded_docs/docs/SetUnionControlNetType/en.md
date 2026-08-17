# Set Union ControlNet Type

The SetUnionControlNetType node lets you set the control type of a control network used for conditioning. It takes an existing control network, creates a modified copy of it, and stores the selected control type in that copy so the original remains unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `control_net` | The control network to copy and modify with the selected control type | CONTROL_NET | Yes | - |
| `type` | The control type to apply to the copied control network. Select "auto" to leave the control type unset, or choose a specific type from the available union control network types (default: "auto") | COMBO | Yes | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

Note: When `type` is "auto", the control type list on the copied control network is cleared. When a specific type is selected, the copied control network stores the corresponding type number.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `control_net` | The modified copy of the control network with the selected control type applied | CONTROL_NET |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/en.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
