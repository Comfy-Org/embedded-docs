# Extender video Grok

El nodo Grok Video Extend utiliza un modelo de IA para crear una continuación sin interrupciones de un video existente. Proporcionas un video corto y un prompt de texto que describa qué debería ocurrir a continuación, y el nodo genera un nuevo clip de video que continúa a partir del original.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo que se utilizará para la extensión de video. | DYNAMIC_COMBO | Sí | `"grok-imagine-video"` |
| `prompt` | Descripción textual de lo que debería suceder a continuación en el video. | STRING | Sí | N/A |
| `video` | Video de origen para extender. Formato MP4, de 2 a 15 segundos. | VIDEO | Sí | N/A |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | No | 0 to 2147483647 |

### Entradas de grok-imagine-video

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duración de la extensión en segundos (por defecto: 8). | INT | Sí | 2 to 10 |

**Restricciones de parámetros:**

- La entrada `video` debe ser un archivo MP4 de entre 2 y 15 segundos de duración y no puede superar los 50MB de tamaño.
- El `prompt` debe contener al menos un carácter (se recortan los espacios en blanco).
- El parámetro `model` es un combo dinámico. Al seleccionar la opción "grok-imagine-video" se revela el parámetro anidado `duration`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La extensión de video recién generada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/es.md)

---
**Source fingerprint (SHA-256):** `bfaf56dd12afab13c820345587db9ee871db87d60b8dc003f00f035513dbdf61`
