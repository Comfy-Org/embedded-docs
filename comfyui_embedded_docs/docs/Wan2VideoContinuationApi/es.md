> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/es.md)

El nodo Wan 2.7 Video Continuation genera un nuevo segmento de video que continúa de forma fluida desde el final de un clip de video de entrada. Utiliza el modelo Wan 2.7 para sintetizar la continuación basándose en un texto descriptivo (prompt) y, opcionalmente, puede guiar el final hacia un fotograma objetivo específico.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | Sí | `"wan2.7-i2v"` | El modelo de generación de video a utilizar. |
| `model.prompt` | STRING | Sí | - | Texto descriptivo que detalla los elementos y características visuales. Admite inglés y chino. (valor por defecto: cadena vacía) |
| `model.negative_prompt` | STRING | Sí | - | Texto descriptivo negativo que especifica lo que se debe evitar. (valor por defecto: cadena vacía) |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución para el video de salida. |
| `model.duration` | INT | Sí | 2 a 15 | Duración total de la salida en segundos. El modelo genera la continuación para llenar el tiempo restante después del clip de entrada. (valor por defecto: 5) |
| `first_clip` | VIDEO | Sí | - | Video de entrada desde el cual continuar. Duración: 2s-10s. La relación de aspecto de la salida se deriva de este video. |
| `last_frame` | IMAGE | No | - | Imagen del último fotograma. La continuación hará una transición hacia este fotograma. |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla (seed) a utilizar para la generación. (valor por defecto: 0) |
| `prompt_extend` | BOOLEAN | Sí | - | Indica si se debe mejorar el texto descriptivo con asistencia de IA. (valor por defecto: True) |
| `watermark` | BOOLEAN | Sí | - | Indica si se debe agregar una marca de agua generada por IA al resultado. (valor por defecto: False) |

**Nota:** El video de entrada `first_clip` debe tener una duración entre 2 y 10 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `output` | VIDEO | La continuación de video generada. |