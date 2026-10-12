# SaveAudioOpus

Der Node SaveAudioOpus speichert Audiodaten in einer Datei im Opus-Format, wobei Sie die Kodierungsqualität (Bitrate) und das Dateinamenpräfix für die exportierte Datei wählen können. Dieser Node ist veraltet und könnte in zukünftigen Versionen entfernt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Die Audiodaten, die als Opus-Datei gespeichert werden sollen. Ein ValueError wird ausgelöst, wenn dies None ist (zum Beispiel, wenn das Quellvideo keine Audiospur enthält). | AUDIO | Ja | - |
| `filename_prefix` | Das Präfix, das für den Ausgabedateinamen verwendet wird (Standard: "audio/ComfyUI"). | STRING | Nein | - |
| `quality` | Die Bitrate, die zum Kodieren der Opus-Datei verwendet wird; höhere Werte erzeugen eine bessere Qualität, aber größere Dateien (Standard: "128k"). | COMBO | Nein | `"64k"`<br>`"96k"`<br>`"128k"`<br>`"192k"`<br>`"320k"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Die Audiodaten, die in der Opus-Datei gespeichert wurden. | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/de.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
