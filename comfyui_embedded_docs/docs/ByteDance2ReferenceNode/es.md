# ByteDance Seedance 2.0 Referencia a Video

Este nodo genera, edita o extiende videos utilizando los modelos de IA Seedance 2.5 o 2.0 de ByteDance. Describes el video en un prompt de texto y puedes añadir imágenes, videos y audio de referencia para guiar el resultado. Admite entradas de referencia multimodales, edición de video y extensión de video.

## Entradas

Seleccionar un `model` determina cuáles de los parámetros siguientes están disponibles. `video_editing` y `output_format` aparecen solo cuando se selecciona Seedance 2.5. Las ranuras de referencia ampliables y las opciones de autoajuste de tamaño de los videos de referencia son comunes a todos los modelos y se describen en Entradas de referencia.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo de IA utilizado para generar el video. Seedance 2.5 para el modelo más nuevo, videos de hasta 30 segundos y salida mp4; Seedance 2.0 para máxima calidad y 1080p/4k; Fast para optimizar la velocidad; Mini para la generación más rápida y de menor costo. Seleccionar un modelo revela las entradas específicas del modelo que se enumeran a continuación. | COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 2147483647 |
| `marca_de_agua` | Si se debe añadir una marca de agua al video (por defecto: False). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de Seedance 2.5

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para la generación del video. Coloca las líneas habladas entre comillas dobles para dirigir el diálogo generado. Debe contener al menos un carácter que no sea un espacio en blanco (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida (por defecto: `"720p"`). | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida (por defecto: `"16:9"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (por defecto: 5). | INT | Sí | 4 a 30<br>Paso: 1 |
| `generate_audio` | Habilita la generación de audio para el video de salida (por defecto: True). | BOOLEAN | Sí | `True`<br>`False` |
| `video_editing` | Habilítalo cuando el prompt edita un video de referencia conectado, por ejemplo para reemplazar un objeto en él. La salida conserva entonces la duración y la relación de aspecto propias del clip de origen, y los widgets de duración y relación de aspecto se ignoran. Déjalo deshabilitado para generar un video nuevo o para extender uno hasta la duración que establezcas (por defecto: False). | BOOLEAN | Sí | `True`<br>`False` |
| `output_format` | Formato de contenedor del video de salida (por defecto: `"mp4"`). | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.0

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para la generación del video. Debe contener al menos un carácter que no sea un espacio en blanco (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida (por defecto: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (por defecto: 7). | INT | Sí | 4 a 15<br>Paso: 1 |
| `generate_audio` | Habilita la generación de audio para el video de salida (por defecto: True). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Compartidas por Seedance 2.0 Fast y Seedance 2.0 Mini. Estos dos modelos exponen el mismo conjunto de entradas que Seedance 2.0, excepto que `resolution` se limita a 480p y 720p.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para la generación del video. Debe contener al menos un carácter que no sea un espacio en blanco (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida (por defecto: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (por defecto: 7). | INT | Sí | 4 a 15<br>Paso: 1 |
| `generate_audio` | Habilita la generación de audio para el video de salida (por defecto: True). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de referencia

Disponibles para todos los modelos. El número máximo de ranuras depende del modelo seleccionado: Seedance 2.5 admite más referencias que los modelos Seedance 2.0.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Ranura ampliable: conecta una o más imágenes de referencia (`image_1`, `image_2`, ...) que guían la generación del video. Las imágenes se reducen automáticamente a un lado máximo de 6000 píxeles y deben tener al menos 300x300 píxeles con una relación de aspecto entre 0.4 y 2.5. | IMAGE | No | Hasta 30 (Seedance 2.5)<br>Hasta 9 (modelos Seedance 2.0) |
| `reference_videos` | Ranura ampliable: conecta uno o más videos de referencia (`video_1`, `video_2`, ...) que guían la generación del video; se utiliza para la edición y extensión de video. | VIDEO | No | Hasta 10 (Seedance 2.5)<br>Hasta 3 (modelos Seedance 2.0) |
| `reference_audios` | Ranura ampliable: conecta uno o más clips de audio de referencia (`audio_1`, `audio_2`, ...) que guían la generación del video. | AUDIO | No | Hasta 10 (Seedance 2.5)<br>Hasta 3 (modelos Seedance 2.0) |
| `auto_downscale` | Reduce automáticamente los videos de referencia que exceden el presupuesto de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya están dentro de los límites no se modifican (por defecto: True). | BOOLEAN | No | `True`<br>`False` |
| `auto_upscale` | Aumenta automáticamente la escala de los videos de referencia que están por debajo del recuento mínimo de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los videos que ya cumplen el mínimo no se modifican. Nota: aumentar la escala de una fuente de baja resolución no añade detalle real y puede producir generaciones de menor calidad (por defecto: False). | BOOLEAN | No | `True`<br>`False` |
| `reference_assets` | Ranura ampliable: IDs de activos de la biblioteca virtual de Seedance creados previamente (Imagen, Video o Audio) para usar como referencias (`asset_1`, `asset_2`, ...). Cada activo debe existir y tener un estado Activo. En el prompt, se puede hacer referencia a los activos como `asset1`, `asset 1`, etc.; el nodo reemplaza estos tokens con etiquetas como "Imagen 2". | STRING | No | Hasta 30 (Seedance 2.5)<br>Hasta 9 (modelos Seedance 2.0) |

**Restricciones importantes:**

* Se requiere al menos una referencia. Para Seedance 2.0, 2.0 Fast y 2.0 Mini, debes proporcionar al menos una referencia de imagen o video (a través de `reference_images`, `reference_videos` o una entrada de imagen o video en `reference_assets`). Seedance 2.5 acepta además referencias de solo audio (a través de `reference_audios` o una entrada de audio en `reference_assets`).
* Los recuentos de referencias dependen del modelo y se validan combinando las entradas directas y las referencias de activos: Seedance 2.5 permite hasta 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` y 30 `reference_assets`; los modelos Seedance 2.0 permiten hasta 9 imágenes, 3 videos, 3 clips de audio y 9 activos.
* Cada video de referencia debe durar al menos 1.8 segundos, y cada clip de audio de referencia debe durar al menos 1.8 segundos. La duración total de todos los videos de referencia y de todos los audios de referencia debe mantenerse dentro del límite del modelo seleccionado (15.1 segundos para los modelos Seedance 2.0).
* Los videos de referencia también deben cumplir los límites de recuento de píxeles del modelo para la resolución seleccionada. Con `auto_downscale` habilitado (por defecto), los videos sobredimensionados se redimensionan automáticamente; con `auto_upscale` habilitado, los videos subdimensionados se amplían. Si cualquiera de los ajustes automáticos está deshabilitado, los videos que estén fuera del límite correspondiente generan un error.
* Cuando `video_editing` está habilitado en Seedance 2.5, las entradas `duration` y `ratio` se ignoran; la salida coincide con la duración y la relación de aspecto propias del video de referencia. Si el proveedor interpreta el prompt como una edición de un video de referencia, la generación falla a menos que `video_editing` esté habilitado o el prompt se reformule para describir un video nuevo.
* Si el proveedor rechaza la pista de audio generada para el video (por ejemplo, una posible coincidencia de derechos de autor), la tarea falla; deshabilitar `generate_audio` produce un video silencioso.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `4429306ac40b0f04ce7176cd805b34164de5e4e2b7204b008ea076b57663c200`
