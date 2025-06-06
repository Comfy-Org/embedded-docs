
The LatentRotate node is designed to rotate latent representations of images by specified angles. It abstracts the complexity of manipulating latent space to achieve rotation effects, enabling users to easily transform images in a generative model's latent space.
## Input types

| Parameter | Comfy dtype | Description |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | The 'samples' parameter represents the latent representations of images to be rotated. It is crucial for determining the starting point of the rotation operation. |
| `rotation` | `COMBO[STRING]` | The 'rotation' parameter specifies the angle by which the latent images should be rotated. It directly influences the orientation of the resulting images. |

## Output types

| Parameter | Comfy dtype | Description |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | The output is a modified version of the input latent representations, rotated by the specified angle. |