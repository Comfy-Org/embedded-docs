# StabilityTextToAudio

Generiert hochwertige Musik und Soundeffekte aus Textbeschreibungen. Dieser Node verwendet die Audiogenerierungstechnologie von Stability AI, um Audioinhalte auf Basis Ihrer Text-Prompts zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das zu verwendende Audiogenerierungsmodell (Standard: "stable-audio-2.5") | COMBO | Ja | `"stable-audio-2.5"` |
| `prompt` | Die Textbeschreibung zur Generierung von Audioinhalten (Standard: leerer String) | STRING | Ja | - |
| `duration` | Steuert die Dauer des generierten Audios in Sekunden (Standard: 190) | INT | Nein | 1-190 |
| `seed` | Der für die Generierung verwendete Zufallsseed (Standard: 0) | INT | Nein | 0-4294967294 |
| `steps` | Steuert die Anzahl der Sampling-Schritte (Standard: 8) | INT | Nein | 4-8 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die generierte Audiodatei basierend auf dem Text-Prompt | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/de.md)

---
**Source fingerprint (SHA-256):** `8dfe0eafb6157bc458c2ba3053a98e2bb5dfe896921cf90a70a88c695f8c5edc`
