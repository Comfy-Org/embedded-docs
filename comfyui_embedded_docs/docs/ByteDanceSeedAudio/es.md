# ByteDanceSeedAudio

Genera voz, música, efectos de sonido y diálogo multi-locutor a partir de un solo prompt con ByteDance Seed Audio 1.0. Describe la(s) voz(ces), emoción, ambiente, música de fondo y efectos de sonido en el prompt, e incluye las líneas a hablar. Opcionalmente, selecciona una voz predefinida integrada, clona voces de hasta 3 clips de referencia (etiquetados como @Audio1-3 en el prompt), o deriva una voz a partir de una imagen de personaje. Hasta 2 minutos de audio por ejecución.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `text_prompt` | Describe la(s) voz(ces), emoción, ritmo, ambiente, música de fondo y efectos de sonido, e incluye las líneas a hablar (nombra personajes en línea para diálogos). En modo 'referencia de audio', refiérete a los clips conectados por orden como @Audio1, @Audio2, @Audio3. Máximo 3000 caracteres. | STRING | Sí | 1 a 3000 caracteres |
| `reference_mode` | Cómo condicionar la voz: 'solo texto' (describe todo en el prompt), 'referencia de audio' (clona hasta 3 voces, etiquetadas @Audio1-3), 'referencia de imagen' (deriva una voz de una imagen de personaje), o 'voz predefinida' (selecciona una voz integrada con nombre que lee el prompt). | COMBO | Sí | `"solo texto"`<br>`"referencia de audio"`<br>`"referencia de imagen"`<br>`"voz predefinida"` |
| `reference_audio_1` | Clip de referencia para clonación de voz, etiquetado @Audio1 en el prompt. Hasta 30s. Solo disponible cuando `reference_mode` es "referencia de audio". | AUDIO | No | Hasta 30 segundos |
| `reference_audio_2` | Clip de referencia etiquetado @Audio2 en el prompt. Hasta 30s. Solo disponible cuando `reference_mode` es "referencia de audio". | AUDIO | No | Hasta 30 segundos |
| `reference_audio_3` | Clip de referencia etiquetado @Audio3 en el prompt. Hasta 30s. Solo disponible cuando `reference_mode` es "referencia de audio". | AUDIO | No | Hasta 30 segundos |
| `reference_image` | Una imagen de un solo personaje; el modelo deriva una voz a partir de ella. No se puede combinar con audio de referencia. Solo disponible cuando `reference_mode` es "referencia de imagen". | IMAGE | No | - |
| `preset_voice` | Una voz TTS 2.0 integrada que lee el prompt. No se necesita clip de referencia, y las etiquetas @AudioN no se utilizan en este modo. Solo disponible cuando `reference_mode` es "voz predefinida". | COMBO | No | Múltiples opciones disponibles (ver descripción) |
| `sample_rate` | Frecuencia de muestreo de salida en Hz. (predeterminado: "24000") | COMBO | Sí | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | Velocidad del habla. 0 = normal, 100 = 2.0x, -50 = 0.5x. (predeterminado: 0) | INT | Sí | -50 a 100 |
| `loudness_rate` | Volumen. 0 = normal, 100 = 2.0x, -50 = 0.5x. (predeterminado: 0) | INT | Sí | -50 a 100 |
| `pitch_rate` | Desplazamiento de tono en semitonos (-12 a 12). (predeterminado: 0) | INT | Sí | -12 a 12 |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 42) | INT | Sí | 0 a 2147483647 |

### Restricciones de Parámetros

- **Dependencias del modo de referencia**: El parámetro `reference_mode` determina qué otras entradas son necesarias:
  - **"solo texto"**: No se requieren entradas adicionales. El prompt no debe contener etiquetas @AudioN.
  - **"referencia de audio"**: Requiere que al menos uno de `reference_audio_1`, `reference_audio_2` o `reference_audio_3` esté conectado. Los clips de referencia deben conectarse en orden sin espacios (ej., _1, luego _2, luego _3). Cada clip tiene una duración máxima de 30 segundos. El prompt debe hacer referencia a los clips conectados usando las etiquetas @Audio1, @Audio2, @Audio3.
  - **"referencia de imagen"**: Requiere que `reference_image` esté conectado. El prompt no debe contener etiquetas @AudioN.
  - **"voz predefinida"**: Requiere que `preset_voice` esté seleccionado. El prompt no debe contener etiquetas @AudioN (todo el prompt se lee con la voz seleccionada).

- **Orden de referencia de audio**: Al usar el modo "referencia de audio", las entradas de audio de referencia deben conectarse secuencialmente comenzando desde `reference_audio_1` sin espacios. Por ejemplo, puedes conectar _1 y _2, pero no _1 y _3 sin _2.

- **Etiquetas de audio máximas**: El prompt puede hacer referencia hasta 3 clips de audio (@Audio1, @Audio2, @Audio3) cuando está en modo "referencia de audio". La etiqueta con el número más alto no debe exceder el número de entradas de audio de referencia conectadas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `AUDIO` | La salida de audio generada por ByteDance Seed Audio 1.0, que contiene voz, música, efectos de sonido o diálogo multi-locutor según lo descrito en el prompt. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/es.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
