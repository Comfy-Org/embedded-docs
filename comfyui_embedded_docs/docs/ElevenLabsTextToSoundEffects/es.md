> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/es.md)

El nodo ElevenLabs Text to Sound Effects genera efectos de sonido a partir de una descripción de texto. Utiliza la API de ElevenLabs para crear efectos de sonido basados en tu indicación, permitiéndote controlar la duración, el comportamiento de bucle y qué tan fielmente sigue el sonido al texto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sí | N/A | Descripción de texto del efecto de sonido a generar. Este es un campo obligatorio. |
| `model` | COMBO | Sí | `"eleven_sfx_v2"` | Modelo a utilizar para la generación de efectos de sonido. Seleccionar este modelo revela parámetros adicionales: `duration` (por defecto: 5.0, rango: 0.5 a 30.0 segundos), `loop` (por defecto: False), y `prompt_influence` (por defecto: 0.3, rango: 0.0 a 1.0). |
| `output_format` | COMBO | Sí | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de salida de audio. |

**Detalles de los Parámetros:**

* **`model["duration"]`**: Duración del sonido generado en segundos. El valor por defecto es 5.0, con un mínimo de 0.5 y un máximo de 30.0.
* **`model["loop"]`**: Cuando está habilitado, crea un efecto de sonido que se repite suavemente en bucle. El valor por defecto es False.
* **`model["prompt_influence"]`**: Controla qué tan fielmente sigue la generación a la indicación de texto. Valores más altos hacen que el sonido siga el texto más de cerca. El valor por defecto es 0.3, con un rango de 0.0 a 1.0.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El archivo de audio del efecto de sonido generado. |
