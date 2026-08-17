# ByteDance Seedance 2.0 Texto a Video

Este nodo genera un video a partir de una descripción de texto utilizando los modelos Seedance 2.5 o 2.0 de ByteDance. Envía tu indicación al modelo seleccionado, espera a que se procese el video y devuelve el resultado final.

## Entradas

El parámetro `model` es un combo dinámico. Cuando seleccionas un modelo, se muestran varias entradas específicas del modelo que deben completarse, incluidos la indicación de texto, la resolución, la relación de aspecto, la duración y la configuración de generación de audio.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo a utilizar para la generación de video. Seedance 2.5 es el modelo más reciente, genera videos de hasta 30 segundos con salida mp4/mov; Seedance 2.0 ofrece la máxima calidad con 1080p/4k; Fast es para optimización de velocidad; Mini es la generación más rápida y de menor costo. | DYNAMIC_COMBO | Sí | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla (por defecto: 0). | INT | No | 0 a 2147483647 |
| `watermark` | Si se debe añadir una marca de agua al video (por defecto: False). Esta es una configuración avanzada. | BOOLEAN | No | True / False |

### Entradas de Seedance 2.5

Estas entradas aparecen cuando `model` está configurado como `Seedance 2.5`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación de video. Ponga las frases habladas entre comillas dobles para dirigir el diálogo generado (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida (por defecto: "720p"). | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida (por defecto: "16:9"). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (por defecto: 5). | INT | Sí | 4 a 30 |
| `generate_audio` | Habilitar la generación de audio para el video de salida (por defecto: True). | BOOLEAN | No | True / False |
| `output_format` | Formato de contenedor del video de salida (por defecto: "mp4"). | COMBO | Sí | `"mp4"` |

### Entradas de Seedance 2.0

Estas entradas aparecen cuando `model` está configurado como `Seedance 2.0`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación de video (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Relación de aspecto del video de salida (por defecto: "16:9"). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (por defecto: 7). | INT | Sí | 4 a 15 |
| `generate_audio` | Habilitar la generación de audio para el video de salida (por defecto: True). | BOOLEAN | No | True / False |

### Entradas de Seedance 2.0 Fast y Seedance 2.0 Mini

Estas entradas aparecen cuando `model` está configurado como `Seedance 2.0 Fast` o `Seedance 2.0 Mini`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para la generación de video (por defecto: vacío). | STRING | Sí | Cualquier texto |
| `resolution` | Resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `ratio` | Relación de aspecto del video de salida (por defecto: "16:9"). | COMBO | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Duración del video de salida en segundos (por defecto: 7). | INT | Sí | 4 a 15 |
| `generate_audio` | Habilitar la generación de audio para el video de salida (por defecto: True). | BOOLEAN | No | True / False |

**Nota:** El `prompt` debe contener al menos 1 carácter después de eliminar los espacios en blanco; de lo contrario, la tarea no supera la validación. Los límites de duración dependen del modelo: Seedance 2.5 admite de 4 a 30 segundos, mientras que Seedance 2.0, Seedance 2.0 Fast y Seedance 2.0 Mini admiten de 4 a 15 segundos. Las opciones de resolución también varían según el modelo: Seedance 2.5 admite 480p y 720p; Seedance 2.0 admite 480p, 720p, 1080p y 4k; Seedance 2.0 Fast y Seedance 2.0 Mini solo admiten 480p y 720p.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `66d200f4ddf674b897def63604b0f29dcbf655e00b4e9b9c11e31b671ead94bc`
