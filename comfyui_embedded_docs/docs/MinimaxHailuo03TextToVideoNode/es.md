# MiniMax H3 Texto a Video

Este nodo genera un video a partir de un prompt de texto utilizando el modelo MiniMax H3. Envía el texto junto con ajustes de video como resolución, relación de aspecto y duración a la API de MiniMax, espera a que la tarea de generación se complete y devuelve el video resultante.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la generación de video. (predeterminado: "MiniMax H3"). Al seleccionar este modelo, también se proporcionan el prompt de texto, la resolución, la relación de aspecto y la duración del video generado (consulte Entradas de MiniMax H3 más abajo). | COMBO | Sí | `"MiniMax H3"` |
| `semilla` | Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos. (predeterminado: 42) | INT | Sí | 0 a 4294967295 |
| `marca de agua` | Indica si se debe añadir una marca de agua AIGC al video. (predeterminado: false) | BOOLEAN | No | true<br>false |

### Entradas de MiniMax H3

Estos ajustes aparecen cuando se selecciona el modelo "MiniMax H3".

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto para la generación del video. | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | "768P"<br>"2K" |
| `ratio` | Relación de aspecto del video de salida. (predeterminado: "16:9") | COMBO | Sí | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Duración del video de salida en segundos. (predeterminado: 5) | INT | Sí | 4 a 15 |

Nota: El prompt de texto incluido en la opción `model` debe contener al menos un carácter que no sea un espacio en blanco. El precio estimado que se muestra para este nodo se calcula a partir de la resolución seleccionada y la duración del video.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El video generado a partir del prompt de texto proporcionado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `93f7c81ba4053da999d29392bce23f7fd809d21876ea489747d203201ed0377f`
