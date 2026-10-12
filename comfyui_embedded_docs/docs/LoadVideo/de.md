# Video laden

Der Load Video-Node lädt Videodateien aus dem Eingabeverzeichnis und stellt sie für die Verarbeitung im Workflow bereit. Er liest Videodateien aus dem festgelegten Eingabeordner und gibt sie als Videodaten aus, die mit anderen Video-Verarbeitungs-Nodes verbunden werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `file` | Die aus dem Eingabeverzeichnis zu ladende Videodatei. Die Dropdown-Liste wird dynamisch mit allen im ComfyUI-Eingabeordner gefundenen Videodateien befüllt; neue Videodateien können direkt über die Dateiauswahl hochgeladen werden. | COMBO | Ja | Mehrere Optionen verfügbar (alle Videodateien im Eingabeverzeichnis) |

**Hinweis:** Die verfügbaren Optionen für den Parameter `file` werden dynamisch aus den im Eingabeverzeichnis vorhandenen Videodateien befüllt. Es werden nur Dateien angezeigt, die unterstützten Video-Inhaltstypen entsprechen, und die Liste ist alphabetisch sortiert. Sie können auch eine neue Videodatei direkt über die Dateiauswahl-Oberfläche des Nodes hochladen. Wenn eine zuvor ausgewählte Videodatei nicht mehr gefunden werden kann, meldet der Node einen Fehler für eine ungültige Datei.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Die geladenen Videodaten, die an andere Video-Verarbeitungs-Nodes zur weiteren Bearbeitung oder Analyse übergeben werden können. | VIDEO |

**Hinweis:** Der Node erzeugt außerdem eine Vorschau des geladenen Videos, die direkt am Node angezeigt wird.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/de.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
