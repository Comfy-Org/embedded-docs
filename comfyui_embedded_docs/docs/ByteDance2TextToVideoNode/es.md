# ByteDance Seedance 2.0 Texto a Video

Este nodo genera un video a partir de una indicación de texto utilizando los modelos Seedance 2.5 o 2.0 de ByteDance. Envía la indicación al modelo seleccionado, espera a que el video termine de procesarse y devuelve el archivo de video resultante.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo Seedance que se utilizará para la generación de video. Seedance 2.5 es el modelo más reciente, compatible con videos de hasta 30 segundos y salida mp4/mov; Seedance 2.0 es para máxima calidad y 4k; Seedance 2.0 Fast es para optimizar la velocidad; Seedance 2.0 Mini es para la generación más rápida y de menor costo. Al seleccionar un modelo, se muestran entradas adicionales para la indicación, la resolución, la relación de aspecto, la duración y la generación de audio. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `semilla` | Controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | No | 0 a 2147483647 |
| `marca_de_agua` | Si se debe añadir una marca de agua al video. (predeterminado: False) Esta es una configuración avanzada. | BOOLEAN | No | True / False |

### Entradas de Seedance 2.5

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación de video. Ponga las líneas habladas entre comillas dobles para guiar el diálogo generado. | STRING | Sí | — |
| `resolution` | Resolución del video de salida. (predeterminado: `"720p"`) | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio` | Relación de aspecto del video de salida. (predeterminado: `"16:9"`) | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos. (predeterminado: 5) | INT | Sí | 4 a 30 |
| `generate_audio` | Habilita la generación de audio para el video de salida. (predeterminado: True) | BOOLEAN | Sí | True / False |
| `output_format` | Formato de contenedor del video de salida. (predeterminado: `"mp4"`) | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.0

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación de video. | STRING | Sí | — |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida. (predeterminado: `"16:9"`) | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos. (predeterminado: 7) | INT | Sí | 4 a 15 |
| `generate_audio` | Habilita la generación de audio para el video de salida. (predeterminado: True) | BOOLEAN | Sí | True / False |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Compartidas por Seedance 2.0 Fast y Seedance 2.0 Mini; ambos modelos exponen los mismos parámetros.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación de video. | STRING | Sí | — |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida. (predeterminado: `"16:9"`) | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos. (predeterminado: 7) | INT | Sí | 4 a 15 |
| `generate_audio` | Habilita la generación de audio para el video de salida. (predeterminado: True) | BOOLEAN | Sí | True / False |

**Nota:** El selector `model` es dinámico; las entradas que se muestran en cada sección de modelo aparecen cuando se selecciona ese modelo. La indicación debe tener al menos 1 carácter después de eliminar los espacios en blanco. Los límites de resolución y duración dependen del modelo seleccionado: Seedance 2.5 admite 480p/720p/1080p y de 4 a 30 segundos; Seedance 2.0 admite 480p/720p/1080p/4k y de 4 a 15 segundos; y Seedance 2.0 Fast y Seedance 2.0 Mini admiten solo 480p/720p y de 4 a 15 segundos. El valor de `seed` solo controla si el nodo se vuelve a ejecutar; no hace que los resultados sean deterministas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `e3b11f5a538d4b9b7e49f651d3939651edfe85000e02e66a8d7700c3389c4b9c`
