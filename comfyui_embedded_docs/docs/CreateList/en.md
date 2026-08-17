# Create List

The Create List node combines multiple inputs into a single, sequential list. It takes any number of inputs of the same data type and concatenates them in the order they are connected. This node is useful for preparing batches of data, such as images or text, to be processed by other nodes in a workflow.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `inputs` | A growable set of input slots. Add more slots by clicking the plus (+) icon, or connect items and new slots are created automatically. Each slot accepts one or more items, and all slots must share the same data type (for example, all IMAGE or all STRING). | Varies (matches the connected data type) | Yes | Any number of slots; each slot accepts one or more items |

**Note:** The node automatically creates new input slots as you connect items. All connected inputs must share the same data type for the node to function correctly, and the output list takes that same type.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `list` | A single list containing all the items from the connected input slots, concatenated in the order the slots are connected. The output data type matches the input data type. | Varies (matches the input data type) |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/en.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
