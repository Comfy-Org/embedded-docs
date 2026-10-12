# StabilityAudioToAudio

Wandelt vorhandene Audio-Samples mithilfe von Textanweisungen in neue hochwertige Kompositionen um. Dieser Node nimmt eine Eingabe-Audiodatei entgegen und modifiziert sie basierend auf Ihrem Text-Prompt, um neuen Audioinhalt zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das KI-Modell, das für die Audiotransformation verwendet wird | COMBO | Ja | "stable-audio-2.5" |
| `prompt` | Textanweisungen, die beschreiben, wie das Audio transformiert werden soll (Standard: leer, maximale Länge: 10000 Zeichen) | STRING | Ja | |
| `audio` | Audio muss zwischen 6 und 190 Sekunden lang sein | AUDIO | Ja | |
| `duration` | Steuert die Dauer des generierten Audios in Sekunden (Standard: 190) | INT | Nein | 1-190 |
| `seed` | Der für die Generierung verwendete Zufallsseed (Standard: 0) | INT | Nein | 0-4294967294 |
| `steps` | Steuert die Anzahl der Sampling-Schritte (Standard: 8) | INT | Nein | 4-8 |
| `strength` | Der Parameter steuert, wie stark der Parameter `audio` das generierte Audio beeinflusst (Standard: 1.0) | FLOAT | Nein | 0.01-1.0 |

**Hinweis:** Das Eingabe-Audio muss zwischen 6 und 190 Sekunden lang sein. Der Prompt-Text hat eine maximale Länge von 10.000 Zeichen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Das transformierte Audio, das basierend auf dem Eingabe-Audio und dem Text-Prompt generiert wurde | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/de.md)

---
**Source fingerprint (SHA-256):** `3df67797bf2eccf9d7464a1dd00ea5b6c5a9527f7290911c60a9ebff69302241`
