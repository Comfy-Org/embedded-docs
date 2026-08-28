# FishAudioSpeechToText

Este nodo transcribe audio a texto utilizando el servicio de voz a texto de Fish Audio. Detecta automáticamente el idioma del audio y puede opcionalmente devolver segmentos con marcas de tiempo a nivel de palabra como JSON.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `audio` | Audio a transcribir. | AUDIO | Sí | — |
| `idioma` | Sugerencia de idioma ISO 639-1 (p. ej. 'en', 'zh'). El idioma se detecta automáticamente de todos modos. Predeterminado: "" (cadena vacía). | STRING | No | Cualquier código de idioma ISO 639-1, p. ej. `en`, `zh`; cadena vacía para auto-detección |
| `precise_timestamps` | Devuelve segmentos con marcas de tiempo a nivel de palabra. Predeterminado: false. | BOOLEAN | No | true o false |

Nota: El parámetro `language` es solo una sugerencia: el idioma siempre se detecta automáticamente a partir del audio. Cuando `precise_timestamps` es false (el valor predeterminado), no se devuelven marcas de tiempo a nivel de palabra; cuando es true, los segmentos de salida incluyen marcas de tiempo a nivel de palabra.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `texto` | El texto transcrito. | STRING |
| `language_code` | El código de idioma ISO 639-1 detectado para el audio. | STRING |
| `segments_json` | Cadena JSON que contiene los segmentos de transcripción. Incluye marcas de tiempo a nivel de palabra cuando `precise_timestamps` está habilitado. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/es.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
