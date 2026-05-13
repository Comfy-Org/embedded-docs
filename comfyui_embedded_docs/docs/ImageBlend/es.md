> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/es.md)

El nodo `ImageBlend` está diseñado para fusionar dos imágenes según un modo de fusión y un factor de mezcla especificados. Admite varios modos de fusión como normal, multiplicar, pantalla, superposición, luz suave y diferencia, lo que permite técnicas versátiles de manipulación y composición de imágenes. Este nodo es esencial para crear imágenes compuestas ajustando la interacción visual entre dos capas de imagen.

## Entradas

| Campo          | Tipo de Dato | Descripción                                                                       |
|----------------|--------------|-----------------------------------------------------------------------------------|
| `image1`       | `IMAGE`      | La primera imagen a fusionar. Actúa como capa base para la operación de fusión.   |
| `image2`       | `IMAGE`      | La segunda imagen a fusionar. Dependiendo del modo de fusión, modifica la apariencia de la primera imagen. |
| `blend_factor` | `FLOAT`      | Determina el peso de la segunda imagen en la mezcla. Un factor de mezcla más alto otorga mayor prominencia a la segunda imagen en el resultado final. |
| `blend_mode`   | COMBO[STRING] | Especifica el método de fusión de las dos imágenes. Admite modos como normal, multiplicar, pantalla, superposición, luz suave y diferencia, cada uno produciendo un efecto visual único. |

## Salidas

| Campo   | Tipo de Dato | Descripción                                                              |
|---------|--------------|--------------------------------------------------------------------------|
| `image` | `IMAGE`      | La imagen resultante tras fusionar las dos imágenes de entrada según el modo de fusión y el factor especificados. |