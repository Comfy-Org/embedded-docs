# PreviewAudio

Der Preview Audio-Node ermöglicht es Ihnen, Audio direkt in ComfyUI anzuhören, ohne es im Ausgabeverzeichnis zu speichern. Er empfängt eine Audio-Eingabe, prüft, ob tatsächlich Audiodaten vorhanden sind, und spielt sie dann über einen Vorschau-Player in der Oberfläche ab, während dasselbe Audio als Ausgabe weitergegeben wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die Audiodaten für die Vorschau. Wenn diese Eingabe None ist, löst der Node einen ValueError aus, was auftreten kann, wenn das Quellvideo keine Audiospur hat. | AUDIO | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio` | Die unverändert von der Eingabe durchgereichten Audiodaten, sodass der Node in der Mitte eines Workflows platziert werden kann. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/de.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
