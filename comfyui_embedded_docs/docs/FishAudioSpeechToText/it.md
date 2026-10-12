# FishAudioSpeechToText

Questo nodo trascrive l'audio in testo usando il servizio speech-to-text di Fish Audio. Rileva automaticamente la lingua dell'audio e può restituire facoltativamente segmenti con timestamp a livello di parola in formato JSON.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `audio` | Audio da trascrivere. | AUDIO | Sì | — |
| `language` | Suggerimento di lingua ISO 639-1 (ad es. 'en', 'zh'). La lingua viene comunque rilevata automaticamente. Predefinito: "" (stringa vuota). | STRING | No | Qualsiasi codice lingua ISO 639-1, ad es. `en`, `zh`; stringa vuota per il rilevamento automatico |
| `precise_timestamps` | Restituisce segmenti con timestamp a livello di parola. Predefinito: false. | BOOLEAN | No | true o false |

Nota: Il parametro `language` è solo un suggerimento — la lingua viene sempre rilevata automaticamente dall'audio. Quando `precise_timestamps` è false (impostazione predefinita), i timestamp a livello di parola non vengono restituiti; quando è true, i segmenti di output includono timestamp a livello di parola.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `text` | Il testo trascritto. | STRING |
| `language_code` | Il codice lingua ISO 639-1 rilevato per l'audio. | STRING |
| `segments_json` | Stringa JSON contenente i segmenti di trascrizione. Include timestamp a livello di parola quando `precise_timestamps` è abilitato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/it.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
