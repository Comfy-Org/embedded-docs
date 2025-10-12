> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/es.md)

El nodo Kling Text to Video Camera Control transforma texto en videos cinematográficos con movimientos de cámara profesionales que simulan cinematografía del mundo real. Este nodo permite controlar acciones de cámara virtual que incluyen zoom, rotación, paneo, inclinación y vista en primera persona, manteniendo el enfoque en su texto original. La duración, el modo y el nombre del modelo están codificados porque el control de cámara solo es compatible en modo pro con el modelo kling-v1-5 en duración de 5 segundos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación de texto positiva |
| `negative_prompt` | STRING | Sí | - | Indicación de texto negativa |
| `cfg_scale` | FLOAT | No | 0.0-1.0 | Controla qué tan estrechamente la salida sigue la indicación (valor predeterminado: 0.75) |
| `aspect_ratio` | COMBO | No | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | La relación de aspecto para el video generado (valor predeterminado: "16:9") |
| `camera_control` | CAMERA_CONTROL | No | - | Puede crearse utilizando el nodo Kling Camera Controls. Controla el movimiento y la acción de la cámara durante la generación del video. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video_id` | VIDEO | El video generado con efectos de control de cámara |
| `duration` | STRING | El identificador único para el video generado |
| `duration` | STRING | La duración del video generado |