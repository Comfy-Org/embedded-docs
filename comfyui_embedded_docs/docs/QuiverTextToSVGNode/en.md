> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNode/en.md)

The Quiver Text to SVG node generates a Scalable Vector Graphic (SVG) image from a text description using Quiver AI's models. You can optionally provide reference images and style instructions to guide the generation process.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Yes | N/A | Text description of the desired SVG output. This is the main instruction for what to generate. |
| `instructions` | STRING | No | N/A | Additional style or formatting guidance. This is an optional, advanced parameter. |
| `reference_images` | IMAGE | No | 0 to 4 images | Up to 4 reference images to guide the generation. This is an optional input. |
| `model` | COMBO | Yes | `"Quiver SVG v1"`<br>`"Quiver SVG v1 Max"`<br>`"Quiver SVG v1 Preview"` | Model to use for SVG generation. The available options are determined by the Quiver API. |
| `seed` | INT | Yes | 0 to 2147483647 | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. Default: 0. |

**Note:** The `reference_images` input accepts a maximum of 4 images. If more are provided, the node will raise an error.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `SVG` | SVG | The generated Scalable Vector Graphic (SVG) image. |

---
**Source fingerprint (SHA-256):** `634758797a59e5a409424deee808e1d8b5b5852a86eac4bccd7f2634a19fb743`
