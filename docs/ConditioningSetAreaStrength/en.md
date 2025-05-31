This node is designed to modify the strength attribute of a given conditioning set, allowing for the adjustment of the influence or intensity of the conditioning on the generation process.

## Input types

| Parameter | Comfy dtype | Description |
|-----------|-------------|-------------|
| `conditioning` | `CONDITIONING` | The conditioning set to be modified, representing the current state of conditioning that influences the generation process. |
| `strength` | `FLOAT` | The strength value to be applied to the conditioning set, dictating the intensity of its influence. |

## Output types

| Parameter | Comfy dtype | Description |
|-----------|-------------|-------------|
| `conditioning` | `CONDITIONING` | The modified conditioning set with updated strength values for each element. |