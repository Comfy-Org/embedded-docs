> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/es.md)

Este nodo genera un video a partir de una descripción de texto utilizando el modelo Wan 2.7. Envía tu solicitud a una API externa, que procesa el *prompt* y devuelve un archivo de video. Opcionalmente, puedes proporcionar un clip de audio para influir en el movimiento y la sincronización del video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"wan2.7-t2v"` | El modelo específico a utilizar para la generación de video. |
| `model.prompt` | STRING | Sí | - | Una descripción de los elementos y características visuales que deseas en el video. Admite inglés y chino. |
| `model.negative_prompt` | STRING | No | - | Una descripción de los elementos o características que deseas evitar en el video generado. |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video de salida. |
| `model.ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto del video de salida. |
| `model.duration` | INT | Sí | 2 a 15 | La duración del video en segundos (por defecto: 5). |
| `audio` | AUDIO | No | - | Un archivo de audio para guiar la generación del video, como para sincronización de labios o coincidencia del movimiento con el ritmo. Si no se proporciona, el modelo generará música de fondo o efectos de sonido coincidentes. La duración del audio debe estar entre 3 y 30 segundos. |
| `seed` | INT | No | 0 a 2147483647 | Un número utilizado para controlar la aleatoriedad de la generación, asegurando resultados reproducibles (por defecto: 0). |
| `prompt_extend` | BOOLEAN | No | - | Cuando está habilitado, el *prompt* se mejorará con asistencia de IA (por defecto: True). |
| `watermark` | BOOLEAN | No | - | Cuando está habilitado, se añadirá una marca de agua generada por IA al resultado (por defecto: False). |

**Nota:** El parámetro `audio` es opcional. Si se proporciona, su duración debe estar entre 3 y 30 segundos. Si se omite, el modelo generará audio automáticamente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |