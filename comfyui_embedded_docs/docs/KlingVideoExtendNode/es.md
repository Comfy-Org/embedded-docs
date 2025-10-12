> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/es.md)

El nodo Kling Video Extend permite extender videos creados por otros nodos Kling. Toma un video existente identificado por su ID de video y genera contenido adicional basado en sus indicaciones de texto. El nodo funciona enviando su solicitud de extensión a la API de Kling y devolviendo el video extendido junto con su nuevo ID y duración.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | No | - | Indicación de texto positiva para guiar la extensión del video |
| `negative_prompt` | STRING | No | - | Indicación de texto negativa para elementos a evitar en el video extendido |
| `cfg_scale` | FLOAT | No | 0.0 - 1.0 | Controla la intensidad de la guía de la indicación (valor predeterminado: 0.5) |
| `video_id` | STRING | Sí | - | El ID del video a extender. Admite videos generados por operaciones de texto a video, imagen a video y extensiones de video anteriores. No puede exceder 3 minutos de duración total después de la extensión. |

**Nota:** El `video_id` debe hacer referencia a un video creado por otros nodos Kling, y la duración total después de la extensión no puede exceder los 3 minutos.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `video_id` | VIDEO | El video extendido generado por la API de Kling |
| `duration` | STRING | El identificador único para el video extendido |
| `duration` | STRING | La duración del video extendido |