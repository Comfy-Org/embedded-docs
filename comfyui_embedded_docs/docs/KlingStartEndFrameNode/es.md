> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/es.md)

El nodo Kling Inicio-Fin de Fotograma a Video crea una secuencia de video que transita entre las imágenes de inicio y fin proporcionadas. Genera todos los fotogramas intermedios para producir una transformación suave desde el primer fotograma hasta el último. Este nodo llama a la API de imagen a video pero solo admite las opciones de entrada que funcionan con el campo de solicitud `image_tail`.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Sí | - | Imagen de referencia - URL o cadena codificada en Base64, no puede exceder 10MB, resolución no menor a 300*300px, relación de aspecto entre 1:2.5 ~ 2.5:1. Base64 no debe incluir el prefijo data:image. |
| `end_frame` | IMAGE | Sí | - | Imagen de referencia - Control del fotograma final. URL o cadena codificada en Base64, no puede exceder 10MB, resolución no menor a 300*300px. Base64 no debe incluir el prefijo data:image. |
| `prompt` | STRING | Sí | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sí | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | No | 0.0-1.0 | Controla la intensidad de la guía del prompt (valor por defecto: 0.5) |
| `aspect_ratio` | COMBO | No | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"9:21"<br>"3:4"<br>"4:3" | La relación de aspecto para el video generado (valor por defecto: "16:9") |
| `mode` | COMBO | No | Múltiples opciones disponibles | La configuración a utilizar para la generación del video siguiendo el formato: modo / duración / nombre_del_modelo. (valor por defecto: tercera opción de los modos disponibles) |

**Restricciones de Imagen:**
- Tanto `start_frame` como `end_frame` deben ser proporcionados y no pueden exceder 10MB de tamaño de archivo
- Resolución mínima: 300×300 píxeles para ambas imágenes
- La relación de aspecto de `start_frame` debe estar entre 1:2.5 y 2.5:1
- Las imágenes codificadas en Base64 no deben incluir el prefijo "data:image"

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La secuencia de video generada |
| `video_id` | STRING | Identificador único para el video generado |
| `duration` | STRING | Duración del video generado |