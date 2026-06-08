El nodo `TextEncodeAceStepAudio1.5` prepara metadatos de texto y audio para su uso con el modelo AceStepAudio 1.5. Toma etiquetas descriptivas, letras y parámetros musicales, y luego utiliza un modelo CLIP para convertirlos en un formato de condicionamiento adecuado para la generación de audio.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para tokenizar y codificar el texto de entrada. | CLIP | Sí | N/A |
| `tags` | Etiquetas descriptivas para el audio, como género, estado de ánimo o instrumentos. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | N/A |
| `lyrics` | La letra de la pista de audio. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | N/A |
| `seed` | Un valor de semilla aleatoria para una generación reproducible. Tiene un widget control_after_generate. Valor predeterminado: 0. | INT | No | 0 a 18446744073709551615 |
| `bpm` | Los pulsos por minuto (BPM) para el audio generado. Valor predeterminado: 120. | INT | No | 10 a 300 |
| `duration` | La duración deseada del audio en segundos. Valor predeterminado: 120.0. | FLOAT | No | 0.0 a 2000.0 |
| `timesignature` | El compás musical. | COMBO | No | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` |
| `language` | El idioma del texto de entrada. Valor predeterminado: "en". | COMBO | No | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` |
| `keyscale` | La tonalidad y escala musical (mayor o menor). | COMBO | No | `"C major"`<br>`"C minor"`<br>`"C# major"`<br>`"C# minor"`<br>`"Db major"`<br>`"Db minor"`<br>`"D major"`<br>`"D minor"`<br>`"D# major"`<br>`"D# minor"`<br>`"Eb major"`<br>`"Eb minor"`<br>`"E major"`<br>`"E minor"`<br>`"F major"`<br>`"F minor"`<br>`"F# major"`<br>`"F# minor"`<br>`"Gb major"`<br>`"Gb minor"`<br>`"G major"`<br>`"G minor"`<br>`"G# major"`<br>`"G# minor"`<br>`"Ab major"`<br>`"Ab minor"`<br>`"A major"`<br>`"A minor"`<br>`"A# major"`<br>`"A# minor"`<br>`"Bb major"`<br>`"Bb minor"`<br>`"B major"`<br>`"B minor"` |
| `generate_audio_codes` | Habilita el LLM que genera códigos de audio. Esto puede ser lento pero aumentará la calidad del audio generado. Desactívalo si le estás dando al modelo una referencia de audio. Valor predeterminado: True. | BOOLEAN | No | N/A |
| `cfg_scale` | La escala de guía libre de clasificador. Valores más altos hacen que la salida siga más fielmente el prompt. Valor predeterminado: 2.0. | FLOAT | No | 0.0 a 100.0 |
| `temperature` | Una temperatura de muestreo. Valores más bajos hacen que la salida sea más determinista. Valor predeterminado: 0.85. | FLOAT | No | 0.0 a 2.0 |
| `top_p` | La probabilidad de muestreo de núcleo (top-p). Valor predeterminado: 0.9. | FLOAT | No | 0.0 a 2000.0 |
| `top_k` | El número de tokens con mayor probabilidad a considerar (top-k). Valor predeterminado: 0. | INT | No | 0 a 100 |
| `min_p` | El umbral de probabilidad mínima para el muestreo de tokens (min-p). Valor predeterminado: 0.000. | FLOAT | No | 0.0 a 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | Los datos de condicionamiento, que contienen el texto codificado y los parámetros de audio para el modelo AceStepAudio 1.5. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/es.md)

---
**Source fingerprint (SHA-256):** `df70a55024812d8c77a3b618cbff6d3148a3f3f5fc4d17dd3c4282ce7f3cbc2c`
