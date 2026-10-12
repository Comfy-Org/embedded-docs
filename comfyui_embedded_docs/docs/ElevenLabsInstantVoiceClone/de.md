# ElevenLabs Instant Voice Clone

Der ElevenLabs Instant Voice Clone-Node erstellt ein neues, einzigartiges Stimmmodell, indem er 1 bis 8 Audioaufnahmen der Stimme einer Person analysiert. Er sendet diese Proben an die ElevenLabs API, die sie verarbeitet, um einen Stimmklon zu erzeugen, der für die Text-zu-Sprache-Synthese verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio_*` | Audioaufnahmen für das Voice-Cloning. Sie müssen zwischen 1 und 8 Audiodateien bereitstellen. | AUDIO | Ja | 1 bis 8 Dateien |
| `remove_background_noise` | Entfernt Hintergrundgeräusche aus Stimmproben mithilfe der Audio-Isolation. (Standard: False) | BOOLEAN | Nein | True / False |

**Hinweis:** Sie müssen mindestens eine Audiodatei bereitstellen, und Sie können bis zu acht bereitstellen. Der Node erstellt automatisch Eingabe-Slots für die Audiodateien, die Sie hinzufügen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `voice` | Die eindeutige Kennung für das neu erstellte geklonte Stimmmodell. Diese Ausgabe kann mit anderen ElevenLabs Text-zu-Sprache-Nodes verbunden werden. | ELEVENLABS_VOICE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/de.md)

---
**Source fingerprint (SHA-256):** `5b109dfff8cdbc51d9e2684b9508b0998aaa014459b973acf29c204835a8db95`
