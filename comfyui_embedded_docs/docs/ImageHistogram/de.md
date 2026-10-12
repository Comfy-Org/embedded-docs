# Bildhistogramm

Der Node ImageHistogram analysiert die Farbverteilung eines Eingabebilds. Er berechnet und gibt mehrere Histogramme aus, also Diagramme, die zeigen, wie viele Pixel im Bild jeden möglichen Intensitätswert haben. Er erzeugt separate Histogramme für die roten, grünen und blauen Farbkanäle, ein zusammengesetztes RGB-Histogramm und ein Luminanzhistogramm, das auf einer Standard-Helligkeitsformel basiert. Jedes Histogramm enthält 256 Bins und deckt Intensitätsstufen von 0 bis 255 ab.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das zu analysierende Eingabebild. Der Node verarbeitet das erste Bild im Batch. | IMAGE | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `rgb` | Ein zusammengesetztes Histogramm, das die durchschnittliche Pixelintensität über die roten, grünen und blauen Kanäle darstellt. | HISTOGRAM |
| `luminance` | Ein Histogramm der wahrgenommenen Helligkeit des Bildes, berechnet mit der Standard-Luminanzformel ITU-R BT.709. | HISTOGRAM |
| `red` | Ein Histogramm, das die Verteilung der Pixelintensitäten im roten Farbkanal zeigt. | HISTOGRAM |
| `green` | Ein Histogramm, das die Verteilung der Pixelintensitäten im grünen Farbkanal zeigt. | HISTOGRAM |
| `blue` | Ein Histogramm, das die Verteilung der Pixelintensitäten im blauen Farbkanal zeigt. | HISTOGRAM |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/de.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
