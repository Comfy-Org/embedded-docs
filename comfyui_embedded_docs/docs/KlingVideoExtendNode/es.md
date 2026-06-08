El Nodo de Extensión de Video Kling te permite extender videos creados por otros nodos Kling. Toma un video existente identificado por su ID de video y genera contenido adicional basado en tus indicaciones de texto. El nodo funciona enviando tu solicitud de extensión a la API de Kling y devuelve el video extendido junto con su nuevo ID y duración.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Indicación de texto positiva para guiar la extensión del video | STRING | No | - |
| `negative_prompt` | Indicación de texto negativa para elementos a evitar en el video extendido | STRING | No | - |
| `cfg_scale` | Controla la fuerza de la guía de la indicación (predeterminado: 0.5) | FLOAT | No | 0.0 - 1.0 |
| `video_id` | El ID del video a extender. Admite videos generados mediante texto a video, imagen a video y operaciones previas de extensión de video. La duración total después de la extensión no puede superar los 3 minutos. | STRING | Sí | - |

**Nota:** El `video_id` debe hacer referencia a un video creado por otros nodos Kling, y la duración total después de la extensión no puede superar los 3 minutos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | El video extendido generado por la API de Kling | VIDEO |
| `duration` | El identificador único para el video extendido | STRING |
| `duration` | La duración del video extendido | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/es.md)

---
**Source fingerprint (SHA-256):** `ecef4aedffe83bf384f2f9c3d8840f3fcab4b8c21e6e9afb36e177abb6f069fd`
