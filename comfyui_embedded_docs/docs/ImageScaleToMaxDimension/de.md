# Bild auf maximale Abmessung skalieren

Der Node ImageScaleToMaxDimension ändert die Größe von Bildern, sodass sie in eine angegebene maximale Dimension passen, während das ursprüngliche Seitenverhältnis beibehalten wird. Er ermittelt, ob das Bild im Hoch- oder Querformat vorliegt, und skaliert dann die größere Dimension auf die Zielgröße, während die kleinere Dimension proportional angepasst wird. Der Node unterstützt mehrere Hochskalierungsmethoden für unterschiedliche Anforderungen an Qualität und Leistung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, dessen Größe geändert werden soll | IMAGE | Ja | - |
| `upscale_method` | Die Interpolationsmethode, die für die Skalierung des Bildes verwendet wird (Standard: "area") | STRING | Ja | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" |
| `largest_size` | Die maximale Dimension für das skalierte Bild (Standard: 512) | INT | Ja | 0 bis 16384 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das skalierte Bild, dessen größte Dimension der angegebenen Größe entspricht | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/de.md)

---
**Source fingerprint (SHA-256):** `83eba56d9f673fb570edc6504fd82f1274ead1d3e055a1a8bcc207c178388015`
