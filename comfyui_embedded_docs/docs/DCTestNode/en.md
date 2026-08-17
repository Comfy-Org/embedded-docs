# DCTestNode

The DCTestNode is a logic node that returns different types of data based on a user's selection from a dynamic combo box. It acts as a conditional router, where the chosen option determines which input field is active and what type of value the node will output.

## Inputs

The `combo` selector is always visible. The input fields shown below it depend on the selected option.

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `combo` | The main selection that determines which input field is active and what the node will output. | DYNAMIC_COMBO | Yes | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `string` | A text input field. This field is only active and required when `combo` is set to `"option1"`. | STRING | Yes | - |

### option2 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `integer` | A whole number input field. This field is only active and required when `combo` is set to `"option2"`. | INT | Yes | - |

### option3 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `image` | An image input field. This field is only active and required when `combo` is set to `"option3"`. | IMAGE | Yes | - |

### option4 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `subcombo` | A secondary selection that appears when `combo` is set to `"option4"`. It determines which nested input fields are active. | DYNAMIC_COMBO | Yes | `"opt1"`<br>`"opt2"` |

#### opt1 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `float_x` | A decimal number input. This field is only active and required when `combo` is set to `"option4"` and `subcombo` is set to `"opt1"`. | FLOAT | Yes | - |
| `float_y` | A decimal number input. This field is only active and required when `combo` is set to `"option4"` and `subcombo` is set to `"opt1"`. | FLOAT | Yes | - |

#### opt2 Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `mask1` | A mask input field. This field is only active when `combo` is set to `"option4"` and `subcombo` is set to `"opt2"`. It is optional. | MASK | No | - |

**Parameter Constraints:**

* The `combo` parameter controls the visibility and requirement of all other input fields. Only the inputs associated with the selected `combo` option are shown and required (except `mask1`, which is optional).
* When `combo` is set to `"option4"`, the `subcombo` parameter becomes active and required, and controls a second set of nested inputs: `"opt1"` shows `float_x` and `float_y`; `"opt2"` shows `mask1`.
* If `combo` is set to an unexpected value, the node raises a ValueError.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | The output depends on the selected `combo` option. It can be a STRING (`"option1"`), an INT (`"option2"`), an IMAGE (`"option3"`), or a string representation of the `subcombo` dictionary (`"option4"`). | ANYTYPE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/en.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
