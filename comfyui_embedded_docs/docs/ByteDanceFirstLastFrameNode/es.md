> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/es.md)

Este nodo genera un video utilizando un texto descriptivo junto con imágenes del primer y último fotograma. Toma tu descripción y los dos fotogramas clave para crear una secuencia de video completa que transiciona entre ellos. El nodo proporciona varias opciones para controlar la resolución, relación de aspecto, duración y otros parámetros de generación del video.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | COMBO | combo | seedance_1_lite | seedance_1_lite | Nombre del modelo |
| `prompt` | STRING | string | - | - | El texto descriptivo utilizado para generar el video. |
| `first_frame` | IMAGE | image | - | - | Primer fotograma que se utilizará para el video. |
| `last_frame` | IMAGE | image | - | - | Último fotograma que se utilizará para el video. |
| `resolution` | COMBO | combo | - | 480p, 720p, 1080p | La resolución del video de salida. |
| `aspect_ratio` | COMBO | combo | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | La relación de aspecto del video de salida. |
| `duration` | INT | slider | 5 | 3-12 | La duración del video de salida en segundos. |
| `seed` | INT | number | 0 | 0-2147483647 | Semilla a utilizar para la generación. (opcional) |
| `camera_fixed` | BOOLEAN | boolean | False | - | Especifica si se debe fijar la cámara. La plataforma añade una instrucción para fijar la cámara a tu descripción, pero no garantiza el efecto real. (opcional) |
| `watermark` | BOOLEAN | boolean | True | - | Si se debe agregar una marca de agua de "Generado por IA" al video. (opcional) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |
