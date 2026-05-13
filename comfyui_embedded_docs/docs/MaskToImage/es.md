> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskToImage/es.md)

El nodo `MaskToImage` está diseñado para convertir una máscara en un formato de imagen. Esta transformación permite visualizar y procesar máscaras como imágenes, facilitando un puente entre las operaciones basadas en máscaras y las aplicaciones basadas en imágenes.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `máscara`    | `MASK`      | La entrada de máscara es esencial para el proceso de conversión, ya que sirve como los datos de origen que se transformarán en un formato de imagen. Esta entrada determina la forma y el contenido de la imagen resultante. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida es una representación en imagen de la máscara de entrada, lo que permite la inspección visual y manipulaciones adicionales basadas en imágenes. |