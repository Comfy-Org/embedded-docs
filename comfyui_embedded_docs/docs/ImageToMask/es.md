El nodo ImageToMask está diseñado para convertir una imagen en una máscara basada en un canal de color especificado. Permite la extracción de capas de máscara correspondientes a los canales rojo, verde, azul o alfa de una imagen, facilitando operaciones que requieren enmascaramiento o procesamiento específico de canales.

## Entradas

| Parámetro   | Data Type | Descripción                                                                                                          |
|-------------|-------------|----------------------------------------------------------------------------------------------------------------------|
| `image`     | `IMAGE`     | El parámetro 'image' representa la imagen de entrada de la cual se generará una máscara basada en el canal de color especificado. Juega un papel crucial en la determinación del contenido y las características de la máscara resultante. |
| `channel`   | COMBO[STRING] | El parámetro 'channel' especifica qué canal de color (rojo, verde, azul o alfa) de la imagen de entrada debe usarse para generar la máscara. Esta elección influye directamente en la apariencia de la máscara y en qué partes de la imagen se destacan o se enmascaran. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `mask`    | `MASK`      | La salida 'mask' es una representación binaria o en escala de grises del canal de color especificado de la imagen de entrada, útil para un procesamiento de imágenes adicional o para operaciones de enmascaramiento. |
