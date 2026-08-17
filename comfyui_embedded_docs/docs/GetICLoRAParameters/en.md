# Get IC-LoRA Parameters

## Overview

This node extracts IC-LoRA parameters from the metadata of a LoRA-loaded model. It reads the safetensors metadata to find values like the reference downscale factor and outputs them as a structured parameter object, which can be connected to the LTXVAddGuide node for special guide handling. If the metadata is missing or the reference downscale factor cannot be read, the value defaults to 1; when found, the value is rounded and clamped to a minimum of 1.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `iclora_model` | Direct output from a LoRA Loader for the specific IC-LoRA from which to extract the metadata. | MODEL | Yes | N/A |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `iclora_parameters` | IC-LoRA parameters extracted from the LoRA metadata (e.g., reference_downscale_factor). Connect to LTXVAddGuide if the LoRA requires special handling of the guides. | IC_LORA_PARAMETERS |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/en.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
