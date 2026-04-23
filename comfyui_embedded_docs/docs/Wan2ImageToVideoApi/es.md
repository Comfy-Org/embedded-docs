> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/es.md)

El nodo Wan 2.7 Image to Video genera un vídeo a partir de una imagen de primer fotograma. Opcionalmente, puedes proporcionar una imagen de último fotograma para crear una transición entre ambas, o proporcionar un archivo de audio para guiar el movimiento y la sincronización del vídeo. El nodo utiliza un modelo de IA para animar la escena basándose en tu descripción textual.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"wan2.7-i2v"` | El modelo de IA a utilizar para la generación del vídeo. |
| `model.prompt` | STRING | Sí | - | Una descripción textual de los elementos y características visuales que deseas en el vídeo. Admite inglés y chino. |
| `model.negative_prompt` | STRING | Sí | - | Una descripción textual de los elementos o características que quieres que el modelo evite. |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del vídeo de salida. |
| `model.duration` | INT | Sí | 2 a 15 | La duración del vídeo generado en segundos (por defecto: 5). |
| `first_frame` | IMAGE | Sí | - | La imagen que se utilizará como primer fotograma del vídeo. La relación de aspecto del vídeo de salida se deriva de esta imagen. |
| `last_frame` | IMAGE | No | - | Una imagen opcional para usar como último fotograma. Cuando se proporciona, el modelo genera un vídeo que transita desde el primer fotograma hasta este último. |
| `audio` | AUDIO | No | - | Un archivo de audio opcional para guiar la generación del vídeo, útil para sincronización labial o movimiento ajustado al ritmo. La duración debe estar entre 2 y 30 segundos. Si no se proporciona, el modelo generará música de fondo o efectos de sonido acordes. |
| `seed` | INT | Sí | 0 a 2147483647 | Un valor de semilla para controlar la aleatoriedad de la generación (por defecto: 0). |
| `prompt_extend` | BOOLEAN | Sí | - | Cuando está habilitado, el nodo utilizará asistencia de IA para mejorar tu indicación textual (por defecto: True). Es un ajuste avanzado. |
| `watermark` | BOOLEAN | Sí | - | Cuando está habilitado, se añadirá una marca de agua generada por IA al vídeo final (por defecto: False). Es un ajuste avanzado. |

**Nota:** La entrada `audio` tiene una restricción de duración. Si se proporciona, el archivo de audio debe tener una duración entre 2 y 30 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de vídeo generado. |