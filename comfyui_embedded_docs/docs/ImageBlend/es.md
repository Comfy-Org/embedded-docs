El nodo `ImageBlend` está diseñado para mezclar dos imágenes juntas basándose en un modo de mezcla y un factor de mezcla especificados. Soporta varios modos de mezcla como normal, multiplicar, pantalla, superponer, luz suave y diferencia, permitiendo técnicas versátiles de manipulación y composición de imágenes. Este nodo es esencial para crear imágenes compuestas ajustando la interacción visual entre dos capas de imagen.

## Entradas

| Campo         | Data Type | Descripción                                                                       |
|---------------|-------------|-----------------------------------------------------------------------------------|
| `image1`      | `IMAGE`     | La primera imagen a mezclar. Sirve como la capa base para la operación de mezcla. |
| `image2`      | `IMAGE`     | La segunda imagen a mezclar. Dependiendo del modo de mezcla, modifica la apariencia de la primera imagen. |
| `blend_factor`| `FLOAT`     | Determina el peso de la segunda imagen en la mezcla. Un factor de mezcla más alto da más prominencia a la segunda imagen en la mezcla resultante. |
| `blend_mode`  | COMBO[STRING] | Especifica el método de mezcla de las dos imágenes. Soporta modos como normal, multiplicar, pantalla, superponer, luz suave y diferencia, cada uno produciendo un efecto visual único. |

## Salidas

| Campo | Data Type | Descripción                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | La imagen resultante después de mezclar las dos imágenes de entrada según el modo y factor de mezcla especificados. |
