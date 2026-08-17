# Dual CFG Guider

The DualCFGGuider node creates a guidance system for dual classifier-free guidance sampling. It combines two positive conditioning inputs with one negative conditioning input, applying different guidance scales to each conditioning pair to control how strongly each prompt influences the generated output.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to use for guidance. | MODEL | Yes | - |
| `cond1` | The first positive conditioning input. | CONDITIONING | Yes | - |
| `cond2` | The second positive conditioning input, treated as the intermediate conditioning. | CONDITIONING | Yes | - |
| `negative` | The negative conditioning input. | CONDITIONING | Yes | - |
| `cfg_conds` | Guidance scale applied between `cond1` and `cond2` (default: 8.0). | FLOAT | Yes | 0.0 - 100.0 |
| `cfg_cond2_negative` | Guidance scale applied between `cond2` and the negative conditioning (default: 8.0). | FLOAT | Yes | 0.0 - 100.0 |
| `style` | The guidance style to apply (default: "regular"). "regular" combines both guidance scales in one step; "nested" applies `cfg_conds` first and then scales the result with `cfg_cond2_negative` relative to the negative conditioning. | COMBO | Yes | "regular"<br>"nested" |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `GUIDER` | A configured guidance system ready for use with sampling. | GUIDER |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/en.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
