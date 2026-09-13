# ElevenLabs Texto a Diálogo

El nodo ElevenLabs Text to Dialogue genera un diálogo de audio con múltiples hablantes a partir de texto. Permite crear una conversación especificando distintas líneas de texto y voces diferenciadas para cada participante. El nodo envía la solicitud de diálogo a la API de ElevenLabs y devuelve el audio generado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `stability` | Estabilidad de la voz. Los valores más bajos ofrecen un rango emocional más amplio; los valores más altos producen un habla más consistente pero potencialmente monótona. (valor predeterminado: 0.5) | FLOAT | Sí | 0.0 - 1.0 |
| `apply_text_normalization` | Modo de normalización de texto. 'auto' deja que el sistema decida, 'on' siempre aplica la normalización, 'off' la omite. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | Modelo que se usará para la generación de diálogo. | COMBO | Sí | `"eleven_v3"` |
| `inputs` | Número de entradas de diálogo. Al seleccionar un número, se crea esa cantidad de pares de entrada de texto y voz. | DYNAMIC_COMBO | Sí | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | Código de idioma ISO-639-1 o ISO-639-3 (p. ej., 'en', 'es', 'fra'). Déjelo vacío para la detección automática. (valor predeterminado: vacío) | STRING | Sí | - |
| `seed` | Semilla para la reproducibilidad. (valor predeterminado: 1) | INT | Sí | 0 - 4294967295 |
| `output_format` | Formato de salida de audio. | COMBO | Sí | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas por entrada de diálogo

Compartidas por todas las opciones de `inputs`.

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `text1` ... `text10` | Contenido de texto para la entrada de diálogo correspondiente. El nodo crea un campo `text` para cada entrada de diálogo seleccionada. Cada valor de texto debe contener al menos un carácter. | STRING | Sí | - |
| `voice1` ... `voice10` | Voz para la entrada de diálogo correspondiente. Conéctela desde un nodo Voice Selector o Instant Voice Clone. El nodo crea un campo `voice` para cada entrada de diálogo seleccionada. | ELEVENLABS_VOICE | Sí | - |

**Nota:** El selector `inputs` puede crear hasta 10 entradas de diálogo. Cada entrada requiere tanto un campo `text` como un campo `voice`. El valor de `text` no puede estar vacío. La entrada `voice` espera un ID de voz proporcionado por un nodo de voz de ElevenLabs compatible.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `audio` | El audio de diálogo con múltiples hablantes generado en el formato de salida seleccionado. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/es.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
