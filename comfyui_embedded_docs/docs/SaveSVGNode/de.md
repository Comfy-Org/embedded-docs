# SVG speichern

SVG-Dateien auf der Festplatte speichern. Dieser Node nimmt SVG-Daten als Eingabe entgegen und schreibt sie in das ComfyUI-Ausgabeverzeichnis, wobei die Dateibenennung mit Zählersuffixen automatisch übernommen wird. Wenn Workflow-Prompt-Informationen verfügbar sind, werden sie direkt als Metadaten-Element in die SVG-Datei eingebettet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `svg` | Die SVG-Daten, die auf der Festplatte gespeichert werden sollen | SVG | Ja | - |
| `filename_prefix` | Das Präfix für die zu speichernde Datei. Dies kann Formatierungsinformationen wie %date:yyyy-MM-dd% oder %Empty Latent Image.width% enthalten, um Werte aus Nodes einzubeziehen. (Standard: "svg/ComfyUI") | STRING | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `svg` | Die ursprünglichen SVG-Daten, nach dem Speichern durchgereicht | SVG |
| `ui` | Informationen zur gespeicherten Datei, einschließlich Dateiname, Unterordner und Typ, zur Anzeige in der ComfyUI-Oberfläche | DICT |

**Hinweis:** Dieser Node bettet Workflow-Metadaten (Prompt- und zusätzliche PNG-Informationen) automatisch in die SVG-Datei ein, sofern verfügbar. Die Metadaten werden als CDATA-Abschnitt innerhalb des Metadaten-Elements der SVG eingefügt. Dateien werden nach dem Muster `filename_prefix_00001_.svg` gespeichert; bei der Verarbeitung eines Batches wird `%batch_num%` im Präfix durch den Index des aktuellen Batch-Elements ersetzt. Der Node ist ein Ausgabe-Node, daher erzeugt er ein gespeichertes Ergebnis im Ausgabeordner, obwohl die Datei selbst nicht als Bildvorschau angezeigt wird.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/de.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
