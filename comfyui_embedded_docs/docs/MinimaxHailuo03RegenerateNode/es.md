# MinimaxHailuo03RegenerateNode

```markdown
Este nodo vuelve a renderizar una salida de video MiniMax H3 768P en resolución 2K. Sube el video de origen y el prompt exacto utilizado para crearlo, inicia un trabajo de regeneración MiniMax H3 y devuelve el video 2K re-renderizado. Si la generación original utilizó primeros o últimos fotogramas o medios de referencia, adjunta las mismas entradas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo a utilizar para la regeneración de video. Al seleccionar este modelo se muestran la configuración de prompt, resolución y medios de referencia que se documentan a continuación. | COMBO | Sí | "MiniMax H3" |
| `prompt` | El prompt exacto utilizado para generar el video de origen. No debe estar vacío. | STRING | Sí | Text |
| `resolution` | Resolución a la que se volverá a renderizar el video de origen. | COMBO | Sí | "2K" |
| `reference_images` | Imágenes de referencia de la generación original, en el mismo orden. Hasta 9 imágenes. | IMAGE | No | 0-9 images |
| `reference_videos` | Videos de referencia de la generación original, en el mismo orden. Hasta 3 videos, de 2 a 15 segundos cada uno, 15 segundos en total. | VIDEO | No | 0-3 videos |
| `reference_audios` | Referencias de audio de la generación original, en el mismo orden. Hasta 3 clips, de 2 a 15 segundos cada uno, 15 segundos en total. No se pueden utilizar sin una imagen o video de referencia. | AUDIO | No | 0-3 clips |
| `video` | El video de salida MiniMax H3 768P que se va a volver a renderizar. Conecta la salida sin modificar de un nodo de video MiniMax H3 (24 FPS, 4-15 segundos). No se pueden utilizar salidas 2K. | VIDEO | Sí | 24 FPS, 4-15 seconds |
| `first_frame` | Imagen del primer fotograma de la generación original, si se utilizó uno. | IMAGE | No | Image |
| `last_frame` | Imagen del último fotograma de la generación original, si se utilizó uno. | IMAGE | No | Image |
| `watermark` | Si se debe añadir una marca de agua AIGC al video. El valor predeterminado es false. | BOOLEAN | Sí | false / true |

### Restricciones

- El `video` de origen debe ser una salida MiniMax H3 768P sin modificar: ancho y alto divisibles por 32, como máximo 1,032,192 píxeles en total, 24 FPS y 107 a 362 fotogramas en incrementos de 17 (4 a 15 segundos a 24 FPS). No se pueden utilizar salidas 2K como origen.
- `first_frame` / `last_frame` y los medios de referencia (`reference_images`, `reference_videos`, `reference_audios`) son mutuamente excluyentes. Utiliza fotogramas para un prompt de imagen a video, o medios de referencia para un prompt de referencia a video.
- `reference_audios` requiere al menos una entrada de `reference_images` o `reference_videos`.
- `reference_images`: cada imagen debe tener una relación de aspecto entre 0.4 y 2.5 y tener al menos 256x256 píxeles.
- `reference_videos`: cada video debe tener entre 23.976 y 60 FPS y durar de 2 a 15 segundos; la duración total no puede exceder los 15 segundos.
- `reference_audios`: cada clip debe durar de 2 a 15 segundos; la duración total no puede exceder los 15 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video MiniMax H3 re-renderizado en resolución 2K. | VIDEO |
```

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/es.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
