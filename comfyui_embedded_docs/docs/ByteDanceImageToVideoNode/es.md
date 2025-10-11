> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/es.md)

El nodo ByteDance Image to Video genera videos utilizando modelos de ByteDance a través de una API basándose en una imagen de entrada y un texto descriptivo. Toma una imagen de marco inicial y crea una secuencia de video que sigue la descripción proporcionada. El nodo ofrece varias opciones de personalización para la resolución de video, relación de aspecto, duración y otros parámetros de generación.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | COMBO | seedance_1_pro | Opciones de Image2VideoModelName | Nombre del modelo |
| `prompt` | STRING | STRING | - | - | El texto descriptivo utilizado para generar el video. |
| `image` | IMAGE | IMAGE | - | - | Primer fotograma que se utilizará para el video. |
| `resolution` | STRING | COMBO | - | ["480p", "720p", "1080p"] | La resolución del video de salida. |
| `aspect_ratio` | STRING | COMBO | - | ["adaptive", "16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | La relación de aspecto del video de salida. |
| `duration` | INT | INT | 5 | 3-12 | La duración del video de salida en segundos. |
| `seed` | INT | INT | 0 | 0-2147483647 | Semilla a utilizar para la generación. |
| `camera_fixed` | BOOLEAN | BOOLEAN | False | - | Especifica si se debe fijar la cámara. La plataforma añade una instrucción para fijar la cámara a su prompt, pero no garantiza el efecto real. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Si se debe añadir una marca de agua de "Generado por IA" al video. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado basado en la imagen de entrada y los parámetros del prompt. |