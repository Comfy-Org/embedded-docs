# ByteDance Seedance 2.0 Referencia a Video

Este nodo genera, edita o extiende videos utilizando los modelos de IA Seedance 2.5 o 2.0 de ByteDance. Usted describe el video en un prompt de texto y puede añadir imágenes, videos y audio de referencia para guiar el resultado. Admite entradas de referencia multimodales, edición de video y extensión de video. Esta es la versión heredada y obsoleta del nodo Seedance de referencia a video.

## Entradas

La selección de un `model` determina cuáles de los parámetros siguientes están disponibles. `video_editing` y `output_format` aparecen solo cuando se selecciona Seedance 2.5. Los espacios de referencia ampliables y las opciones de ajuste automático de tamaño de los videos de referencia son comunes a todos los modelos y se describen en Entradas de referencia.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo de IA utilizado para generar el video. Seedance 2.5 para el modelo más reciente, videos de hasta 30 segundos y salida mp4/mov; Seedance 2.0 para máxima calidad y 4k; Fast para optimización de velocidad; Mini para la generación más rápida y de menor costo. Al seleccionar un modelo se muestran las entradas específicas de ese modelo que se enumeran a continuación. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 2147483647<br>Paso: 1 |
| `marca_de_agua` | Indica si se debe añadir una marca de agua al video (predeterminado: False). Configuración avanzada. | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de Seedance 2.5

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación del video. Coloque las líneas habladas entre comillas dobles para guiar el diálogo generado. Debe contener al menos un carácter que no sea un espacio en blanco (predeterminado: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida (predeterminado: `"720p"`). | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Relación de aspecto del video de salida (predeterminado: `"16:9"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (predeterminado: 5). | INT | Sí | 4 a 30<br>Paso: 1 |
| `generate_audio` | Habilitar la generación de audio para el video de salida (predeterminado: True). | BOOLEAN | Sí | `True`<br>`False` |
| `video_editing` | Habilitar cuando la indicación edita un video de referencia conectado, por ejemplo, reemplazando un objeto en él. La salida conserva entonces la duración y la relación de aspecto propias del clip de origen, y los controles de duración y relación de aspecto se ignoran. Déjelo deshabilitado para generar un video nuevo o para extender uno hasta la duración que establezca (predeterminado: False). | BOOLEAN | Sí | `True`<br>`False` |
| `output_format` | Formato de contenedor del video de salida (predeterminado: `"mp4"`). | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.0

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación del video. Debe contener al menos un carácter que no sea un espacio en blanco (predeterminado: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida (predeterminado: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (predeterminado: 7). | INT | Sí | 4 a 15<br>Paso: 1 |
| `generate_audio` | Habilitar la generación de audio para el video de salida (predeterminado: True). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Compartidas por Seedance 2.0 Fast y Seedance 2.0 Mini. Estos dos modelos exponen el mismo conjunto de entradas que Seedance 2.0, excepto que `resolution` está limitada a 480p y 720p.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación del video. Debe contener al menos un carácter que no sea un espacio en blanco (predeterminado: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida (predeterminado: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (predeterminado: 7). | INT | Sí | 4 a 15<br>Paso: 1 |
| `generate_audio` | Habilitar la generación de audio para el video de salida (predeterminado: True). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de referencia

Disponibles para todos los modelos. El número máximo de espacios depende del modelo seleccionado: Seedance 2.5 admite más referencias que los modelos Seedance 2.0.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `reference_images` | Espacio ampliable: conecte una o más imágenes de referencia (`image_1`, `image_2`, ...) que guíen la generación del video. Las imágenes se reducen automáticamente de escala hasta un lado máximo de 6000 píxeles y deben tener al menos 300x300 píxeles con una relación de aspecto entre 0.4 y 2.5. | IMAGE | No | Hasta 30 (Seedance 2.5)<br>Hasta 9 (modelos Seedance 2.0) |
| `reference_videos` | Espacio ampliable: conecte uno o más videos de referencia (`video_1`, `video_2`, ...) que guíen la generación del video; se utiliza para la edición y extensión de video. | VIDEO | No | Hasta 10 (Seedance 2.5)<br>Hasta 3 (modelos Seedance 2.0) |
| `reference_audios` | Espacio ampliable: conecte uno o más clips de audio de referencia (`audio_1`, `audio_2`, ...) que guíen la generación del video. | AUDIO | No | Hasta 10 (Seedance 2.5)<br>Hasta 3 (modelos Seedance 2.0) |
| `auto_downscale` | Reduce automáticamente la escala de los videos de referencia que excedan el presupuesto de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya están dentro de los límites no se modifican (predeterminado: True). | BOOLEAN | No | `True`<br>`False` |
| `auto_upscale` | Configuración avanzada. Aumenta automáticamente la escala de los videos de referencia que estén por debajo del recuento mínimo de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya cumplen el mínimo no se modifican. Nota: aumentar la escala de una fuente de baja resolución no añade detalle real y puede producir generaciones de menor calidad (predeterminado: False). | BOOLEAN | No | `True`<br>`False` |
| `reference_assets` | Espacio ampliable: IDs de recursos creados previamente en la biblioteca virtual de Seedance (Image, Video o Audio) para usar como referencias (`asset_1`, `asset_2`, ...). Cada recurso debe existir y tener estado Active. En el prompt, se puede hacer referencia a los recursos como `asset1`, `asset 1`, etc.; el nodo reemplaza estos tokens por etiquetas como "Image 2". | STRING | No | Hasta 30 (Seedance 2.5)<br>Hasta 9 (modelos Seedance 2.0) |

**Restricciones importantes:**

* Se requiere al menos una referencia. Para Seedance 2.0, 2.0 Fast y 2.0 Mini, debe proporcionar al menos una referencia de imagen o video (mediante `reference_images`, `reference_videos`, o una entrada de imagen o video en `reference_assets`). Seedance 2.5 acepta además referencias solo de audio (mediante `reference_audios` o una entrada de audio en `reference_assets`).
* Los recuentos de referencias dependen del modelo y se validan combinando las entradas directas y las referencias de recursos: Seedance 2.5 permite hasta 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` y 30 `reference_assets`; los modelos Seedance 2.0 permiten hasta 9 imágenes, 3 videos, 3 clips de audio y 9 recursos.
* Cada video de referencia debe durar al menos 1.8 segundos, y cada clip de audio de referencia debe durar al menos 1.8 segundos. La duración total de todos los videos de referencia y de todos los clips de audio de referencia debe mantenerse dentro del límite del modelo seleccionado (15.1 segundos para los modelos Seedance 2.0).
* Los videos de referencia también deben cumplir los límites de recuento de píxeles del modelo para la resolución seleccionada. Con `auto_downscale` habilitado (predeterminado), los videos sobredimensionados se redimensionan automáticamente; con `auto_upscale` habilitado, los videos de tamaño insuficiente se amplían. Si alguno de los ajustes automáticos está deshabilitado, los videos que estén fuera del límite correspondiente generan un error.
* Cuando `video_editing` está habilitado en Seedance 2.5, las entradas `duration` y `ratio` se ignoran; la salida coincide con la duración y la relación de aspecto propias del video de referencia. Si el proveedor interpreta el prompt como una edición de un video de referencia, la generación falla a menos que `video_editing` esté habilitado o que el prompt se reformule para describir un video nuevo.
* Si el proveedor rechaza la pista de audio generada para el video (por ejemplo, una posible coincidencia de derechos de autor), la tarea falla; deshabilitar `generate_audio` produce un video sin sonido.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
