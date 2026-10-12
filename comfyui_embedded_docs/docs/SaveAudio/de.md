# SaveAudio

Dieser Node speichert Audiodaten in einer Datei im FLAC-Format. Er nimmt eine Audio-Eingabe entgegen und schreibt sie unter Verwendung des angegebenen Dateinamenpräfixes in das Ausgabeverzeichnis. Außerdem reicht er die Audiodaten an seinen Ausgang weiter. Dieser Node ist veraltet und sollte durch den aktuellen Save Audio-Node ersetzt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Die zu speichernden Audiodaten | AUDIO | Ja | - |
| `filename_prefix` | Das Präfix für den Ausgabedateinamen (Standard: "audio/ComfyUI") | STRING | Nein | - |

*Hinweis: Die Parameter `prompt` und `extra_pnginfo` sind ausgeblendet und werden automatisch vom System verarbeitet.*

Wenn die Eingabe `audio` keine Daten empfängt (zum Beispiel, wenn das Quellvideo keine Audiospur hat), löst der Node einen Fehler aus und es wird keine Datei gespeichert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die Audiodaten, die an die Eingabe übergeben wurden, nach dem Speichern der Datei weitergeleitet | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/de.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
