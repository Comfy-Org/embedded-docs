> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/es.md)

El nodo ElevenLabs Text to Dialogue genera un diálogo de audio con múltiples hablantes a partir de texto. Permite crear una conversación especificando diferentes líneas de texto y voces distintas para cada participante. El nodo envía la solicitud de diálogo a la API de ElevenLabs y devuelve el audio generado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `stability` | FLOAT | No | 0.0 - 1.0 | Estabilidad de la voz. Valores más bajos dan un rango emocional más amplio, valores más altos producen un habla más consistente pero potencialmente monótona. (por defecto: 0.5) |
| `apply_text_normalization` | COMBO | No | `"auto"`<br>`"on"`<br>`"off"` | Modo de normalización de texto. 'auto' deja que el sistema decida, 'on' siempre aplica normalización, 'off' la omite. |
| `model` | COMBO | No | `"eleven_v3"` | Modelo a utilizar para la generación del diálogo. |
| `inputs` | DYNAMICCOMBO | Sí | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | Número de entradas de diálogo. Seleccionar un número generará esa cantidad de campos de entrada para texto y voz. |
| `language_code` | STRING | No | - | Código de idioma ISO-639-1 o ISO-639-3 (ej., 'en', 'es', 'fra'). Déjelo vacío para detección automática. (por defecto: vacío) |
| `seed` | INT | No | 0 - 4294967295 | Semilla para reproducibilidad. (por defecto: 1) |
| `output_format` | COMBO | No | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de salida de audio. |

**Nota:** El parámetro `inputs` es dinámico. Cuando selecciona un número (ej., "3"), el nodo mostrará tres campos de entrada `text` y `voice` correspondientes (ej., `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Cada campo `text` debe contener al menos un carácter.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El audio del diálogo con múltiples hablantes generado, en el formato de salida seleccionado. |
