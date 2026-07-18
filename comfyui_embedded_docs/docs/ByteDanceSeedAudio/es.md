# ByteDance Seed Audio 1.0

Genera voz, música, efectos de sonido y diálogos multi-locutor a partir de una sola indicación con ByteDance Seed Audio 1.0. Describe la(s) voz(es), emoción, ambiente, música de fondo y efectos de sonido en la indicación, e incluye las líneas a hablar. Opcionalmente, elige una voz predefinida incorporada, clona voces de hasta 3 clips de referencia (etiquetados @Audio1-3 en la indicación), o deriva una voz a partir de una imagen de personaje. Hasta 2 minutos de audio por ejecución.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `text_prompt` | Describe la(s) voz(es), emoción, ritmo, ambiente, música de fondo y efectos de sonido, e incluye las líneas a hablar (nombra a los personajes en línea para el diálogo). En el modo 'referencia de audio', refiérete a los clips conectados por orden como @Audio1, @Audio2, @Audio3. Máximo 3000 caracteres. | STRING | Sí | 1 a 3000 caracteres |
| `reference_mode` | Cómo condicionar la voz: 'solo texto' (describe todo en la indicación), 'referencia de audio' (clona hasta 3 voces, etiquetadas @Audio1-3), 'referencia de imagen' (deriva una voz a partir de una imagen de personaje), o 'voz predefinida' (elige una voz incorporada con nombre que lea la indicación). | COMBO | Sí | `"solo texto"`<br>`"referencia de audio"`<br>`"referencia de imagen"`<br>`"voz predefinida"` |
| `reference_audio_1` | Clip de referencia para clonación de voz, etiquetado @Audio1 en la indicación. Hasta 30s. | AUDIO | No | Hasta 30 segundos |
| `reference_audio_2` | Clip de referencia etiquetado @Audio2 en la indicación. Hasta 30s. | AUDIO | No | Hasta 30 segundos |
| `reference_audio_3` | Clip de referencia etiquetado @Audio3 en la indicación. Hasta 30s. | AUDIO | No | Hasta 30 segundos |
| `reference_image` | Una imagen de un solo personaje; el modelo deriva una voz a partir de ella. No se puede combinar con audio de referencia. | IMAGE | No | Imagen única |
| `preset_voice` | Una voz TTS 2.0 incorporada que lee la indicación. No se necesita clip de referencia, y las etiquetas @AudioN no se utilizan en este modo. | COMBO | No | Múltiples opciones de voz predefinida disponibles |
| `sample_rate` | Frecuencia de muestreo de salida en Hz. (predeterminado: "24000") | COMBO | Sí | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Velocidad del habla. 0 = normal, 100 = 2.0x, -50 = 0.5x. (predeterminado: 0) | INT | Sí | -50 a 100 |
| `loudness_rate` | Volumen. 0 = normal, 100 = 2.0x, -50 = 0.5x. (predeterminado: 0) | INT | Sí | -50 a 100 |
| `pitch_rate` | Desplazamiento de tono en semitonos (-12 a 12). (predeterminado: 0) | INT | Sí | -12 a 12 |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 42) | INT | Sí | 0 a 2147483647 |

**Restricciones y dependencias de parámetros:**

- La selección de `reference_mode` determina qué parámetros adicionales son necesarios:
  - **"solo texto"**: No se necesitan entradas de referencia. La indicación no debe contener etiquetas @AudioN.
  - **"referencia de audio"**: Requiere al menos uno de `reference_audio_1`, `reference_audio_2` o `reference_audio_3` conectado. Los clips de referencia deben conectarse en orden sin espacios (ej., si se usan dos clips, conecta `reference_audio_1` y `reference_audio_2`). Cada clip de audio de referencia tiene una duración máxima de 30 segundos. La indicación debe hacer referencia a los clips conectados usando las etiquetas @Audio1, @Audio2, @Audio3 en orden.
  - **"referencia de imagen"**: Requiere que `reference_image` esté conectado. No se puede combinar con ninguna entrada de audio de referencia. La indicación no debe contener etiquetas @AudioN.
  - **"voz predefinida"**: Requiere que `preset_voice` esté seleccionado. No se necesitan clips de referencia. La indicación no debe contener etiquetas @AudioN más allá de @Audio1.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `audio` | La salida de audio generada como una señal de audio. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/es.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
