# SaveAudioMP3

Der Node SaveAudioMP3 speichert Audiodaten als MP3-Datei. Er nimmt eine Audio-Eingabe entgegen und exportiert sie in das Ausgabeverzeichnis, mit anpassbarem Dateinamen und Qualitätseinstellung; dabei werden Dateibenennung und MP3-Formatkonvertierung automatisch übernommen. **Dieser Node ist veraltet und könnte in zukünftigen Versionen entfernt werden.**

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `audio` | Die Audiodaten, die als MP3-Datei gespeichert werden sollen | AUDIO | Ja | - |
| `filename_prefix` | Das Präfix für den Namen der Ausgabedatei (Standard: "audio/ComfyUI") | STRING | Nein | - |
| `quality` | Die Audioqualitätseinstellung für die MP3-Datei (Standard: "V0") | COMBO | Nein | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Interne Prompt-Daten, automatisch vom System bereitgestellt | PROMPT | Nein | - |
| `extra_pnginfo` | Zusätzliche PNG-Informationen, automatisch vom System bereitgestellt | EXTRA_PNGINFO | Nein | - |

**Hinweis:** Wenn die Eingabe `audio` None ist (zum Beispiel, wenn das Quellvideo keine Audiospur hat), löst der Node einen ValueError aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `audio` | Die Audiodaten, die als MP3-Datei gespeichert wurden | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/de.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
