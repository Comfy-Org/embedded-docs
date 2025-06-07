
El nodo LoadImageMask está diseñado para cargar imágenes y sus máscaras asociadas desde una ruta especificada, procesándolas para asegurar su compatibilidad con tareas posteriores de manipulación o análisis de imágenes. Se centra en manejar varios formatos de imagen y condiciones, como la presencia de un canal alfa para máscaras, y prepara las imágenes y máscaras para el procesamiento posterior convirtiéndolas a un formato estandarizado.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | COMBO[STRING] | El parámetro 'image' especifica el archivo de imagen que se cargará y procesará. Desempeña un papel crucial en la determinación de la salida al proporcionar la imagen fuente para la extracción de la máscara y la conversión de formato. |
| `channel` | COMBO[STRING] | El parámetro 'channel' especifica el canal de color de la imagen que se utilizará para generar la máscara. Esto permite flexibilidad en la creación de máscaras basadas en diferentes canales de color, mejorando la utilidad del nodo en varios escenarios de procesamiento de imágenes. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | Este nodo produce la máscara generada a partir de la imagen y el canal especificados, preparada en un formato estandarizado adecuado para un procesamiento posterior en tareas de manipulación de imágenes. |
