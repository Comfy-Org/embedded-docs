# MinimaxHailuo03RegenerateNode

Este nodo vuelve a renderizar un video de salida MiniMax H3 768P en resolución 2K. Sube el video 768P sin modificar y el prompt exacto usado para generarlo, inicia un trabajo de regeneración MiniMax H3 y devuelve el video re-renderizado en 2K. Si la generación original usó primeros o últimos fotogramas o medios de referencia, adjunta las mismas entradas.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo a usar para la regeneración del video. Seleccionar "MiniMax H3" revela los ajustes de prompt, resolución y medios de referencia. | DYNAMIC_COMBO | Sí | "MiniMax H3" |
| `video` | El video de salida MiniMax H3 768P que se va a volver a renderizar. Conecta la salida sin modificar de un nodo de video MiniMax H3 (24 FPS, 4-15 segundos). No se pueden usar salidas 2K. | VIDEO | Sí | 24 FPS, 4-15 segundos |
| `first_frame` | Imagen del primer fotograma de la generación original, si se usó una. | IMAGE | No | Imagen |
| `last_frame` | Imagen del último fotograma de la generación original, si se usó una. | IMAGE | No | Imagen |
| `watermark` | Si se debe añadir una marca de agua AIGC al video. El valor predeterminado es false. | BOOLEAN | Sí | false / true |

### Entradas de MiniMax H3

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | El prompt exacto usado para generar el video de origen. No debe estar vacío. | STRING | Sí | Texto (multilínea) |
| `resolution` | Resolución a la que se volverá a renderizar el video de origen. | COMBO | Sí | "2K" |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `reference_images` | Ranura ampliable: conecta `image_1` hasta `image_9` (hasta 9 imágenes). Imágenes de referencia de la generación original, en el mismo orden. | IMAGE | No | 0-9 imágenes |
| `reference_videos` | Ranura ampliable: conecta `video_1` hasta `video_3` (hasta 3 videos). Videos de referencia de la generación original, en el mismo orden. | VIDEO | No | 0-3 videos |
| `reference_audios` | Ranura ampliable: conecta `audio_1` hasta `audio_3` (hasta 3 clips). Referencias de audio de la generación original, en el mismo orden. No se pueden usar sin una imagen o video de referencia. | AUDIO | No | 0-3 clips |

### Restricciones

- El `prompt` no debe estar vacío.
- El `video` de origen debe ser una salida MiniMax H3 768P sin modificar: 24 FPS, ancho y alto divisibles por 32, un máximo de 1.032.192 píxeles totales, y de 107 a 362 fotogramas en pasos de 17 (4 a 15 segundos a 24 FPS). No se pueden usar salidas 2K como origen.
- `first_frame` y `last_frame` son mutuamente excluyentes con los medios de referencia (`reference_images`, `reference_videos`, `reference_audios`). Usa fotogramas para un prompt de imagen a video, o medios de referencia para un prompt de referencia a video.
- `reference_audios` requiere al menos una entrada de `reference_images` o `reference_videos`.
- `first_frame`, `last_frame` y cada `reference_image` deben tener una relación de aspecto entre 0.4 y 2.5, y ser de al menos 256x256 píxeles.
- `reference_videos`: cada video debe tener entre 23.976 y 60 FPS y durar de 2 a 15 segundos; la duración total no puede exceder los 15 segundos.
- `reference_audios`: cada clip debe durar de 2 a 15 segundos; la duración total no puede exceder los 15 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video MiniMax H3 re-renderizado en resolución 2K. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/es.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
