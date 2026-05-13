> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/es.md)

El nodo SolidMask genera una máscara uniforme con un valor específico en toda su área. Está diseñado para crear máscaras de dimensiones e intensidad determinadas, útil en diversas tareas de procesamiento de imágenes y enmascaramiento.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `value`   | FLOAT       | Especifica el valor de intensidad de la máscara, afectando su apariencia general y utilidad en operaciones posteriores. |
| `width`   | INT         | Determina el ancho de la máscara generada, influyendo directamente en su tamaño y relación de aspecto. |
| `height`  | INT         | Establece la altura de la máscara generada, afectando su tamaño y relación de aspecto. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `mask`    | MASK        | Genera una máscara uniforme con las dimensiones y el valor especificados. |