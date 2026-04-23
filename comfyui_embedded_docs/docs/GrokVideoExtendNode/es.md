> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/es.md)

El nodo Grok Video Extend utiliza un modelo de IA para crear una continuación fluida de un video existente. Proporcionas un video corto y un texto que describe lo que debería suceder a continuación, y el nodo genera un nuevo clip de video que sigue al original.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción textual de lo que debería suceder a continuación en el video. |
| `video` | VIDEO | Sí | N/A | Video fuente a extender. Formato MP4, de 2 a 15 segundos. |
| `model` | COMBO | Sí | `"grok-imagine-video"` | El modelo a utilizar para la extensión de video. Al seleccionarlo, revela un parámetro `duration`. |
| `seed` | INT | No | 0 a 2147483647 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). |

**Restricciones de Parámetros:**
*   La entrada `video` debe ser un archivo MP4 de entre 2 y 15 segundos de duración y no puede superar los 50MB de tamaño de archivo.
*   El `prompt` debe contener al menos un carácter (los espacios en blanco se recortan).
*   El parámetro `model` es un combo dinámico. Al seleccionar la opción "grok-imagine-video" se revela un parámetro anidado `duration`, que controla la longitud de la extensión en segundos (por defecto: 8, rango: 2 a 10).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La nueva extensión de video generada. |