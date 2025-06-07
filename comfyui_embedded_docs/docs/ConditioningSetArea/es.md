Este nodo está diseñado para modificar la información de condicionamiento estableciendo áreas específicas dentro del contexto de condicionamiento. Permite la manipulación espacial precisa de los elementos de condicionamiento, habilitando ajustes y mejoras dirigidas basadas en dimensiones y fuerza especificadas.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento a modificar. Sirve como base para aplicar ajustes espaciales. |
| `width`   | `INT`      | Especifica el ancho del área a establecer dentro del contexto de condicionamiento, influyendo en el alcance horizontal del ajuste. |
| `height`  | `INT`      | Determina la altura del área a establecer, afectando la extensión vertical de la modificación de condicionamiento. |
| `x`       | `INT`      | El punto de inicio horizontal del área a establecer, posicionando el ajuste dentro del contexto de condicionamiento. |
| `y`       | `INT`      | El punto de inicio vertical para el ajuste del área, estableciendo su posición dentro del contexto de condicionamiento. |
| `strength`| `FLOAT`    | Define la intensidad de la modificación de condicionamiento dentro del área especificada, permitiendo un control matizado sobre el impacto del ajuste. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento modificados, reflejando los ajustes y configuraciones de área especificados. |
