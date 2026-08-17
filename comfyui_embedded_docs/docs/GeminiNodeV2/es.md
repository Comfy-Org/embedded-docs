# Google Gemini

Genere respuestas de texto con los modelos Gemini de Google. Proporcione un mensaje de texto y, opcionalmente, una o más imágenes, clips de audio, vídeos o archivos como contexto multimodal.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo Gemini utilizado para generar la respuesta. | DYNAMIC_COMBO | Sí | `"Gemini 3.5 Flash"`<br>`"Gemini 3.1 Pro"`<br>`"Gemini 3.1 Flash-Lite"` |
| `prompt` | Entrada de texto para el modelo. Incluye instrucciones detalladas, preguntas o contexto. Debe contener al menos un carácter que no sea un espacio en blanco. (predeterminado: "") | STRING | Sí |  |
| `seed` | Semilla para el muestreo. Establézcala en 0 para una semilla aleatoria. No se garantiza una salida determinista. (predeterminado: 42) | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (predeterminado: "") | STRING | No |  |

### Entradas de Gemini 3.5 Flash

Estas entradas aparecen cuando `model` está configurado en `"Gemini 3.5 Flash"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Cuánto razona internamente el modelo antes de responder. HIGH mejora la calidad en tareas difíciles, pero consume más tokens de (razonamiento) y es más lento. (predeterminado: "MEDIUM") | COMBO | Sí | `"MINIMAL"`<br>`"LOW"`<br>`"MEDIUM"`<br>`"HIGH"` |
| `temperature` | Controla la aleatoriedad. Un valor más bajo es más enfocado/determinista, un valor más alto es más creativo. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 2.0 |
| `top_p` | Muestreo de núcleo: muestrear del conjunto de tokens más pequeño cuya probabilidad acumulada alcanza top_p. (predeterminado: 0.95) | FLOAT | Sí | 0.0 a 1.0 |
| `max_output_tokens` | Cantidad máxima de tokens a generar, incluyendo el razonamiento interno del modelo. Con thinking_level HIGH, un valor bajo puede dejar sin espacio para la respuesta; aumente este valor si las respuestas llegan vacías o truncadas. El modelo se detiene antes cuando termina, por lo que un límite más alto no cuesta nada extra para respuestas cortas. (predeterminado: 32768) | INT | Sí | 16 a 65536 |

### Entradas de Gemini 3.1 Pro

Estas entradas aparecen cuando `model` está configurado en `"Gemini 3.1 Pro"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Cuánto razona internamente el modelo antes de responder. HIGH mejora la calidad en tareas difíciles, pero consume más tokens de (razonamiento) y es más lento. (predeterminado: "HIGH") | COMBO | Sí | `"LOW"`<br>`"HIGH"` |
| `temperature` | Controla la aleatoriedad. Un valor más bajo es más enfocado/determinista, un valor más alto es más creativo. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 2.0 |
| `top_p` | Muestreo de núcleo: muestrear del conjunto de tokens más pequeño cuya probabilidad acumulada alcanza top_p. (predeterminado: 0.95) | FLOAT | Sí | 0.0 a 1.0 |
| `max_output_tokens` | Cantidad máxima de tokens a generar, incluyendo el razonamiento interno del modelo. Con thinking_level HIGH, un valor bajo puede dejar sin espacio para la respuesta; aumente este valor si las respuestas llegan vacías o truncadas. El modelo se detiene antes cuando termina, por lo que un límite más alto no cuesta nada extra para respuestas cortas. (predeterminado: 32768) | INT | Sí | 16 a 65536 |

### Entradas de Gemini 3.1 Flash-Lite

Estas entradas aparecen cuando `model` está configurado en `"Gemini 3.1 Flash-Lite"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `thinking_level` | Cuánto razona internamente el modelo antes de responder. HIGH mejora la calidad en tareas difíciles, pero consume más tokens de (razonamiento) y es más lento. (predeterminado: "LOW") | COMBO | Sí | `"LOW"`<br>`"HIGH"` |
| `temperature` | Controla la aleatoriedad. Un valor más bajo es más enfocado/determinista, un valor más alto es más creativo. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 2.0 |
| `top_p` | Muestreo de núcleo: muestrear del conjunto de tokens más pequeño cuya probabilidad acumulada alcanza top_p. (predeterminado: 0.95) | FLOAT | Sí | 0.0 a 1.0 |
| `max_output_tokens` | Cantidad máxima de tokens a generar, incluyendo el razonamiento interno del modelo. Con thinking_level HIGH, un valor bajo puede dejar sin espacio para la respuesta; aumente este valor si las respuestas llegan vacías o truncadas. El modelo se detiene antes cuando termina, por lo que un límite más alto no cuesta nada extra para respuestas cortas. (predeterminado: 32768) | INT | Sí | 16 a 65536 |

### Entradas de medios y archivos

Las siguientes entradas son compartidas por los tres modelos y aparecen junto a las entradas específicas del modelo.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `images` | Ranura ampliable: conecte de 1 a 16 imágenes (`image_1` ... `image_16`). Imagen(es) opcional(es) para usar como contexto para el modelo. | IMAGE | No | 0 a 16 imágenes |
| `audio` | Ranura ampliable: conecte un clip de audio (`audio_1`). Clip de audio opcional para usar como contexto para el modelo. | AUDIO | No | 0 a 1 clip |
| `video` | Ranura ampliable: conecte un clip de video (`video_1`). Clip de video opcional para usar como contexto para el modelo. | VIDEO | No | 0 a 1 clip |
| `files` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Input Files. | GEMINI_INPUT_FILES | No |  |

**Nota:** Cuando se adjuntan medios (imágenes, audio o video), el nodo sube los primeros 10 elementos de medios al almacenamiento de ComfyAPI y los pasa como URL; este presupuesto de URL se comparte entre todos los tipos de medios y se consume en orden (primero video, luego audio, luego imágenes). Los medios restantes se codifican en línea como datos base64, con una carga útil combinada máxima de 18 MB. Si la carga útil en línea supera los 18 MB, el nodo genera un error. El parámetro `prompt` debe contener al menos un carácter que no sea un espacio en blanco. Establecer `seed` en 0 solicita una semilla aleatoria.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La respuesta de texto generada por el modelo Gemini. Si el modelo no produce texto, se devuelve la cadena "Empty response from Gemini model...". | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `e88c253d9ae987ab91b0fb6b0b55cfd9cd3671438770afcedd844f236b30dc36`
