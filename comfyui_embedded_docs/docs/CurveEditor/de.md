# CurveEditor

Der Node Curve Editor bietet eine visuelle Oberfläche zum Anpassen und Feinabstimmen einer Kurve. Sie können die Form einer Eingabekurve direkt in der Oberfläche des Nodes ändern und optional ein Histogramm daneben als visuelle Referenz anzeigen. Der Node unterstützt Zwischenausgaben während der Bearbeitung, sodass Sie Live-Ergebnisse sehen können, während Sie Änderungen vornehmen, und gibt die geänderte Kurve zur Verwendung in anderen Teilen Ihres Workflows aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `curve` | Die zu bearbeitende Eingabekurve. | CURVE | Ja | N/A |
| `histogram` | Ein optionales Histogramm, das neben der Kurve als visuelle Referenz angezeigt wird. | HISTOGRAM | Nein | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `curve` | Die bearbeitete Kurve nach den Anpassungen in der Oberfläche des Nodes. | CURVE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/de.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`
