
## Empty Hunyuan Latent Video Input Types

| Parameter    | Comfy Type | Description                                                                                |
| ----------- | ---------- | ------------------------------------------------------------------------------------------ |
| `width`     | `INT`      | Video width, default 848, minimum 16, maximum `nodes.MAX_RESOLUTION`, step size 16.        |
| `height`    | `INT`      | Video height, default 480, minimum 16, maximum `nodes.MAX_RESOLUTION`, step size 16.       |
| `length`    | `INT`      | Video length, default 25, minimum 1, maximum `nodes.MAX_RESOLUTION`, step size 4.          |
| `batch_size`| `INT`      | Batch size, default 1, minimum 1, maximum 4096.                                           |

## Empty Hunyuan Latent Video Output Types

| Parameter | Comfy Type | Description                                                                               |
| --------- | ---------- | ----------------------------------------------------------------------------------------- |
| `samples` | `LATENT`   | Generated latent video samples containing zero tensors, ready for processing and generation tasks. |
