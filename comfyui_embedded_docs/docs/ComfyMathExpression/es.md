El nodo ComfyMathExpression evalúa una fórmula matemática utilizando un conjunto de valores de entrada. Puedes escribir una expresión usando nombres de variables (como `a`, `b`, `c`), y el nodo calculará el resultado. Admite la adición dinámica de tantos valores de entrada como sean necesarios para tu cálculo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `expresión` | La fórmula matemática a evaluar. Puedes usar nombres de variables que correspondan a los valores de entrada (predeterminado: "a + b"). | STRING | Sí | N/A |
| `valores` | Un conjunto de entradas numéricas o booleanas que se pueden agregar dinámicamente. A cada entrada se le asigna una letra del alfabeto (a, b, c, ...) para usarse como variable en la expresión. | FLOAT, INT, BOOLEAN | No | N/A |

**Restricciones de los parámetros:**
*   El parámetro `expression` no puede estar vacío ni contener solo espacios en blanco.
*   La expresión debe evaluarse a un resultado numérico finito (INT o FLOAT). Los valores booleanos u otros resultados no numéricos generarán un error.
*   Los valores de entrada para el parámetro `values` pueden ser números (INT o FLOAT) o valores booleanos (VERDADERO/FALSO).

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `FLOAT` | El resultado de la expresión matemática como número de punto flotante. | FLOAT |
| `BOOL` | El resultado de la expresión matemática como número entero. | INT |
| `BOOL` | El resultado de la expresión matemática como valor booleano. | BOOLEAN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/es.md)

---
**Source fingerprint (SHA-256):** `962f82684d9dc58a67a57e6738d6d2ed457d7f30288cedb21fd46b5c655c1708`
