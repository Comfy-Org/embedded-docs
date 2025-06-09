This node is designed to modify the behavior of a CLIP model by setting a specific layer as the last one to be executed. It allows for the customization of the depth of processing within the CLIP model, potentially affecting the model's output by limiting the amount of information processed.

## Inputs

| Parameter            | Data Type | Description |
|----------------------|-----------|-------------|
| `clip`               | `CLIP`    | The CLIP model to be modified. This parameter allows the node to directly interact with and alter the structure of the CLIP model. |
| `stop_at_clip_layer` | `INT`     | Specifies the layer at which the CLIP model should stop processing. This allows for control over the depth of computation and can be used to adjust the model's behavior or performance. |

## Outputs

| Parameter | Data Type   | Description |
|-----------|-------------|-------------|
| `clip`    | CLIP      | The modified CLIP model with the specified layer set as the last one. This output enables further use or analysis of the adjusted model. |
