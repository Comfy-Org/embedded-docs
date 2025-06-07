El nodo `EmptyImage` está diseñado para generar imágenes en blanco de dimensiones y color especificados. Permite la creación de imágenes de color uniforme que pueden servir como fondos o marcadores de posición en varias tareas de procesamiento de imágenes.

## Entradas

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `width`   | `INT`      | Especifica el ancho de la imagen generada. Determina qué tan ancha será la imagen. |
| `height`  | `INT`      | Determina la altura de la imagen generada. Afecta el tamaño vertical de la imagen. |
| `batch_size` | `INT` | Indica el número de imágenes a generar en un solo lote. Esto permite la creación de múltiples imágenes a la vez. |
| `color`   | `INT`      | Define el color de la imagen generada usando un valor hexadecimal, permitiendo la personalización de la apariencia de la imagen. Este parámetro permite la selección de una amplia gama de colores. |

## Salidas

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`    | La salida es un tensor que representa la imagen o imágenes generadas, con las dimensiones y color especificados. |
