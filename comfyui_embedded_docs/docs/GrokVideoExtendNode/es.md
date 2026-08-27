# Extender video Grok

El nodo Grok Video Extend utiliza un modelo de IA para crear una continuación perfecta de un video existente. Proporcionas un video corto y una indicación de texto que describe lo que debería suceder a continuación, y el nodo genera un nuevo clip de video que continúa al original.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo que se utilizará para la extensión de video. | DYNAMIC_COMBO | Sí | `"grok-imagine-video"` |
| `prompt` | Descripción de texto de lo que debería suceder a continuación en el video. | STRING | Sí | N/A |
| `video` | Video de origen a extender. Formato MP4, de 2 a 15 segundos. | VIDEO | Sí | N/A |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 2147483647 |

### Entradas de grok-imagine-video

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duración de la extensión en segundos (predeterminado: 8). | INT | Sí | 2 a 10 |

**Restricciones de parámetros:**
*   La entrada `video` debe ser un archivo MP4 de entre 2 y 15 segundos de duración y no puede superar los 50MB de tamaño de archivo.
*   El `prompt` debe contener al menos un carácter después de eliminar los espacios en blanco.
*   El parámetro `model` es un combo dinámico. Seleccionar la opción "grok-imagine-video" revela el parámetro anidado `duration`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La extensión de video recién generada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/es.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
