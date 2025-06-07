El nodo `ImageColorToMask` está diseñado para convertir un color especificado en una imagen a una máscara. Procesa una imagen y un color objetivo, generando una máscara donde el color especificado está resaltado, facilitando operaciones como la segmentación basada en color o la aislamiento de objetos.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El parámetro 'image' representa la imagen de entrada a procesar. Es crucial para determinar las áreas de la imagen que coinciden con el color especificado para ser convertidas en una máscara. |
| `color`   | `INT`       | El parámetro 'color' especifica el color objetivo en la imagen que se convertirá en una máscara. Juega un papel clave en la identificación de las áreas de color específicas que se resaltarán en la máscara resultante. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | La salida es una máscara que resalta las áreas de la imagen de entrada que coinciden con el color especificado. Esta máscara puede ser utilizada para tareas de procesamiento de imágenes adicionales, como segmentación o aislamiento de objetos. |
