# Grok Image Edit

Modify an existing image based on a text prompt. This node sends your images and a text description to the Grok API, which edits the images according to your instructions and returns the result.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The Grok image model to use. The sub-parameters shown below change depending on the selected model. | MODEL | Yes | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | The text prompt used to generate the image. (default: "") | STRING | Yes | N/A |
| `seed` | Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. (default: 0) | INT | Yes | 0 to 2147483647 |

### grok-imagine-image-2.0 Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Reference image(s) to edit. Up to 3 images. | IMAGE | Yes | 1 to 3 images |
| `resolution` | Output resolution of the edited images. | STRING | Yes | "1K"<br>"2K" |
| `number_of_images` | Number of edited images to generate. (default: 1) | INT | Yes | 1 to 10 |
| `quality` | Quality level of the generated images. | STRING | Yes | "medium"<br>"low" |
| `aspect_ratio` | Aspect ratio of the edited image. (default: "auto") | STRING | Yes | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality and grok-imagine-image Inputs

Shared by grok-imagine-image-quality and grok-imagine-image.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Reference image(s) to edit. Up to 3 images. | IMAGE | Yes | 1 to 3 images |
| `resolution` | Output resolution of the edited images. | STRING | Yes | "1K"<br>"2K" |
| `number_of_images` | Number of edited images to generate. (default: 1) | INT | Yes | 1 to 10 |
| `aspect_ratio` | Only allowed when multiple images are connected. (default: "auto") | STRING | Yes | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Reference image to edit. | IMAGE | Yes | 1 image |
| `resolution` | Output resolution of the edited images. | STRING | Yes | "1K"<br>"2K" |
| `number_of_images` | Number of edited images to generate. (default: 1) | INT | Yes | 1 to 10 |

### Reference Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | Growable slot: connect 1 or more reference images to edit. Numbered slots such as `image_1`, `image_2`, `image_3` can be added. The maximum number of images depends on the selected model (see model sections above). | IMAGE | Yes | 1 to 3 images, depending on the model |

**Note on constraints:**
- `prompt` must contain at least 1 non-whitespace character.
- At least one reference image is required for editing; the node raises an error if no image is connected.
- The maximum number of input images is 1 for `grok-imagine-image-pro` and 3 for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image`. Connecting more images than the model supports raises an error.
- For `grok-imagine-image-quality` and `grok-imagine-image`, a custom `aspect_ratio` (anything other than "auto") is only allowed when multiple images are connected. With a single image, `aspect_ratio` must be "auto".
- For `grok-imagine-image-2.0`, `aspect_ratio` can be set freely even with a single image.
- The `quality` sub-parameter is only available with `grok-imagine-image-2.0`.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `IMAGE` | The edited image(s) returned by the Grok API. If a single image is generated, it is returned directly. If multiple images are generated, they are concatenated into a single batch tensor. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/en.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
