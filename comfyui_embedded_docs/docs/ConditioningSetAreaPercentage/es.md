El nodo ConditioningSetAreaPercentage se especializa en ajustar el área de influencia de los elementos de condicionamiento basado en valores porcentuales. Permite especificar las dimensiones y la posición del área como porcentajes del tamaño total de la imagen, junto con un parámetro de fuerza para modular la intensidad del efecto de condicionamiento.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Representa los elementos de condicionamiento a modificar, sirviendo como base para aplicar ajustes de área y fuerza. |
| `width`   | `FLOAT`     | Especifica el ancho del área como un porcentaje del ancho total de la imagen, influyendo en cuánto de la imagen afecta el condicionamiento horizontalmente. |
| `height`  | `FLOAT`     | Determina la altura del área como un porcentaje de la altura total de la imagen, afectando la extensión vertical de la influencia del condicionamiento. |
| `x`       | `FLOAT`     | Indica el punto de inicio horizontal del área como un porcentaje del ancho total de la imagen, posicionando el efecto de condicionamiento. |
| `y`       | `FLOAT`     | Especifica el punto de inicio vertical del área como un porcentaje de la altura total de la imagen, posicionando el efecto de condicionamiento. |
| `strength`| `FLOAT`     | Controla la intensidad del efecto de condicionamiento dentro del área especificada, permitiendo un ajuste fino de su impacto. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Devuelve los elementos de condicionamiento modificados con parámetros de área y fuerza actualizados, listos para un procesamiento o aplicación adicional. |
