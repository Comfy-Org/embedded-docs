El nodo ImageQuantize está diseñado para reducir el número de colores en una imagen a un número especificado, aplicando opcionalmente técnicas de dithering para mantener la calidad visual. Este proceso es útil para crear imágenes basadas en paletas o reducir la complejidad de color para ciertas aplicaciones.

## Entradas

| Campo   | Data Type | Descripción                                                                       |
|---------|-------------|-----------------------------------------------------------------------------------|
| `image` | `IMAGE`     | El tensor de imagen de entrada a cuantizar. Afecta la ejecución del nodo al ser el dato principal sobre el cual se realiza la reducción de color. |
| `colors`| `INT`       | Especifica el número de colores al que se debe reducir la imagen. Influye directamente en el proceso de cuantización al determinar el tamaño de la paleta de colores. |
| `dither`| COMBO[STRING] | Determina la técnica de dithering a aplicar durante la cuantización, afectando la calidad visual y apariencia de la imagen de salida. |

## Salidas

| Campo | Data Type | Descripción                                                                   |
|-------|-------------|-------------------------------------------------------------------------------|
| `image`| `IMAGE`     | La versión cuantizada de la imagen de entrada, con complejidad de color reducida y opcionalmente con dithering para mantener la calidad visual. |
