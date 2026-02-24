> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/es.md)

Este nodo utiliza el modelo Kling AI para generar un video a partir de una descripción de texto. Envía su *prompt* a una API remota y devuelve el video generado. El nodo le permite controlar la duración, la forma y la calidad del video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-video-o1"` | El modelo específico de Kling a utilizar para la generación de video. |
| `prompt` | STRING | Sí | De 1 a 2500 caracteres | Un *prompt* de texto que describe el contenido del video. Puede incluir tanto descripciones positivas como negativas. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La forma o dimensiones del video a generar. |
| `duration` | COMBO | Sí | `5`<br>`10` | La duración del video en segundos. |
| `resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La calidad o resolución en píxeles del video (valor por defecto: `"1080p"`). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en el *prompt* de texto proporcionado. |
