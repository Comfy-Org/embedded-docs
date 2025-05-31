The ConditioningAverage node is designed to blend two sets of conditioning data, applying a weighted average based on a specified strength. This process allows for the dynamic adjustment of conditioning influence, facilitating the fine-tuning of generated content or features.
## Input types

| Parameter             | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Represents the primary set of conditioning data to which the blending will be applied. It serves as the base for the weighted average operation. |
| `conditioning_from`   | `CONDITIONING`     | Denotes the secondary set of conditioning data that will be blended into the primary set. This data influences the final output based on the specified strength. |
| `conditioning_to_strength` | `FLOAT` | A scalar value that determines the strength of the blend between the primary and secondary conditioning data. It directly influences the balance of the weighted average. |

## Output types

| Parameter            | Comfy dtype        | Description |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | The result of blending the primary and secondary conditioning data, producing a new set of conditioning that reflects the weighted average. |