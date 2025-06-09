Este nodo está diseñado para preparar imágenes para el proceso de extensión añadiendo acolchado alrededor de ellas. Ajusta las dimensiones de la imagen para asegurar la compatibilidad con los algoritmos de extensión, facilitando la generación de áreas de imagen extendidas más allá de los límites originales.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La entrada 'image' es la imagen principal que se preparará para la extensión, sirviendo como base para las operaciones de acolchado. |
| `left`    | `INT`       | Especifica la cantidad de acolchado a añadir al lado izquierdo de la imagen, influyendo en el área expandida para la extensión. |
| `top`     | `INT`       | Determina la cantidad de acolchado a añadir en la parte superior de la imagen, afectando la expansión vertical para la extensión. |
| `right`   | `INT`       | Define la cantidad de acolchado a añadir al lado derecho de la imagen, impactando la expansión horizontal para la extensión. |
| `bottom`  | `INT`       | Indica la cantidad de acolchado a añadir en la parte inferior de la imagen, contribuyendo a la expansión vertical para la extensión. |
| `feathering` | `INT` | Controla la suavidad de la transición entre la imagen original y el acolchado añadido, mejorando la integración visual para la extensión. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida 'image' representa la imagen acolchada, lista para el proceso de extensión. |
| `mask`    | `MASK`      | La salida 'mask' indica las áreas de la imagen original y el acolchado añadido, útil para guiar los algoritmos de extensión. |
