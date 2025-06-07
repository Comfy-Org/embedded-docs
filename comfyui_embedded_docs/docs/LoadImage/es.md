
El nodo LoadImage está diseñado para cargar y preprocesar imágenes desde una ruta especificada. Maneja formatos de imagen con múltiples fotogramas, aplica transformaciones necesarias como la rotación basada en datos EXIF, normaliza los valores de los píxeles y, opcionalmente, genera una máscara para imágenes con un canal alfa. Este nodo es esencial para preparar imágenes para un procesamiento o análisis posterior dentro de una tubería.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|--------------|-------------|
| `image`   | COMBO[STRING] | El parámetro 'image' especifica el identificador de la imagen que se va a cargar y procesar. Es crucial para determinar la ruta al archivo de imagen y posteriormente cargar la imagen para su transformación y normalización. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La imagen procesada, con valores de píxeles normalizados y transformaciones aplicadas según sea necesario. Está lista para un procesamiento o análisis posterior. |
| `mask`    | `MASK`      | Una salida opcional que proporciona una máscara para la imagen, útil en escenarios donde la imagen incluye un canal alfa para transparencia. |
