# Wan Context Windows

The Wan Context Windows (Manual) node lets you manually configure context windows for Wan-like models with 2-dimensional processing. It applies context window settings during sampling by specifying the window length, overlap, scheduling method, and fusion technique, giving you control over how the model processes different context regions.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The model to apply context windows to during sampling. | MODEL | Yes | - |
| `context_length` | The length of the context window in real frames. Must be 4*n + 1. (default: 81) | INT | Yes | 1 to 16384 (step 4) |
| `context_overlap` | The overlap of the context window in real frames. (default: 30) | INT | Yes | 0 or greater |
| `context_schedule` | Step-dependent scheduling algorithm for context windows. (default: "uniform_standard") | COMBO | Yes | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | The stride of the context window; only applicable to uniform schedules. (default: 1) | INT | Yes | 1 or greater |
| `closed_loop` | Whether to close the context window loop; only applicable to looped schedules. (default: False) | BOOLEAN | Yes | True or False |
| `fuse_method` | The method to use to fuse the context windows. (default: "pyramid") | COMBO | Yes | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Whether to apply FreeNoise noise shuffling, improves window blending. (default: True) | BOOLEAN | Yes | True or False |
| `retain_first_frame` | Retain the first I2V frame in every context window (may help retain initial reference). (default: False) | BOOLEAN | Yes | True or False |
| `split_conds_to_windows` | Whether to split multiple conditionings (created by ConditionCombine) to each window based on region index. (default: False) | BOOLEAN | Yes | True or False |

**Note:** `context_stride` only affects uniform schedules, and `closed_loop` only applies to looped schedules. `context_length` should follow the pattern 4n + 1. The node converts `context_length` and `context_overlap` from real frames to model units before applying them, enforcing a minimum of 1 for `context_length` and 0 for `context_overlap`. The `context_stride`, `closed_loop`, `freenoise`, and `split_conds_to_windows` inputs are advanced options.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The model with the applied context window configuration. | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/en.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
