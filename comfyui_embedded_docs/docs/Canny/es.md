El nodo Canny está diseñado para la detección de bordes en imágenes, utilizando el algoritmo Canny para identificar y resaltar los bordes. Este proceso implica aplicar una serie de filtros a la imagen de entrada para detectar áreas de alto gradiente, que corresponden a bordes, mejorando así los detalles estructurales de la imagen.

## Tipos de entrada

| Parameter | Comfy dtype | Description |
| --- | --- | --- |
| `image` | `IMAGE` | La imagen de entrada a procesar para la detección de bordes. Es crucial ya que sirve como base para la operación de detección de bordes. |
| `low_threshold` | `FLOAT` | El umbral inferior para el procedimiento de histéresis en la detección de bordes. Determina el gradiente de intensidad mínimo considerado para un borde, afectando la sensibilidad de la detección de bordes. |
| `high_threshold` | `FLOAT` | El umbral superior para el procedimiento de histéresis en la detección de bordes. Establece el gradiente de intensidad máximo considerado para un borde, influyendo en la selectividad de la detección de bordes. |

## Tipos de salida

| Parameter | Comfy dtype | Description |
| --- | --- | --- |
| `image` | `IMAGE` | La salida es una imagen con bordes resaltados, donde los bordes se detectan utilizando el algoritmo Canny. Esto mejora los detalles estructurales de la imagen original. |
