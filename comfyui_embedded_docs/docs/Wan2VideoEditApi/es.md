> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/es.md)

El nodo Wan2VideoEditApi utiliza el modelo Wan 2.7 para editar un video basándose en instrucciones de texto, imágenes de referencia o transferencia de estilo. Procesa el video de entrada y genera un nuevo video de acuerdo con los parámetros especificados, como resolución, duración y relación de aspecto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | COMBO | Sí | `"wan2.7-videoedit"` | El modelo a utilizar para la edición de video. |
| `model.prompt` | STRING | Sí | - | Instrucciones de edición o requisitos de transferencia de estilo. (por defecto: cadena vacía) |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video de salida. |
| `model.ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto del video de salida. Si no se modifica, se aproxima a la relación de aspecto del video de entrada. |
| `model.duration` | COMBO | Sí | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | La duración de salida en segundos. 'auto' coincide con la duración del video de entrada. Un valor específico trunca desde el inicio del video. (por defecto: "auto") |
| `model.reference_images` | IMAGE | No | - | Una lista de hasta 4 imágenes de referencia para guiar la edición. |
| `video` | VIDEO | Sí | - | El video a editar. |
| `semilla` | INT | No | 0 a 2147483647 | La semilla a utilizar para la generación. (por defecto: 0) |
| `configuración_de_audio` | COMBO | No | `"auto"`<br>`"origin"` | 'auto': el modelo decide si regenerar el audio según el prompt. 'origin': conserva el audio original del video de entrada. (por defecto: "auto") |
| `marca de agua` | BOOLEAN | No | - | Si se debe agregar una marca de agua generada por IA al resultado. (por defecto: Falso) |

**Restricciones:**
*   El `model.prompt` debe tener al menos 1 carácter de longitud.
*   El `video` de entrada debe tener una duración entre 2 y 10 segundos.
*   La entrada `model.reference_images` puede aceptar un máximo de 4 imágenes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video editado generado por el modelo. |

---
**Source fingerprint (SHA-256):** `d2dd65d743358c6a357e75076774e93c52c39893fbb376da2f4395446f440a20`
