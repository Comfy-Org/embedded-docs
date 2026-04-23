> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/es.md)

El nodo ComfyMathExpression evalúa una fórmula matemática utilizando un conjunto de valores de entrada. Puedes escribir una expresión usando nombres de variables (como `a`, `b`, `c`), y el nodo calculará el resultado. Admite agregar dinámicamente tantos valores de entrada como sean necesarios para tu cálculo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `expression` | STRING | Sí | N/A | La fórmula matemática a evaluar. Puedes usar nombres de variables que correspondan a los valores de entrada (por defecto: "a + b"). |
| `values` | FLOAT, INT | No | N/A | Un conjunto de entradas numéricas que se pueden agregar dinámicamente. A cada entrada se le asigna una letra del alfabeto (a, b, c, ...) para ser usada como variable en la expresión. |

**Restricciones de Parámetros:**
*   El parámetro `expression` no puede estar vacío o contener solo espacios en blanco.
*   La expresión debe evaluarse a un resultado numérico finito (INT o FLOAT). Los resultados booleanos u otros no numéricos causarán un error.
*   Los valores de entrada para el parámetro `values` deben ser números válidos (INT o FLOAT).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | El resultado de la expresión matemática como un número de punto flotante. |
| `INT` | INT | El resultado de la expresión matemática como un número entero. |