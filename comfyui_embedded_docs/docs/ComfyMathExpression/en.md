> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/en.md)

The ComfyMathExpression node evaluates a mathematical formula using a set of input values. You can write an expression using variable names (like `a`, `b`, `c`), and the node will calculate the result. It supports dynamically adding as many input values as needed for your calculation.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `expression` | STRING | Yes | N/A | The mathematical formula to evaluate. You can use variable names that correspond to the input values (default: "a + b"). |
| `values` | FLOAT, INT, BOOLEAN | No | N/A | A set of numeric or boolean inputs that can be dynamically added. Each input is assigned a letter from the alphabet (a, b, c, ...) to be used as a variable in the expression. |

**Parameter Constraints:**
*   The `expression` parameter cannot be empty or contain only whitespace.
*   The expression must evaluate to a finite numeric result (INT or FLOAT). Boolean or other non-numeric results will cause an error.
*   The input values for the `values` parameter can be numbers (INT or FLOAT) or boolean values (TRUE/FALSE).

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | The result of the mathematical expression as a floating-point number. |
| `INT` | INT | The result of the mathematical expression as an integer. |
| `BOOL` | BOOLEAN | The result of the mathematical expression as a boolean value. |

---
**Source fingerprint (SHA-256):** `962f82684d9dc58a67a57e6738d6d2ed457d7f30288cedb21fd46b5c655c1708`
