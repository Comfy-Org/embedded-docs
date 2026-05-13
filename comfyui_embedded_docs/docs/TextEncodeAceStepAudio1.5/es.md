> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/es.md)

El nodo `TextEncodeAceStepAudio1.5` prepara metadatos de texto y audio para su uso con el modelo AceStepAudio 1.5. Toma etiquetas descriptivas, letras y parámetros musicales, y luego utiliza un modelo CLIP para convertirlos en un formato de condicionamiento adecuado para la generación de audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|---------------|-----------|-------|-------------|
| `clip` | CLIP | Sí | N/A | El modelo CLIP utilizado para tokenizar y codificar el texto de entrada. |
| `tags` | STRING | Sí | N/A | Etiquetas descriptivas para el audio, como género, estado de ánimo o instrumentos. Admite entrada multilínea y prompts dinámicos. |
| `lyrics` | STRING | Sí | N/A | La letra de la pista de audio. Admite entrada multilínea y prompts dinámicos. |
| `seed` | INT | No | 0 a 18446744073709551615 | Un valor de semilla aleatoria para una generación reproducible. Tiene un widget control_after_generate. Valor predeterminado: 0. |
| `bpm` | INT | No | 10 a 300 | Los pulsos por minuto (BPM) para el audio generado. Valor predeterminado: 120. |
| `duration` | FLOAT | No | 0.0 a 2000.0 | La duración deseada del audio en segundos. Valor predeterminado: 120.0. |
| `timesignature` | COMBO | No | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` | El compás musical. |
| `language` | COMBO | No | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` | El idioma del texto de entrada. Valor predeterminado: "en". |
| `keyscale` | COMBO | No | `"C major"`<br>`"C minor"`<br>`"C# major"`<br>`"C# minor"`<br>`"Db major"`<br>`"Db minor"`<br>`"D major"`<br>`"D minor"`<br>`"D# major"`<br>`"D# minor"`<br>`"Eb major"`<br>`"Eb minor"`<br>`"E major"`<br>`"E minor"`<br>`"F major"`<br>`"F minor"`<br>`"F# major"`<br>`"F# minor"`<br>`"Gb major"`<br>`"Gb minor"`<br>`"G major"`<br>`"G minor"`<br>`"G# major"`<br>`"G# minor"`<br>`"Ab major"`<br>`"Ab minor"`<br>`"A major"`<br>`"A minor"`<br>`"A# major"`<br>`"A# minor"`<br>`"Bb major"`<br>`"Bb minor"`<br>`"B major"`<br>`"B minor"` | La tonalidad y escala musical (mayor o menor). |
| `generate_audio_codes` | BOOLEAN | No | N/A | Habilita el LLM que genera códigos de audio. Esto puede ser lento pero aumentará la calidad del audio generado. Desactívalo si le estás dando al modelo una referencia de audio. Valor predeterminado: True. |
| `cfg_scale` | FLOAT | No | 0.0 a 100.0 | La escala de guía libre de clasificador. Valores más altos hacen que la salida siga más fielmente el prompt. Valor predeterminado: 2.0. |
| `temperature` | FLOAT | No | 0.0 a 2.0 | Una temperatura de muestreo. Valores más bajos hacen que la salida sea más determinista. Valor predeterminado: 0.85. |
| `top_p` | FLOAT | No | 0.0 a 2000.0 | La probabilidad de muestreo de núcleo (top-p). Valor predeterminado: 0.9. |
| `top_k` | INT | No | 0 a 100 | El número de tokens con mayor probabilidad a considerar (top-k). Valor predeterminado: 0. |
| `min_p` | FLOAT | No | 0.0 a 1.0 | El umbral de probabilidad mínima para el muestreo de tokens (min-p). Valor predeterminado: 0.000. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento, que contienen el texto codificado y los parámetros de audio para el modelo AceStepAudio 1.5. |

---
**Source fingerprint (SHA-256):** `df70a55024812d8c77a3b618cbff6d3148a3f3f5fc4d17dd3c4282ce7f3cbc2c`
