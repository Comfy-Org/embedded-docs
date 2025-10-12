> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/es.md)

El nodo Kling Image to Video Camera Control transforma imágenes fijas en videos cinematográficos con movimientos de cámara profesionales. Este nodo especializado de imagen a video permite controlar acciones de cámara virtual que incluyen zoom, rotación, paneo, inclinación y vista en primera persona, manteniendo el enfoque en tu imagen original. El control de cámara actualmente solo es compatible en modo pro con el modelo kling-v1-5 y una duración de 5 segundos.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Sí | - | Imagen de referencia - URL o cadena codificada en Base64, no puede exceder 10MB, resolución no menor a 300*300px, relación de aspecto entre 1:2.5 ~ 2.5:1. Base64 no debe incluir el prefijo data:image. |
| `prompt` | STRING | Sí | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sí | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | No | 0.0-1.0 | Controla la fuerza de la guía de texto (predeterminado: 0.75) |
| `aspect_ratio` | COMBO | No | Múltiples opciones disponibles | Selección de relación de aspecto del video (predeterminado: 16:9) |
| `camera_control` | CAMERA_CONTROL | Sí | - | Puede crearse usando el nodo Kling Camera Controls. Controla el movimiento y la acción de la cámara durante la generación del video. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `video_id` | VIDEO | La salida de video generada |
| `duration` | STRING | Identificador único para el video generado |
| `duration` | STRING | Duración del video generado |