# Video speichern

Der Node Save Video speichert das eingegebene Video im Ausgabeverzeichnis von ComfyUI. Sie können das Dateinamenpräfix, das Containerformat, den Videocodec und Kodierungsoptionen wie die Qualität wählen. Der Node generiert automatisch einen eindeutigen Dateinamen mithilfe eines Zählers und kann Workflow-Metadaten in die gespeicherte Datei einbetten.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Das zu speichernde Video. | VIDEO | Ja | - |
| `filename_prefix` | Das Präfix für die zu speichernde Datei. Dies kann Formatierungsinformationen wie `%date:yyyy-MM-dd%` oder `%Empty Latent Image.width%` enthalten, um Werte aus Nodes einzubeziehen (Standard: `video/ComfyUI`). | STRING | Ja | - |
| `format` | Der Ausgabe-Container. Auto verwendet MP4 für Auto/H.264 und WebM für AV1. MP4, MKV und WebM wählen einen bestimmten Container aus. Die Auswahl eines Formats bestimmt auch, welche Codec-Optionen verfügbar sind (Standard: `auto`). | DYNAMIC_COMBO | Ja | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Der Ausgabe-Videocodec. Auto behält einen kompatiblen Quellstream bei. H.264- und AV1-Neukodierung unterstützen SDR, HDR (HLG) und HDR PQ. Diese Auswahl ist unter dem gewählten Format verschachtelt (Standard: `auto`). | DYNAMIC_COMBO | Nein | `"auto"`<br>`"h264"`<br>`"av1"` (nicht verfügbar mit dem `webm`-Format) |

### H.264 Eingaben

Diese Eingaben erscheinen, wenn `codec` `"h264"` ist, und sind mit den Formaten `auto`, `mp4` und `mkv` verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `encoding` | Automatisch behält kompatible H.264-Streams bei. Neukodierung wendet benutzerdefinierte Kodierungsoptionen an. | DYNAMIC_COMBO | Nein | `"auto"`<br>`"re-encode"` |
| `crf` | Niedrigere Werte erzeugen höhere Qualität und größere Dateien. Erscheint, wenn `encoding` `"re-encode"` ist (Standard: 23.0). | FLOAT | Nein | 0.0 bis 51.0 |

### AV1 Eingaben

Diese Eingaben erscheinen, wenn `codec` `"av1"` ist, und sind mit den Formaten `auto`, `mp4`, `mkv` und `webm` verfügbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `encoding` | Automatisch behält kompatible AV1-Streams bei. Neukodierung wendet benutzerdefinierte Kodierungsoptionen an. | DYNAMIC_COMBO | Nein | `"auto"`<br>`"re-encode"` |
| `crf` | Niedrigere Werte erzeugen höhere Qualität und größere Dateien. Erscheint, wenn `encoding` `"re-encode"` ist (Standard: 30.0). | FLOAT | Nein | 0.0 bis 63.0 |

Hinweis: Wenn `format` `"auto"` ist, wird der gespeicherte Container automatisch gewählt: `av1` erzeugt WebM, während `auto` und `h264` MP4 erzeugen. Das Format `webm` erlaubt nur die Codecs `auto` und `av1`. Wenn `codec` `"auto"` ist, wird der Quellvideostream beibehalten statt neu kodiert. Die gespeicherte Datei verwendet ein Zähler-Suffix, um ein Überschreiben vorhandener Dateien zu vermeiden. Die Dateiendung wird durch den aufgelösten Container bestimmt. Workflow-Metadaten (der Prompt und zusätzliche Node-Informationen) werden in die gespeicherte Datei eingebettet, es sei denn, das Speichern von Metadaten ist beim Start deaktiviert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Das eingegebene Video, unverändert. | VIDEO |
| `ui` | Eine Vorschau der gespeicherten Videodatei, einschließlich Dateipfad und Unterordnerinformationen zur Anzeige in der UI. | PREVIEW_VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/de.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
