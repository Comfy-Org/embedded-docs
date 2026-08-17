# ByteDance Seedance 2.0 Referencia a Video

Este nodo genera, edita o extiende vídeos utilizando los modelos de IA Seedance 2.5 o 2.0 de ByteDance. Describe el vídeo en una indicación de texto y puede añadir imágenes, vídeos y audio de referencia para guiar el resultado. Admite entradas de referencia multimodales, edición de vídeo y extensión de vídeo. Esta es la versión heredada y obsoleta del nodo ByteDance Seedance 2.5 Reference to Video.

## Entradas

Seleccionar un `model` determina cuáles de los parámetros siguientes están disponibles. `video_editing` y `output_format` solo aparecen cuando se selecciona Seedance 2.5. Las ranuras de referencia ampliables y las opciones de redimensionado automático de vídeos de referencia son comunes a todos los modelos y se describen en Entradas de referencia.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo de IA utilizado para generar el vídeo. Seedance 2.5 para el modelo más reciente, vídeos de hasta 30 segundos y salida mp4/mov; Seedance 2.0 para la máxima calidad y 1080p/4k; Fast para optimizar la velocidad; Mini para la generación más rápida y de menor coste. Al seleccionar un modelo se muestran las entradas específicas de ese modelo que se indican a continuación. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | La semilla (`seed`) controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 2147483647<br>Paso: 1 |
| `watermark` | Indica si se debe añadir una marca de agua al vídeo (por defecto: False). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de Seedance 2.5

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Indicación de texto para la generación del vídeo. Ponga las frases habladas entre comillas dobles para dirigir el diálogo generado. Debe contener al menos un carácter que no sea un espacio en blanco (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del vídeo de salida (por defecto: `"720p"`). | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del vídeo de salida (por defecto: `"16:9"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del vídeo de salida en segundos (por defecto: 5). | INT | Sí | 4 a 30<br>Paso: 1 |
| `generate_audio` | Habilita la generación de audio para el vídeo de salida (por defecto: True). | BOOLEAN | Sí | `True`<br>`False` |
| `video_editing` | Habilite esta opción cuando la indicación edite un vídeo de referencia conectado, por ejemplo, para reemplazar un objeto en él. En ese caso, la salida conserva la duración y la relación de aspecto propias del clip de origen, y los controles de duración y relación de aspecto se ignoran. Mantenga esta opción desactivada para generar un vídeo nuevo o para extender uno hasta la duración que establezca (por defecto: False). | BOOLEAN | Sí | `True`<br>`False` |
| `output_format` | Formato de contenedor del vídeo de salida (por defecto: `"mp4"`). | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.0

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Indicación de texto para la generación del vídeo. Debe contener al menos un carácter que no sea un espacio en blanco (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del vídeo de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del vídeo de salida (por defecto: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del vídeo de salida en segundos (por defecto: 7). | INT | Sí | 4 a 15<br>Paso: 1 |
| `generate_audio` | Habilita la generación de audio para el vídeo de salida (por defecto: True). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Compartidas por Seedance 2.0 Fast y Seedance 2.0 Mini. Estos dos modelos exponen el mismo conjunto de entradas que Seedance 2.0, excepto que `resolution` se limita a 480p y 720p.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Indicación de texto para la generación del vídeo. Debe contener al menos un carácter que no sea un espacio en blanco (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del vídeo de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del vídeo de salida (por defecto: `"adaptive"`). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del vídeo de salida en segundos (por defecto: 7). | INT | Sí | 4 a 15<br>Paso: 1 |
| `generate_audio` | Habilita la generación de audio para el vídeo de salida (por defecto: True). | BOOLEAN | Sí | `True`<br>`False` |

### Entradas de referencia

Disponibles para todos los modelos. El número máximo de ranuras depende del modelo seleccionado: Seedance 2.5 admite más referencias que los modelos Seedance 2.0.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `reference_images` | Ranura ampliable: conecte una o más imágenes de referencia (`image_1`, `image_2`, ...) que guíen la generación del vídeo. El límite de cantidad depende del modelo (consulte las secciones de cada modelo). Las imágenes se reducen automáticamente a un lado máximo de 6000 píxeles y deben tener al menos 300x300 píxeles con una relación de aspecto entre 0.4 y 2.5. | IMAGE | No | Hasta 30 (Seedance 2.5)<br>Hasta 9 (modelos Seedance 2.0) |
| `reference_videos` | Ranura ampliable: conecte uno o más vídeos de referencia (`video_1`, `video_2`, ...) que guíen la generación del vídeo; se utilizan para la edición y extensión de vídeo. | VIDEO | No | Hasta 10 (Seedance 2.5)<br>Hasta 3 (modelos Seedance 2.0) |
| `reference_audios` | Ranura ampliable: conecte uno o más clips de audio de referencia (`audio_1`, `audio_2`, ...) que guíen la generación del vídeo. | AUDIO | No | Hasta 10 (Seedance 2.5)<br>Hasta 3 (modelos Seedance 2.0) |
| `auto_downscale` | Reduce automáticamente la escala de los vídeos de referencia que superen el límite de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los vídeos que ya están dentro de los límites no se modifican (por defecto: True). | BOOLEAN | No | `True`<br>`False` |
| `auto_upscale` | Aumenta automáticamente la escala de los vídeos de referencia que estén por debajo del número mínimo de píxeles del modelo para la resolución seleccionada. Se conserva la relación de aspecto; los vídeos que ya cumplen el mínimo no se modifican. Nota: aumentar la escala de una fuente de baja resolución no añade detalle real y puede generar vídeos de menor calidad (por defecto: False). | BOOLEAN | No | `True`<br>`False` |
| `reference_assets` | Ranura ampliable: IDs de activos creados previamente en la biblioteca virtual de Seedance (Image, Video o Audio) para usarlos como referencias (`asset_1`, `asset_2`, ...). Cada activo debe existir y tener estado Active. En la indicación, los activos pueden mencionarse como `asset1`, `asset 1`, etc.; el nodo reemplaza estos tokens por etiquetas como «Image 2». | STRING | No | Hasta 30 (Seedance 2.5)<br>Hasta 9 (modelos Seedance 2.0) |

**Restricciones importantes:**

* Se requiere al menos una referencia. Para Seedance 2.0, 2.0 Fast y 2.0 Mini, debe proporcionar al menos una referencia de imagen o vídeo (mediante `reference_images`, `reference_videos`, o una entrada de imagen o vídeo en `reference_assets`). Seedance 2.5 además acepta referencias solo de audio (mediante `reference_audios` o una entrada de audio en `reference_assets`).
* El número de referencias depende del modelo y se valida combinando las entradas directas y las referencias de activos: Seedance 2.5 permite hasta 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` y 30 `reference_assets`; los modelos Seedance 2.0 permiten hasta 9 imágenes, 3 vídeos, 3 clips de audio y 9 activos.
* Cada vídeo de referencia debe durar al menos 1.8 segundos, y cada clip de audio de referencia debe durar al menos 1.8 segundos. La duración total de todos los vídeos de referencia y de todos los audios de referencia debe permanecer dentro del límite del modelo seleccionado (15.1 segundos para los modelos Seedance 2.0).
* Los vídeos de referencia también deben cumplir los límites de número de píxeles del modelo para la resolución seleccionada. Con `auto_downscale` activado (por defecto), los vídeos demasiado grandes se redimensionan automáticamente; con `auto_upscale` activado, los vídeos demasiado pequeños se amplían. Si cualquiera de los ajustes automáticos está desactivado, los vídeos fuera del límite correspondiente generan un error.
* Cuando `video_editing` está activado en Seedance 2.5, las entradas `duration` y `ratio` se ignoran; la salida coincide con la duración y la relación de aspecto propias del vídeo de referencia. Si el proveedor interpreta la indicación como una edición de un vídeo de referencia, la generación falla a menos que `video_editing` esté activado o que la indicación se reformule para describir un vídeo nuevo.
* Si el proveedor rechaza la pista de audio generada para el vídeo (por ejemplo, por una posible coincidencia de derechos de autor), la tarea falla; desactivar `generate_audio` produce un vídeo sin audio.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de vídeo generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/es.md)

---
**Source fingerprint (SHA-256):** `4a1b62f65ff3515cdb749c9b3916e631e53523fe144e8cdf71ca020825196ae6`
