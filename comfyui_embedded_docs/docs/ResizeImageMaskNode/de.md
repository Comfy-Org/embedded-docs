# Bild/Maske skalieren

Der Node „Resize Image/Mask“ bietet mehrere Methoden, um die Abmessungen eines Eingabebilds oder einer Eingabemaske zu ändern. Er kann um einen Multiplikator skalieren, bestimmte Abmessungen festlegen, an die Größe einer anderen Eingabe anpassen oder basierend auf der Pixelanzahl anpassen, wobei verschiedene Interpolationsmethoden für die Qualität verwendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `input` | Das Bild oder die Maske, das bzw. die in der Größe geändert werden soll. | IMAGE oder MASK | Ja | N/A |
| `resize_type` | Die Methode zur Bestimmung der neuen Größe. Die erforderlichen Parameter ändern sich je nach ausgewähltem Typ. | COMBO | Ja | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` |
| `multiplier` | Der Skalierungsfaktor. Erforderlich, wenn `resize_type` gleich `SCALE_BY` ist (Standard: 1.00). | FLOAT | Nein | 0.01 bis 8.0 |
| `width` | Die Zielbreite in Pixeln. Erforderlich, wenn `resize_type` gleich `SCALE_DIMENSIONS` oder `SCALE_WIDTH` ist (Standard: 512). | INT | Nein | 0 bis 8192 |
| `height` | Die Zielhöhe in Pixeln. Erforderlich, wenn `resize_type` gleich `SCALE_DIMENSIONS` oder `SCALE_HEIGHT` ist (Standard: 512). | INT | Nein | 0 bis 8192 |
| `crop` | Die Zuschneidemethode, die angewendet werden soll, wenn die Abmessungen nicht dem Seitenverhältnis entsprechen. Nur verfügbar, wenn `resize_type` gleich `SCALE_DIMENSIONS` oder `MATCH_SIZE` ist (Standard: `"center"`). | COMBO | Nein | `"disabled"`<br>`"center"` |
| `longer_size` | Die Zielgröße für die längere Seite des Bildes. Erforderlich, wenn `resize_type` gleich `SCALE_LONGER_DIMENSION` ist (Standard: 512). | INT | Nein | 0 bis 8192 |
| `shorter_size` | Die Zielgröße für die kürzere Seite des Bildes. Erforderlich, wenn `resize_type` gleich `SCALE_SHORTER_DIMENSION` ist (Standard: 512). | INT | Nein | 0 bis 8192 |
| `megapixels` | Die Ziel-Gesamtzahl an Megapixeln. Erforderlich, wenn `resize_type` gleich `SCALE_TOTAL_PIXELS` ist (Standard: 1.0). | FLOAT | Nein | 0.01 bis 16.0 |
| `match` | Ein Bild oder eine Maske, an deren Abmessungen die Eingabe angepasst wird. Erforderlich, wenn `resize_type` gleich `MATCH_SIZE` ist. | IMAGE oder MASK | Nein | N/A |
| `scale_method` | Der Interpolationsalgorithmus, der zum Skalieren verwendet wird (Standard: `"area"`). | COMBO | Ja | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` |

**Hinweis:** Der Parameter `crop` ist nur verfügbar und relevant, wenn `resize_type` auf `SCALE_DIMENSIONS` oder `MATCH_SIZE` gesetzt ist. Bei Verwendung von `SCALE_WIDTH` oder `SCALE_HEIGHT` wird die andere Dimension automatisch skaliert, um das ursprüngliche Seitenverhältnis beizubehalten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `resized` | Das in der Größe geänderte Bild oder die in der Größe geänderte Maske, passend zum Datentyp der Eingabe. | IMAGE oder MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/de.md)

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
