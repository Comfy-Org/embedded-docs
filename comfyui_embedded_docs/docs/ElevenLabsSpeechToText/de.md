# ElevenLabs Sprache zu Text

Der ElevenLabs Speech to Text-Node transkribiert Audio mithilfe der ElevenLabs API in Text. Er unterstützt automatische Spracherkennung, Sprecherdiarisierung (Identifizierung verschiedener Sprecher) und Audioereignis-Tagging (Annotation von Geräuschen wie Lachen oder Musik im Transkript).

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Modell, das für die Transkription verwendet wird. Bei Auswahl dieses Modells werden zusätzliche Parameter angezeigt. | DYNAMIC_COMBO | Ja | `"scribe_v2"` |
| `audio` | Audio, das transkribiert werden soll. | AUDIO | Ja | - |
| `language_code` | ISO-639-1- oder ISO-639-3-Sprachcode (z. B. 'en', 'es', 'fra'). Leer lassen für automatische Erkennung. (Standard: "") | STRING | Nein | - |
| `num_speakers` | Maximale Anzahl der vorherzusagenden Sprecher. Auf 0 setzen für automatische Erkennung. (Standard: 0) | INT | Nein | 0 - 32 |
| `seed` | Seed für Reproduzierbarkeit (Determinismus nicht garantiert). (Standard: 1) | INT | Nein | 0 - 2147483647 |

### Scribe v2 Eingaben

Diese Parameter werden angezeigt, wenn das Modell `"scribe_v2"` ausgewählt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | Geräusche wie (Gelächter), (Musik) usw. im Transkript annotieren. (Standard: False) | BOOLEAN | Nein | - |
| `diarize` | Kennzeichnen, welcher Sprecher spricht. (Standard: False) | BOOLEAN | Nein | - |
| `diarization_threshold` | Empfindlichkeit der Sprechertrennung. Niedrigere Werte reagieren empfindlicher auf Sprecherwechsel. Wird nur verwendet, wenn `diarize` aktiviert ist. (Standard: 0.22) | FLOAT | Nein | 0.1 - 0.4 |
| `temperature` | Steuerung der Zufälligkeit. 0.0 verwendet den Modellstandard. Höhere Werte erhöhen die Zufälligkeit. (Standard: 0.0) | FLOAT | Nein | 0.0 - 2.0 |
| `timestamps_granularity` | Zeitliche Genauigkeit für Transkriptwörter. (Standard: "word") | COMBO | Nein | `"word"`<br>`"character"`<br>`"none"` |

**Hinweis:** `num_speakers` kann nicht auf einen Wert größer als 0 gesetzt werden, wenn `diarize` aktiviert ist. Sie müssen entweder `diarize` deaktivieren oder `num_speakers` auf 0 setzen.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `text` | Der transkribierte Text aus dem Audio. | STRING |
| `language_code` | Der erkannte Sprachcode des Audios. | STRING |
| `words_json` | Ein JSON-formatierter String mit detaillierten Informationen auf Wortebene, einschließlich Zeitstempeln und Sprecherbezeichnungen, falls aktiviert. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/de.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
