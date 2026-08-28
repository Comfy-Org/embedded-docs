# ByteDance Seedance 2.0 Primer-Último Fotograma a Video

Este nodo genera un video a partir de una imagen de primer fotograma obligatoria y una imagen de último fotograma opcional mediante los modelos Seedance de ByteDance. Describes el video con un prompt de texto; el primer fotograma guía el inicio del video y el último fotograma guía el final. Es compatible con Seedance 2.5 y la familia Seedance 2.0 (Seedance 2.0, Seedance 2.0 Fast y Seedance 2.0 Mini).

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo` | Seedance 2.5 para el modelo más reciente, videos de hasta 30 segundos y salida mp4/mov; Seedance 2.0 para máxima calidad y 4k; Fast para optimización de velocidad; Mini para la generación más rápida y de menor costo. Al seleccionar un modelo se muestran entradas específicas del modelo a continuación. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `primer_fotograma` | Imagen del primer fotograma para el video. | IMAGE | No | - |
| `último_fotograma` | Imagen del último fotograma para el video. | IMAGE | No | - |
| `first_frame_asset_id` | asset_id de Seedance que se usará como primer fotograma. Es mutuamente excluyente con la entrada de imagen `first_frame`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `last_frame_asset_id` | asset_id de Seedance que se usará como último fotograma. Es mutuamente excluyente con la entrada de imagen `last_frame`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. El valor predeterminado es 0. | INT | Sí | 0 a 2147483647 |
| `marca_de_agua` | Indica si se debe añadir una marca de agua al video. El valor predeterminado es False. | BOOLEAN | Sí | False<br>True |

### Entradas de Seedance 2.5

Estas entradas aparecen cuando se selecciona `Seedance 2.5`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para la generación del video. Ponga las líneas habladas entre comillas dobles para guiar el diálogo generado. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. El valor predeterminado es 720p. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `duration` | Duración del video de salida en segundos (4-30). El valor predeterminado es 5. | INT | Sí | 4 a 30 |
| `generate_audio` | Habilita la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | False<br>True |
| `output_format` | Formato de contenedor del video de salida. El valor predeterminado es mp4. | COMBO | Sí | `"mp4"` |

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

Compartidas por `Seedance 2.0 Fast` y `Seedance 2.0 Mini`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para la generación del video. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida. El valor predeterminado es `adaptive`, que usa la relación compatible más cercana a la relación de aspecto del fotograma de entrada. | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (4-15). El valor predeterminado es 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Habilita la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | False<br>True |

**Restricciones de parámetros**

- Debe proporcionar el primer fotograma como una imagen `first_frame` o como un `first_frame_asset_id`. Proporcionar ambos genera un error; no proporcionar ninguno también genera un error.
- Las entradas `last_frame` y `last_frame_asset_id` son opcionales, pero no puede proporcionar ambas para el mismo fotograma.
- Los Asset IDs deben hacer referencia a activos de imagen Seedance existentes y activos.
- La entrada `prompt` es obligatoria y no puede estar vacía.
- Con `Seedance 2.5`, la relación de aspecto de salida es siempre adaptativa y sigue la relación de aspecto del propio primer fotograma, por lo que no se muestra ninguna entrada `ratio`.
- Con los modelos de la familia Seedance 2.0 y las imágenes de fotogramas locales, las imágenes se recortan desde el centro y se redimensionan a la resolución y relación de aspecto de salida objetivo antes de la generación. Cuando `ratio` es `adaptive`, se usa la relación compatible más cercana a la imagen de entrada.
- Las imágenes de fotogramas locales se validan en cuanto a la relación de aspecto y las dimensiones compatibles; las imágenes sobredimensionadas se reducen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `bc2eb5f43c935986ad870703cfbc92dd99a53d6f0ac91cf0cad46bee33ff2cc0`
