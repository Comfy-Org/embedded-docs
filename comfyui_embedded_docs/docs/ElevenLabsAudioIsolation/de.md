# ElevenLabsAudioIsolation

Der ElevenLabs Voice Isolation-Node entfernt Hintergrundgeräusche aus einer Audiodatei und isoliert die Stimme bzw. Sprache. Er sendet das Audio zur Verarbeitung an die ElevenLabs-API und gibt das bereinigte Audio zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Audio, das zur Entfernung von Hintergrundgeräuschen verarbeitet werden soll. | AUDIO | Ja | |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Das verarbeitete Audio mit entfernten Hintergrundgeräuschen. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/de.md)

---
**Source fingerprint (SHA-256):** `9527f6cc976a72c787985d866dade272f3fcdc485d2bd9e3ceaaaf625822f3e1`
