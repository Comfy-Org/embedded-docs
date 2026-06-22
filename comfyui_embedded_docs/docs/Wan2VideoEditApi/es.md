# Wan 2.7 Edición de Video

El nodo Wan2VideoEditApi utiliza el modelo Wan 2.7 para editar un video basándose en instrucciones de texto, imágenes de referencia o transferencia de estilo. Procesa el video de entrada y genera un nuevo video de acuerdo con los parámetros especificados, como resolución, duración y relación de aspecto.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la edición de video. | COMBO | Sí | `"wan2.7-videoedit"` |
| `model.prompt` | Instrucciones de edición o requisitos de transferencia de estilo. (por defecto: cadena vacía) | STRING | Sí | - |
| `model.resolution` | La resolución del video de salida. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `model.ratio` | La relación de aspecto del video de salida. Si no se modifica, se aproxima a la relación de aspecto del video de entrada. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | La duración de salida en segundos. 'auto' coincide con la duración del video de entrada. Un valor específico trunca desde el inicio del video. (por defecto: "auto") | COMBO | Sí | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `model.reference_images` | Una lista de hasta 4 imágenes de referencia para guiar la edición. | IMAGE | No | - |
| `video` | El video a editar. | VIDEO | Sí | - |
| `semilla` | La semilla a utilizar para la generación. (por defecto: 0) | INT | No | 0 a 2147483647 |
| `configuración_de_audio` | 'auto': el modelo decide si regenerar el audio según el prompt. 'origin': conserva el audio original del video de entrada. (por defecto: "auto") | COMBO | No | `"auto"`<br>`"origin"` |
| `marca de agua` | Si se debe agregar una marca de agua generada por IA al resultado. (por defecto: Falso) | BOOLEAN | No | - |

**Restricciones:**
*   El `model.prompt` debe tener al menos 1 carácter de longitud.
*   El `video` de entrada debe tener una duración entre 2 y 10 segundos.
*   La entrada `model.reference_images` puede aceptar un máximo de 4 imágenes.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video editado generado por el modelo. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/es.md)

---
**Source fingerprint (SHA-256):** `d2dd65d743358c6a357e75076774e93c52c39893fbb376da2f4395446f440a20`
