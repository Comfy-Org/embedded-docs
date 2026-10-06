# Kling Texto a Video (Control de Cámara)

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

El nodo de Control de Cámara para Video de Texto a Video de Kling transforma texto en videos cinematográficos con movimientos de cámara profesionales que simulan la cinematografía del mundo real. Este nodo permite controlar acciones de cámara virtual, incluyendo zoom, rotación, paneo, inclinación y vista en primera persona, manteniendo el enfoque en tu texto original. La duración, el modo y el nombre del modelo están codificados porque el control de cámara solo es compatible en modo profesional con el modelo kling-v1-5 a una duración de 5 segundos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto positivo | STRING | Sí | - |
| `negative_prompt` | Prompt de texto negativo | STRING | Sí | - |
| `cfg_scale` | Controla qué tan fielmente la salida sigue el prompt (predeterminado: 0.75) | FLOAT | No | 0.0-1.0 |
| `aspect_ratio` | La relación de aspecto para el video generado (predeterminado: "16:9") | COMBO | No | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" |
| `camera_control` | Se puede crear usando el nodo Controles de Cámara de Kling. Controla el movimiento y desplazamiento de la cámara durante la generación del video. | CAMERA_CONTROL | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | El video generado con efectos de control de cámara | VIDEO |
| `video_id` | El identificador único para el video generado | STRING |
| `duration` | La duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/es.md)

---
**Source fingerprint (SHA-256):** `4ebdd6af31f9e5c0816c4bcba886179b3f7d2b5030ff4fa3ddad6df25c528af7`
