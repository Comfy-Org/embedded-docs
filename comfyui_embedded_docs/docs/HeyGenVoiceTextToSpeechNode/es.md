# HeyGen Voice 1.0 Text to Speech

Pronuncia texto con una voz clonada mediante HeyGen Voice 1.0 Instant Clone. El nodo envía el texto y el ID de voz a HeyGen y devuelve el habla generada como audio. Hay dos modelos disponibles: `heygen-voice-1` y el más rápido `heygen-voice-1-turbo`, que cuesta la mitad.

Al seleccionar un `model`, se muestran los parámetros específicos de ese modelo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | Modelo a usar. `heygen-voice-1-turbo` es más rápido y cuesta la mitad. Al seleccionar un modelo se muestran los parámetros específicos de este: `voice_id`, `text`, `language` y `expressiveness_boost`. | DYNAMIC_COMBO | Sí | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `voice_id` | Voz de HeyGen Voice 1.0 Instant Clone (predeterminado: vacío). | STRING | Sí | N/A |
| `text` | Texto a pronunciar. Hasta 5000 caracteres; falla la síntesis de voz de más de aproximadamente 12 minutos, así que divida el texto chino o japonés muy largo (predeterminado: vacío). | STRING | Sí | 1 a 5000 caracteres |
| `language` | Idioma del texto. Configúrelo para idiomas estrechamente relacionados, como serbio o malayo, que la detección automática puede confundir (predeterminado: "auto"). | COMBO | Sí | `"auto"`<br>Múltiples preajustes de idioma |
| `expressiveness_boost` | Los valores más altos son más expresivos; los valores más bajos se mantienen más cerca de la voz original (predeterminado: 0.5). | FLOAT | Sí | 0.0 a 1.0 (paso 0.05) |

**Nota:** `voice_id` debe ser una voz creada por HeyGen Voice 1.0 Instant Clone; el nodo se detiene con un error cuando está vacío. `text` debe contener al menos un carácter.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `AUDIO` | La voz generada a partir del texto, pronunciada con la voz clonada. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/es.md)

---
**Source fingerprint (SHA-256):** `61e345563db04a4dfc61e8862a328d5062aa2a77af57c2209ca4ca3862930be8`
