> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/es.md)

El nodo Kling Omni Edit Video (Pro) utiliza un modelo de IA para editar un video existente basándose en una descripción textual. Usted proporciona un video fuente y un *prompt*, y el nodo genera un nuevo video de la misma duración con los cambios solicitados. Opcionalmente, puede usar imágenes de referencia para guiar el estilo y conservar el audio original del video fuente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-video-o1"` | El modelo de IA a utilizar para la edición de video. |
| `prompt` | STRING | Sí | | Un *prompt* de texto que describe el contenido del video. Puede incluir descripciones tanto positivas como negativas. |
| `video` | VIDEO | Sí | | Video para editar. La duración del video de salida será la misma. |
| `keep_original_sound` | BOOLEAN | Sí | | Determina si se conserva el audio original del video de entrada en la salida (por defecto: True). |
| `reference_images` | IMAGE | No | | Hasta 4 imágenes de referencia adicionales. |
| `resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución para el video de salida (por defecto: "1080p"). |

**Restricciones y Limitaciones:**

* El `prompt` debe tener entre 1 y 2500 caracteres de longitud.
* El `video` de entrada debe tener una duración entre 3.0 y 10.05 segundos.
* Las dimensiones del `video` de entrada deben estar entre 720x720 y 2160x2160 píxeles.
* Se pueden proporcionar un máximo de 4 `reference_images` cuando se usa un video.
* Cada `reference_image` debe tener al menos 300x300 píxeles.
* Cada `reference_image` debe tener una relación de aspecto entre 1:2.5 y 2.5:1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El video editado generado por el modelo de IA. |
