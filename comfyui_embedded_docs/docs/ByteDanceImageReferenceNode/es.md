> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/es.md)

El nodo ByteDance Image Reference genera videos utilizando un texto descriptivo y de una a cuatro imágenes de referencia. Envía las imágenes y el texto a un servicio API externo que crea un video que coincide con tu descripción mientras incorpora el estilo visual y el contenido de tus imágenes de referencia. El nodo proporciona varios controles para la resolución del video, relación de aspecto, duración y otros parámetros de generación.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | seedance_1_lite | seedance_1_lite | Nombre del modelo |
| `prompt` | STRING | STRING | - | - | El texto descriptivo utilizado para generar el video. |
| `images` | IMAGE | IMAGE | - | - | De una a cuatro imágenes. |
| `resolution` | STRING | COMBO | - | 480p, 720p | La resolución del video de salida. |
| `aspect_ratio` | STRING | COMBO | - | adaptive, 16:9, 4:3, 1:1, 3:4, 9:16, 21:9 | La relación de aspecto del video de salida. |
| `duration` | INT | INT | 5 | 3-12 | La duración del video de salida en segundos. |
| `seed` | INT | INT | 0 | 0-2147483647 | Semilla a utilizar para la generación. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Si añadir o no una marca de agua de "Generado por IA" al video. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado basado en el texto descriptivo y las imágenes de referencia de entrada. |
