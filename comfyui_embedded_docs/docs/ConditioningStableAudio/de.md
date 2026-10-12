# ConditioningStableAudio

Der Node ConditioningStableAudio fügt sowohl positiven als auch negativen Conditioning-Eingaben Zeitinformationen für die Audiogenerierung hinzu. Er legt die Parameter Startzeit und Gesamtdauer fest, die dabei helfen, zu steuern, wann und wie lange Audioinhalte generiert werden sollen. Dieser Node modifiziert vorhandene Conditioning-Daten, indem er audiospezifische Timing-Metadaten anhängt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Conditioning-Eingabe, die mit Audio-Zeitinformationen modifiziert werden soll | CONDITIONING | Ja | - |
| `negative` | Die negative Conditioning-Eingabe, die mit Audio-Zeitinformationen modifiziert werden soll | CONDITIONING | Ja | - |
| `seconds_start` | Die Startzeit in Sekunden für die Audiogenerierung (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1000.0 (Schrittweite 0.1) |
| `seconds_total` | Die Gesamtdauer in Sekunden für die Audiogenerierung (Standard: 47.0) | FLOAT | Ja | 0.0 bis 1000.0 (Schrittweite 0.1) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierte positive Conditioning-Eingabe mit angewendeten Audio-Zeitinformationen | CONDITIONING |
| `negative` | Die modifizierte negative Conditioning-Eingabe mit angewendeten Audio-Zeitinformationen | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/de.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
