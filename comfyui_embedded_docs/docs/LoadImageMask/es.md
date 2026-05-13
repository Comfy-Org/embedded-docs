> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/es.md)

El nodo LoadImageMask está diseñado para cargar imágenes y sus máscaras asociadas desde una ruta especificada, procesándolas para garantizar la compatibilidad con tareas posteriores de manipulación o análisis de imágenes. Se enfoca en manejar varios formatos de imagen y condiciones, como la presencia de un canal alfa para las máscaras, y prepara las imágenes y máscaras para el procesamiento posterior convirtiéndolas a un formato estandarizado.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `imagen`   | COMBO[STRING] | El parámetro `imagen` especifica el archivo de imagen que se cargará y procesará. Desempeña un papel crucial en la determinación de la salida al proporcionar la imagen de origen para la extracción de la máscara y la conversión de formato. |
| `canal` | COMBO[STRING] | El parámetro `canal` especifica el canal de color de la imagen que se utilizará para generar la máscara. Esto permite flexibilidad en la creación de máscaras basadas en diferentes canales de color, mejorando la utilidad del nodo en diversos escenarios de procesamiento de imágenes. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Este nodo genera la máscara producida a partir de la imagen y el canal especificados, preparada en un formato estandarizado adecuado para su posterior procesamiento en tareas de manipulación de imágenes. |