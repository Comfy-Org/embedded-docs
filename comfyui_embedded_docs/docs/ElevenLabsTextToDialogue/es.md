# ElevenLabs Texto a Diálogo

El nodo ElevenLabs Text to Dialogue genera un diálogo de audio multiparlante a partir de texto. Permite crear una conversación especificando diferentes líneas de texto y voces distintas para cada participante. El nodo envía la solicitud de diálogo a la API de ElevenLabs y devuelve el audio generado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `estabilidad` | Estabilidad de la voz. Los valores más bajos ofrecen un rango emocional más amplio; los valores más altos producen un habla más consistente pero potencialmente monótona. (por defecto: 0.5) | FLOAT | Sí | 0.0 - 1.0 |
| `aplicar_normalización_de_texto` | Modo de normalización de texto. 'auto' permite que el sistema decida, 'on' aplica siempre la normalización, 'off' la omite. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `modelo` | Modelo a utilizar para la generación del diálogo. | COMBO | Sí | `"eleven_v3"` |
| `entradas` | Número de entradas de diálogo. Seleccionar un número genera esa cantidad de campos de entrada de texto y voz. | DYNAMIC_COMBO | Sí | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `código_de_idioma` | Código de idioma ISO-639-1 o ISO-639-3 (por ejemplo, 'en', 'es', 'fra'). Déjelo vacío para detección automática. (por defecto: vacío) | STRING | Sí | - |
| `semilla` | Semilla para reproducibilidad. (por defecto: 1) | INT | Sí | 0 - 4294967295 |
| `formato_de_salida` | Formato de salida de audio. | COMBO | Sí | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Nota:** El parámetro `inputs` es dinámico. Cuando selecciona un número (por ejemplo, "3"), el nodo mostrará tres campos de entrada `text` y `voice` correspondientes (por ejemplo, `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Cada campo `text` debe contener al menos un carácter. Cada campo `voice` acepta una voz conectada desde el nodo Voice Selector o Instant Voice Clone.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El audio de diálogo multiparlante generado en el formato de salida seleccionado. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/es.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
