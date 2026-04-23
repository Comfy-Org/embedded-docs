> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/es.md)

El nodo Wan2VideoEditApi utiliza el modelo Wan 2.7 para editar un video basándose en instrucciones de texto, imágenes de referencia o transferencia de estilo. Procesa el video de entrada y genera un nuevo video de acuerdo con los parámetros especificados, como resolución, duración y relación de aspecto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"wan2.7-videoedit"` | El modelo a utilizar para la edición de video. |
| `model.prompt` | STRING | Sí | - | Instrucciones de edición o requisitos de transferencia de estilo. (valor por defecto: cadena vacía) |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución para el video de salida. |
| `model.ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto para el video de salida. Si no se cambia, aproxima la relación del video de entrada. |
| `model.duration` | COMBO | Sí | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | La duración de salida en segundos. 'auto' coincide con la duración del video de entrada. Un valor específico trunca desde el inicio del video. (valor por defecto: "auto") |
| `model.reference_images` | IMAGE | No | - | Una lista de hasta 4 imágenes de referencia para guiar la edición. |
| `video` | VIDEO | Sí | - | El video a editar. |
| `seed` | INT | No | 0 a 2147483647 | La semilla a utilizar para la generación. (valor por defecto: 0) |
| `audio_setting` | COMBO | No | `"auto"`<br>`"origin"` | 'auto': el modelo decide si regenerar el audio basándose en la instrucción. 'origin': preserva el audio original del video de entrada. (valor por defecto: "auto") |
| `watermark` | BOOLEAN | No | - | Si se debe agregar una marca de agua generada por IA al resultado. (valor por defecto: Falso) |

**Restricciones:**
*   El `model.prompt` debe tener al menos 1 carácter de longitud.
*   El `video` de entrada debe tener una duración entre 2 y 10 segundos.
*   La entrada `model.reference_images` puede aceptar un máximo de 4 imágenes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video editado generado por el modelo. |