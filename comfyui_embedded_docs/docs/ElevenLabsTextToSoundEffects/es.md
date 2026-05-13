> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/es.md)

El nodo ElevenLabs Text to Sound Effects genera efectos de sonido a partir de una descripción textual. Utiliza la API de ElevenLabs para crear efectos de sonido basados en tu indicación, permitiéndote controlar la duración, el comportamiento de bucle y qué tan fielmente sigue el sonido al texto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `texto` | STRING | Sí | N/A | Descripción textual del efecto de sonido a generar. Este campo es obligatorio. |
| `modelo` | COMBO | Sí | `"eleven_sfx_v2"` | Modelo a utilizar para la generación del efecto de sonido. Seleccionar este modelo revela parámetros adicionales: `duration` (predeterminado: 5.0, rango: 0.5 a 30.0 segundos), `loop` (predeterminado: Falso) y `prompt_influence` (predeterminado: 0.3, rango: 0.0 a 1.0). |
| `formato_de_salida` | COMBO | Sí | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de salida de audio. |

**Detalles de los parámetros:**

* **`model["duration"]`**: Duración del sonido generado en segundos. El valor predeterminado es 5.0, con un mínimo de 0.5 y un máximo de 30.0.
* **`model["loop"]`**: Cuando está habilitado, crea un efecto de sonido que se repite suavemente. El valor predeterminado es Falso.
* **`model["prompt_influence"]`**: Controla qué tan fielmente la generación sigue la indicación de texto. Los valores más altos hacen que el sonido siga el texto con mayor precisión. El valor predeterminado es 0.3, con un rango de 0.0 a 1.0.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El archivo de audio del efecto de sonido generado. |

---
**Source fingerprint (SHA-256):** `c23c4dd3c9c12f0e891d40683265c5b74b5c6320601aaadb686489510db9f107`
