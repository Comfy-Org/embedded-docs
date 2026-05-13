> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/es.md)

Este nodo está diseñado para preparar imágenes para el proceso de outpainting añadiendo relleno alrededor de ellas. Ajusta las dimensiones de la imagen para garantizar la compatibilidad con los algoritmos de outpainting, facilitando la generación de áreas extendidas más allá de los límites originales.

## Inputs

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `imagen`   | `IMAGE`     | La entrada 'image' es la imagen principal que se preparará para outpainting, sirviendo como base para las operaciones de relleno. |
| `izquierda`    | `INT`       | Especifica la cantidad de relleno que se añadirá al lado izquierdo de la imagen, influyendo en el área expandida para outpainting. |
| `arriba`     | `INT`       | Determina la cantidad de relleno que se añadirá en la parte superior de la imagen, afectando la expansión vertical para outpainting. |
| `derecha`   | `INT`       | Define la cantidad de relleno que se añadirá al lado derecho de la imagen, impactando la expansión horizontal para outpainting. |
| `abajo`  | `INT`       | Indica la cantidad de relleno que se añadirá en la parte inferior de la imagen, contribuyendo a la expansión vertical para outpainting. |
| `difuminado` | `INT` | Controla la suavidad de la transición entre la imagen original y el relleno añadido, mejorando la integración visual para outpainting. |

## Outputs

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `imagen`   | `IMAGE`     | La salida 'image' representa la imagen con relleno, lista para el proceso de outpainting. |
| `mask`    | `MASK`      | La salida 'mask' indica las áreas de la imagen original y el relleno añadido, útil para guiar los algoritmos de outpainting. |