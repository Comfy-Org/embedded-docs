> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/es.md)

El nodo ImageToMask está diseñado para convertir una imagen en una máscara basada en un canal de color específico. Permite extraer capas de máscara correspondientes a los canales rojo, verde, azul o alfa de una imagen, facilitando operaciones que requieren enmascaramiento o procesamiento específico por canal.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|---------------|-------------|
| `image`   | `IMAGE`       | El parámetro `image` representa la imagen de entrada a partir de la cual se generará una máscara basada en el canal de color especificado. Desempeña un papel crucial en la determinación del contenido y las características de la máscara resultante. |
| `channel` | COMBO[STRING] | El parámetro `channel` especifica qué canal de color (rojo, verde, azul o alfa) de la imagen de entrada debe utilizarse para generar la máscara. Esta elección influye directamente en la apariencia de la máscara y en qué partes de la imagen se resaltan o se enmascaran. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|---------------|-------------|
| `mask`    | `MASK`        | La máscara de salida `mask` es una representación binaria o en escala de grises del canal de color especificado de la imagen de entrada, útil para operaciones posteriores de procesamiento de imágenes o enmascaramiento. |