# ByteDance Seedance 2.0 Referencia a Video

Este nodo genera, edita o extiende videos con los modelos de IA Seedance 2.5 o 2.0 de ByteDance. El video se describe en un prompt de texto y se pueden añadir imágenes, videos y audio de referencia para guiar el resultado. Admite entradas de referencia multimodales, edición de video y extensión de video.

## Entradas

Al seleccionar un `model` se determina cuáles de los parámetros siguientes están disponibles. `video_editing` y `output_format` aparecen solo cuando se selecciona Seedance 2.5.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de IA utilizado para generar el video. Seedance 2.5 es el modelo más reciente, con videos de hasta 30 segundos y salida en mp4/mov; Seedance 2.0 está orientado a la máxima calidad y a 1080p/4k; Fast está optimizado para la velocidad; Mini es para la generación más rápida y de menor costo. Al seleccionar un modelo se muestran las entradas específicas de dicho modelo que se indican a continuación. | COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `watermark` | Indica si se añade una marca de agua al video (predeterminado: False). | BOOLEAN | Sí | `True`<br>`False` |
| `prompt` | Prompt de texto para la generación de video. Para Seedance 2.5, las líneas habladas deben ir entre comillas dobles para dirigir el diálogo generado. Debe contener al menos un carácter que no sea un espacio en blanco. | STRING | Sí | Any text |
| `resolution` | Resolución del video de salida. Seedance 2.5, 2.0 Fast y 2.0 Mini ofrecen 480p y 720p; Seedance 2.0 también ofrece 1080p y 4k (predeterminado de Seedance 2.5: 720p). | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida (predeterminado de Seedance 2.5: `"16:9"`; predeterminado de los modelos Seedance 2.0: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (Seedance 2.5: 4-30, predeterminado 5; modelos Seedance 2.0: 4-15, predeterminado 7). | INT | Sí | 4 a 30 (Seedance 2.5)<br>4 a 15 (Seedance 2.0)<br>Step: 1 |
| `generate_audio` | Activa la generación de audio para el video de salida (predeterminado: True). | BOOLEAN | Sí | `True`<br>`False` |
| `video_editing` | Solo Seedance 2.5. Actívela cuando el prompt edite un video de referencia conectado, por ejemplo, para reemplazar un objeto en él. La salida conserva entonces la duración y la relación de aspecto propias del clip de origen, y los controles de duración y relación de aspecto se ignoran. Déjela desactivada para generar un video nuevo, o para extender uno hasta la duración que establezca (predeterminado: False). | BOOLEAN | Sí | `True`<br>`False` |
| `output_format` | Solo Seedance 2.5. Formato contenedor del video de salida (predeterminado: `"mp4"`). | COMBO | Sí | `"mp4"` |
| `reference_images` | Imágenes de referencia que guían la generación del video. Las imágenes se reducen automáticamente de escala a un lado máximo de 6000 píxeles y deben tener al menos 300x300 píxeles con una relación de aspecto entre 0.4 y 2.5. | IMAGE | No | Up a 30 (Seedance 2.5)<br>Up a 9 (Seedance 2.0) |
| `reference_videos` | Videos de referencia que guían la generación del video; se usan para la edición y extensión de video. | VIDEO | No | Up a 10 (Seedance 2.5)<br>Up a 3 (Seedance 2.0) |
| `reference_audios` | Clips de audio de referencia que guían la generación del video. | AUDIO | No | Up a 10 (Seedance 2.5)<br>Up a 3 (Seedance 2.0) |
| `auto_downscale` | Reduce automáticamente la escala de los videos de referencia que superen el presupuesto de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya están dentro de los límites no se modifican (predeterminado: True). | BOOLEAN | No | `True`<br>`False` |
| `auto_upscale` | Aumenta automáticamente la escala de los videos de referencia que estén por debajo del recuento mínimo de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya cumplen el mínimo no se modifican. Nota: aumentar la escala de una fuente de baja resolución no añade detalle real y puede producir generaciones de menor calidad (predeterminado: False). | BOOLEAN | No | `True`<br>`False` |
| `reference_assets` | IDs de recursos de la biblioteca virtual de Seedance creados anteriormente (imagen, video o audio) para usar como referencias. Cada recurso debe existir y tener un estado Active. En el prompt, los recursos pueden mencionarse como asset1, asset 2, etc.; el nodo reemplaza estos tokens por etiquetas como Image 2. | STRING | No | Up a 30 (Seedance 2.5)<br>Up a 9 (Seedance 2.0) |

**Restricciones importantes:**

* Se requiere al menos una referencia. Para Seedance 2.0, 2.0 Fast y 2.0 Mini, debe proporcionar al menos una referencia de imagen o video (mediante `reference_images`, `reference_videos` o una entrada de `reference_assets` de imagen/video). Seedance 2.5 también acepta referencias de solo audio.
* El número de referencias depende del modelo: Seedance 2.5 permite hasta 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` y 30 `reference_assets`; los modelos Seedance 2.0 permiten hasta 9 imágenes, 3 videos, 3 clips de audio y 9 recursos. Los totales se calculan combinando las entradas directas y las referencias de recursos, y se validan antes de la generación.
* Cada video de referencia debe durar al menos 1.8 segundos, y cada clip de audio de referencia, al menos 1.8 segundos. La duración total de todos los videos de referencia y de todos los audios de referencia debe mantenerse dentro del límite del modelo seleccionado (15.1 segundos para los modelos Seedance 2.0).
* Los videos de referencia también deben cumplir los límites de recuento de píxeles del modelo para la resolución seleccionada. Con `auto_downscale` activado (predeterminado), los videos demasiado grandes se redimensionan automáticamente; con `auto_upscale` activado, los videos demasiado pequeños se amplían. Si cualquiera de los ajustes automáticos está desactivado, los videos que queden fuera del límite correspondiente generan un error.
* Cuando `video_editing` está activado en Seedance 2.5, las entradas `duration` y `ratio` se ignoran; la salida coincide con la duración y la relación de aspecto propias del video de referencia.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
