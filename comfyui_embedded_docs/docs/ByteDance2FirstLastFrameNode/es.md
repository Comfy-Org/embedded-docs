# ByteDance Seedance 2.0 Primer-Último Fotograma a Video

Este nodo genera un video a partir de una primera imagen de fotograma obligatoria y una imagen de último fotograma opcional, utilizando los modelos Seedance 2.5 o Seedance 2.0 de ByteDance. El primer fotograma define el inicio del clip, el último fotograma (cuando se proporciona) define el final, y un mensaje de texto describe el movimiento. El modelo seleccionado controla las resoluciones, duraciones y opciones de formato de salida disponibles.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo utilizado para la generación de video. Seedance 2.5 es el modelo más reciente, con videos de hasta 30 segundos y salida en mp4/mov; Seedance 2.0 ofrece la máxima calidad y 1080p/4k; Fast está optimizado para velocidad; Mini es la generación más rápida y de menor costo. Seleccionar un modelo revela sus entradas específicas a continuación. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `first_frame` | Imagen del primer fotograma del video. Se requiere una de `first_frame` o `first_frame_asset_id`. | IMAGE | No | - |
| `last_frame` | Imagen del último fotograma del video. | IMAGE | No | - |
| `first_frame_asset_id` | asset_id de Seedance que se utilizará como primer fotograma. Se excluye mutuamente con la entrada de imagen `first_frame`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `last_frame_asset_id` | asset_id de Seedance que se utilizará como último fotograma. Se excluye mutuamente con la entrada de imagen `last_frame`. El valor predeterminado es una cadena vacía. | STRING | No | - |
| `seed` | La semilla (seed) controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. El valor predeterminado es 0. | INT | No | 0 a 2147483647 |
| `watermark` | Si se debe agregar una marca de agua al video. El valor predeterminado es False. | BOOLEAN | No | - |

### Entradas de Seedance 2.5

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Mensaje de texto para la generación de video. Coloca las líneas habladas entre comillas dobles para orientar el diálogo generado. El valor predeterminado es una cadena vacía. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. El valor predeterminado es "720p". | COMBO | Sí | `"480p"`<br>`"720p"` |
| `duration` | Duración del video de salida en segundos (4-30). El valor predeterminado es 5. | INT | Sí | 4 a 30 |
| `generate_audio` | Activar la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | - |
| `output_format` | Formato de contenedor del video de salida. El valor predeterminado es "mp4". | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.0

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Mensaje de texto para la generación de video. El valor predeterminado es una cadena vacía. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida. El valor predeterminado es "adaptive". | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (4-15). El valor predeterminado es 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Activar la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | - |

### Compartidas por Seedance 2.0 Fast y Seedance 2.0 Mini

Estos dos modelos exponen las mismas entradas que Seedance 2.0, excepto que solo están disponibles las resoluciones 480p y 720p.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Mensaje de texto para la generación de video. El valor predeterminado es una cadena vacía. | STRING | Sí | - |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida. El valor predeterminado es "adaptive". | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (4-15). El valor predeterminado es 7. | INT | Sí | 4 a 15 |
| `generate_audio` | Activar la generación de audio para el video de salida. El valor predeterminado es True. | BOOLEAN | Sí | - |

**Restricciones y limitaciones:**

*   El `prompt` es obligatorio y debe contener al menos un carácter que no sea espacio en blanco (se ignoran los espacios en blanco al inicio y al final).
*   Debe proporcionarse exactamente una fuente de primer fotograma: ya sea la imagen `first_frame` o el `first_frame_asset_id`. Proporcionar ambos genera un error, y no proporcionar ninguno también genera un error.
*   La imagen `last_frame` y el `last_frame_asset_id` son mutuamente excluyentes. Ambos pueden omitirse.
*   Los ID de activos deben hacer referencia a activos Seedance existentes con estado Activo. Si un activo no está activo o no es un activo de imagen, se genera un error.
*   Las imágenes locales deben tener una relación de aspecto entre 0.4 y 2.5 (2:5 a 5:2).
*   Para los modelos Seedance 2.0, las imágenes locales deben tener al menos 300x300 píxeles. Se redimensionan automáticamente a las dimensiones de salida admitidas exactas para la resolución y relación de aspecto seleccionadas, y la solicitud se envía con la relación de aspecto "adaptive". Cuando `ratio` es "adaptive", la relación de aspecto de salida se deriva de la relación de aspecto del primer fotograma, ajustándose a la relación admitida más cercana. Cuando se utilizan ID de activos en lugar de imágenes locales, el valor de `ratio` seleccionado se aplica directamente.
*   Para Seedance 2.5, y para cualquier modelo cuando se utilizan ID de activos, las imágenes se reducen automáticamente a un lado máximo de 6000 píxeles y deben tener entre 300 y 6000 píxeles en cada dimensión.
*   Seedance 2.5 siempre mantiene la relación de aspecto del primer fotograma, por lo que no se muestra ninguna entrada `ratio` para este modelo.
*   Los límites de duración difieren según el modelo: Seedance 2.5 admite de 4 a 30 segundos, mientras que Seedance 2.0, 2.0 Fast y 2.0 Mini admiten de 4 a 15 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `d87265eb75d67f7d80f76474fc699f7ca87b6edbddda36733d5e440708b074a2`
