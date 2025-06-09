
El nodo SolidMask genera una máscara uniforme con un valor especificado en toda su área. Está diseñado para crear máscaras de dimensiones e intensidad específicas, útiles en diversas tareas de procesamiento de imágenes y enmascaramiento.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `value`   | FLOAT       | Especifica el valor de intensidad de la máscara, afectando su apariencia general y utilidad en operaciones posteriores. |
| `width`   | INT         | Determina el ancho de la máscara generada, influyendo directamente en su tamaño y relación de aspecto. |
| `height`  | INT         | Establece la altura de la máscara generada, afectando su tamaño y relación de aspecto. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `mask`    | MASK        | Produce una máscara uniforme con las dimensiones y el valor especificados. |
