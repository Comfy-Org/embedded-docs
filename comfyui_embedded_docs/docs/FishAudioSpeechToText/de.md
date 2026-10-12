# FishAudioSpeechToText

Dieser Node transkribiert Audio mithilfe des Fish Audio Speech-to-Text-Dienstes in Text. Er erkennt die Sprache des Audios automatisch und kann optional zeitgestempelte Segmente auf Wortebene als JSON zurückgeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `audio` | Audio, das transkribiert werden soll. | AUDIO | Ja | — |
| `language` | ISO-639-1-Sprachhinweis (z. B. 'en', 'zh'). Die Sprache wird unabhängig davon automatisch erkannt. Standard: "" (leere Zeichenkette). | STRING | Nein | Beliebiger ISO-639-1-Sprachcode, z. B. `en`, `zh`; leere Zeichenkette für automatische Erkennung |
| `precise_timestamps` | Gibt zeitgestempelte Segmente auf Wortebene zurück. Standard: false. | BOOLEAN | Nein | true or false |

Hinweis: Der Parameter `language` ist nur ein Hinweis – die Sprache wird immer automatisch aus dem Audio erkannt. Wenn `precise_timestamps` false ist (der Standard), werden keine Zeitstempel auf Wortebene zurückgegeben; wenn true, enthalten die Ausgabesegmente Zeitstempel auf Wortebene.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `text` | Der transkribierte Text. | STRING |
| `language_code` | Der für das Audio erkannte ISO-639-1-Sprachcode. | STRING |
| `segments_json` | JSON-Zeichenkette, die die Transkriptionssegmente enthält. Enthält Zeitstempel auf Wortebene, wenn `precise_timestamps` aktiviert ist. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/de.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
