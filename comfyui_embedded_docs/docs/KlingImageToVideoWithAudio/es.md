> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/es.md)

El nodo Kling Image(First Frame) to Video with Audio utiliza el modelo Kling AI para generar un video corto a partir de una imagen inicial y un texto descriptivo. Crea una secuencia de video que comienza con la imagen proporcionada y puede incluir opcionalmente audio generado por IA para acompañar las imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v2-6"` | La versión específica del modelo Kling AI que se utilizará para la generación de video. |
| `start_frame` | IMAGE | Sí | - | La imagen que servirá como el primer fotograma del video generado. La imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. |
| `prompt` | STRING | Sí | - | Texto descriptivo positivo. Describe el contenido del video que se desea generar. El texto debe tener entre 1 y 2500 caracteres. |
| `mode` | COMBO | Sí | `"pro"` | El modo operativo para la generación del video. |
| `duration` | COMBO | Sí | `5`<br>`10` | La duración del video a generar, en segundos. |
| `generate_audio` | BOOLEAN | No | - | Cuando está habilitado, el nodo generará audio para acompañar el video. Cuando está deshabilitado, el video será silencioso. (valor por defecto: True) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video generado, que puede incluir audio dependiendo de la entrada `generate_audio`. |
