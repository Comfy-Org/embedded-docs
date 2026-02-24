> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/es.md)

Este nodo utiliza el modelo Kling AI para generar un nuevo video basado en un video de entrada e imágenes de referencia opcionales. Proporcionas un texto descriptivo (prompt) que describe el contenido deseado, y el nodo transforma el video de referencia en consecuencia. También puede incorporar hasta cuatro imágenes de referencia adicionales para guiar el estilo y el contenido de la salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-video-o1"` | El modelo Kling específico a utilizar para la generación de video. |
| `prompt` | STRING | Sí | N/A | Un texto descriptivo (prompt) que describe el contenido del video. Puede incluir tanto descripciones positivas como negativas. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La relación de aspecto deseada para el video generado. |
| `duration` | INT | Sí | 3 a 10 | La duración del video generado en segundos (por defecto: 3). |
| `reference_video` | VIDEO | Sí | N/A | Video a utilizar como referencia. |
| `keep_original_sound` | BOOLEAN | Sí | N/A | Determina si el audio del video de referencia se conserva en la salida (por defecto: True). |
| `reference_images` | IMAGE | No | N/A | Hasta 4 imágenes de referencia adicionales. |
| `resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución para el video generado (por defecto: "1080p"). |

**Restricciones de Parámetros:**

* El `prompt` debe tener entre 1 y 2500 caracteres de longitud.
* El `reference_video` debe tener una duración entre 3.0 y 10.05 segundos.
* El `reference_video` debe tener dimensiones entre 720x720 y 2160x2160 píxeles.
* Se pueden proporcionar un máximo de 4 `reference_images`. Cada imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video recién generado. |
