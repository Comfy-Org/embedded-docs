# WEBM speichern

Der SaveWEBM-Node speichert eine Bildsequenz als WEBM-Videodatei. Er nimmt mehrere Eingabebilder entgegen und kodiert sie mit dem VP9- oder AV1-Codec unter konfigurierbaren Qualitätseinstellungen und Bildrate zu einem Video. Die resultierende Videodatei wird im Ausgabeverzeichnis gespeichert, zusammen mit Metadaten, die Prompt-Informationen enthalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | RGBA-Bilder werden mit ihrem Alpha-Kanal als Transparenz gespeichert (nur VP9-Codec). | IMAGE | Ja | - |
| `filename_prefix` | Präfix für den Ausgabedateinamen (Standard: "ComfyUI"). | STRING | Nein | - |
| `codec` | Für die Kodierung zu verwendender Video-Codec. | COMBO | Ja | "vp9"<br>"av1" |
| `fps` | Bildrate für das Ausgabevideo (Standard: 24.0). | FLOAT | Nein | 0.01-1000.0 |
| `crf` | Ein höherer crf-Wert bedeutet niedrigere Qualität bei kleinerer Dateigröße, ein niedrigerer crf-Wert bedeutet höhere Qualität bei größerer Dateigröße (Standard: 32.0). | FLOAT | Nein | 0-63.0 |

**Hinweis zum Alpha-Kanal:** Der Alpha-Kanal von RGBA-Bildern wird nur beim VP9-Codec beibehalten. Bei Verwendung des AV1-Codecs wird der Alpha-Kanal ignoriert und nur RGB-Daten werden kodiert.

**Hinweis zur Dateibenennung:** Videos werden im Ausgabeverzeichnis als `{filename_prefix}_{counter:05}_.webm` gespeichert, wobei der Zähler automatisch erhöht wird, um das Überschreiben vorhandener Dateien zu vermeiden.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `images` | Die Eingabebilder werden nach dem Speichern des Videos unverändert weitergegeben. | IMAGE |
| UI preview | Videovorschau, die die gespeicherte WEBM-Datei anzeigt. | PREVIEW |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/de.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
