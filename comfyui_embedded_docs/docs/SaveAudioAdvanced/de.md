# Audio speichern (Erweitert)

Speichert das eingegebene Audio im ComfyUI-Ausgabeverzeichnis. Dieser Node ermöglicht den Export von Audio in verschiedenen Formaten, einschließlich FLAC, MP3 und Opus, mit konfigurierbaren Qualitätseinstellungen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `audio` | Das zu speichernde Audio. | AUDIO | Ja | - |
| `filename_prefix` | Das Präfix für die zu speichernde Datei. Kann Formatierungstokens wie %date:yyyy-MM-dd% enthalten. (Standard: "audio/ComfyUI") | STRING | Ja | - |
| `format` | Das Dateiformat, in dem das Audio gespeichert werden soll. | DYNAMIC_COMBO | Ja | "flac"<br>"mp3"<br>"opus" |

### MP3 Eingaben

Wenn "mp3" als Format ausgewählt wird, wird die folgende Einstellung verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `quality` | Die Kodierungsqualität der ausgegebenen MP3-Datei. (Standard: "V0") | COMBO | Nein | "V0"<br>"128k"<br>"320k" |

### Opus Eingaben

Wenn "opus" als Format ausgewählt wird, wird die folgende Einstellung verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `quality` | Die Kodierungsqualität der ausgegebenen Opus-Datei. (Standard: "128k") | COMBO | Nein | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

Hinweis: Die Einstellung `quality` ist nur verfügbar, wenn das passende Format ausgewählt ist. Wenn "flac" ausgewählt ist, ist keine zusätzliche Qualitätseinstellung verfügbar.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `audio` | Das eingegebene Audio, das nach dem Speichern unverändert weitergegeben wird. | AUDIO |

Der Node gibt außerdem UI-Informationen zurück, die Informationen zur gespeicherten Audiodatei enthalten.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/de.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
