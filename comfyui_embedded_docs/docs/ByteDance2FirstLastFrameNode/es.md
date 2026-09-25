# ByteDance Seedance 2.0 Primer-Último Fotograma a Video

Este nodo genera un video a partir de una imagen de primer fotograma obligatoria y una imagen de último fotograma opcional usando modelos ByteDance Seedance. Describes el video con un prompt de texto; el primer fotograma guía el inicio del video y el último fotograma guía el final. Es compatible con Seedance 2.5 y la familia Seedance 2.0 (Seedance 2.0, Seedance 2.0 Fast y Seedance 2.0 Mini). Seleccionar el modelo `Seedance 2.5 Draft` genera una vista previa rápida en 480p; conecta el `draft_task_id` resultante al nodo ByteDance Seedance 2.5 Draft to Final Video para renderizar el final en 1080p.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo` | Seedance 2.5 para el modelo más reciente, videos de hasta 30 segundos y salida mp4/mov; Seedance 2.5 Draft para una vista previa rápida en 480p cuya salida `draft_task_id` renderiza el final en 1080p en el nodo ByteDance Seedance 2.5 Draft to Final Video; Seedance 2.0 para máxima calidad y 4k; Fast para optimización de la velocidad; Mini para la generación más rápida y de menor costo. Al seleccionar un modelo se muestran las entradas específicas del modelo a continuación. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.5 Draft"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `primer_fotograma` | Imagen del primer fotograma para el video. | IMAGE | No | - |
| `último_fotograma` | Imagen del último fotograma para el video. | IMAGE | No | - |
| `first_frame_asset_id` | asset_id de Seedance que se usará como primer fotograma. Mutuamente excluyente con la entrada de imagen `first_frame`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `last_frame_asset_id` | asset_id de Seedance que se usará como último fotograma. Mutuamente excluyente con la entrada de imagen `last_frame`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. El valor predeterminado es 0. | INT | Sí | 0 a 2147483647 |
| `marca_de_agua` | Indica si se debe agregar una marca de agua al video. El valor predeterminado es False. | BOOLEAN | Sí | False<br>True |

### Entradas de Seedance 2.5

Estas entradas aparecen cuando se selecciona `Seedance 2.5`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para la generación del video. Coloca las líneas habladas entre comillas dobles para dirigir el diálogo generado. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. El valor predeterminado es 720p. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Duración del video de salida en segundos (4-30). El valor predeterminado es 5. | INT | Sí | 4 a 30 |
| `generate_audio` | Habilita la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | False<br>True |
| `output_format` | Formato de contenedor del video de salida. El valor predeterminado es mp4. | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.5 Draft

Estas entradas aparecen cuando se selecciona `Seedance 2.5 Draft`. El conjunto de parámetros coincide con Seedance 2.5 anterior, excepto que `resolution` ofrece solo `"480p"` (valor predeterminado `"480p"`).

### Entradas de Seedance 2.0

Estas entradas aparecen cuando se selecciona `Seedance 2.0`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para la generación del video. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida. El valor predeterminado es `adaptive`, que usa la relación compatible más cercana a la relación de aspecto del fotograma de entrada. | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (4-15). El valor predeterminado es 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Habilita la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | False<br>True |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Estas entradas son compartidas por `Seedance 2.0 Fast` y `Seedance 2.0 Mini`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para la generación del video. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida. El valor predeterminado es `adaptive`, que usa la relación compatible más cercana a la relación de aspecto del fotograma de entrada. | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (4-15). El valor predeterminado es 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Habilita la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | False<br>True |

**Restricciones de parámetros**

- Debes proporcionar el primer fotograma ya sea como una imagen `first_frame` o como un `first_frame_asset_id`. Proporcionar ambos genera un error; no proporcionar ninguno también genera un error.
- Las entradas `last_frame` y `last_frame_asset_id` son opcionales, pero no puedes proporcionar ambas para el mismo fotograma.
- Los asset IDs deben hacer referencia a assets de imagen de Seedance existentes y activos.
- La entrada `prompt` es obligatoria y no puede estar vacía.
- La salida `draft_task_id` solo la produce `Seedance 2.5 Draft`; con cualquier otro modelo debe dejarse desconectada, de lo contrario la ejecución falla.
- Con `Seedance 2.5`, la relación de aspecto de salida siempre es adaptativa y sigue la relación de aspecto del primer fotograma, por lo que no se muestra la entrada `ratio`.
- Con los modelos de la familia Seedance 2.0 y las imágenes de fotogramas locales, las imágenes se recortan desde el centro y se redimensionan a la resolución y relación de aspecto de salida objetivo antes de la generación. Cuando `ratio` es `adaptive`, se usa la relación compatible más cercana a la imagen de entrada.
- Las imágenes de fotogramas locales se validan en cuanto a relación de aspecto y dimensiones compatibles; las imágenes de tamaño excesivo se reducen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado. | VIDEO |
| `draft_task_id` | ID de tarea de la ejecución de borrador. Solo lo produce el modelo Seedance 2.5 Draft; conéctalo al nodo ByteDance Seedance 2.5 Draft to Final Video para renderizar el final en 1080p. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `363f1baac1685c2dada0e64a0b339f6ab2671161dccb002eb81f6b4f0d0aa243`
