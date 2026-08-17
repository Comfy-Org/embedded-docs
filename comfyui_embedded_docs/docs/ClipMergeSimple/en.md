# CLIPMergeSimple

`CLIPMergeSimple` merges two CLIP text encoder models into a single one. It clones the first CLIP model as the base and applies weighted parameter patches taken from the second CLIP model, so the result combines features from both. The `ratio` setting controls how strongly each model contributes; at the default of 1.0 the first model is used unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `clip1` | The first CLIP model. It is cloned and used as the base model for the merge. | CLIP | Yes | — |
| `clip2` | The second CLIP model. Its key patches are applied to the base model, except for patches whose keys end with `.position_ids` or `.logit_scale`. | CLIP | Yes | — |
| `ratio` | Controls the relative strength of the two models. The base model (`clip1`) keeps a strength equal to `ratio`, and `clip2`'s patches are applied with a strength of `1.0 - ratio`. At the default of 1.0 the output equals `clip1`; lower values blend in more of `clip2`; at 0.0 `clip2`'s patches are applied at full strength. | FLOAT | Yes | 0.0 to 1.0 (default: 1.0, step: 0.01) |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `clip` | The merged CLIP model: a clone of `clip1` with patches from `clip2` applied according to `ratio`. | CLIP |

## Merging Mechanism Explained

### Merging Algorithm

The node uses weighted patch application to combine the two models:

1. **Clone Base Model**: Clones `clip1` to serve as the base model.
2. **Get Patches**: Collects all key patches (parameter values) from `clip2`.
3. **Filter Special Keys**: Skips keys ending with `.position_ids` and `.logit_scale`, so those parameters stay unchanged.
4. **Apply Weighted Merge**: Applies `clip2`'s patches to the cloned base model with a patch strength of `1.0 - ratio`, while the base model keeps a strength of `ratio`.

### Ratio Parameter Explained

- **ratio = 1.0**: Base strength is 1.0 and patch strength is 0.0, so the output is identical to `clip1` (default).
- **ratio = 0.5**: Base strength and patch strength are both 0.5, so both models contribute with equal strength.
- **ratio = 0.0**: Base strength is 0.0 and patch strength is 1.0, so `clip2`'s patches are applied at full strength.

## Use Cases

1. **Model Style Fusion**: Combine characteristics of CLIP models trained on different data.
2. **Performance Optimization**: Balance strengths and weaknesses of different models.
3. **Experimental Research**: Explore combinations of different CLIP encoders.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSimple/en.md)

---
**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`
