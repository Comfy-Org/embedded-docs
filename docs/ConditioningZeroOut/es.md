Este nodo anula elementos específicos dentro de la estructura de datos de condicionamiento, neutralizando efectivamente su influencia en los pasos de procesamiento posteriores. Está diseñado para operaciones de condicionamiento avanzadas donde se requiere la manipulación directa de la representación interna del condicionamiento.

## Tipos de entrada

| Parámetro | Tipo Comfy                | Descripción |
|-----------|----------------------------|-------------|
| `conditioning` | `CONDITIONING` | La estructura de datos de condicionamiento que se va a modificar. Este nodo anula los elementos 'pooled_output' dentro de cada entrada de condicionamiento, si están presentes. |

## Tipos de salida

| Parámetro | Tipo Comfy                | Descripción |
|-----------|----------------------------|-------------|
| `conditioning` | `CONDITIONING` | La estructura de datos de condicionamiento modificada, con los elementos 'pooled_output' establecidos en cero donde sea aplicable. |
