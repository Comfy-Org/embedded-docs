> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/en.md)

This node creates a style configuration for generating realistic images using Recraft's API. It selects the `realistic_image` style and lets you choose an optional substyle to fine-tune the output appearance.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | Yes | Multiple options available (determined by Recraft API) | The specific substyle to apply to the realistic_image style. If set to "None", no substyle will be applied. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | A Recraft style configuration object containing the `realistic_image` style and the selected substyle settings. This output can be connected to other Recraft nodes that accept a style input. |

---
**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`
