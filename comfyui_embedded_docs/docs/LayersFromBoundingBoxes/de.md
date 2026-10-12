# LayersFromBoundingBoxes

Dieser Node wandelt einen Bildstapel und seine Bounding-Boxen in einen Ebenenstapel um, erstellt eine Ebene pro Frame und platziert jede Ebene gemäß ihrer zugehörigen Box. Verwenden Sie ihn, wenn ein Node Ebenen als Batch ausgibt, denn ein Batch enthält nur eine einzige Platzierung für jeden Frame, und die einzelnen Positionen würden andernfalls verloren gehen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Bildstapel; jeder Frame wird zu einer Ebene. | IMAGE | Ja | — |
| `bboxes` | Platzierungs-Bounding-Boxen, indexgleich mit dem Bildstapel. Akzeptiert Bounding-Boxen (x, y, Breite, Höhe), normalisierte Elemente (mit einer "bbox" – diese benötigen canvas_width/canvas_height, um in Pixel aufgelöst zu werden), oder eine JSON-Zeichenkette eines der beiden. Frames ohne passende Box werden am Ursprung platziert. Die Breite/Höhe einer Box skaliert die Ebene so, dass sie hineinpasst. metadata.name (oder desc) und metadata.z_index werden verwendet, sofern vorhanden, und metadata.content_rect (frame-relativ) schneidet den Frame auf seinen tatsächlichen Inhalt zu. | BOUNDING_BOX, ARRAY oder STRING | Ja | — |
| `mask` | Transparenz pro Frame, indexgleich mit dem Bildstapel (1 = transparent, LoadImage-Konvention). | MASK | Nein | — |
| `layers` | Ebenenstapel, an den angehängt werden soll. Nicht verbunden lassen, um einen neuen Stapel zu beginnen. | LAYERS | Nein | — |
| `crop_to_content` | Jeden Frame auf metadata.content_rect zuschneiden, sofern vorhanden, und den Inhalt an der Box-Position plus dem Rect-Offset platzieren. Für Batches, deren Frames aufgefüllt sind, eingeschaltet lassen – so bleibt nur der echte Inhalt an seiner richtigen Stelle. (Standard: true) | BOOLEAN | Nein | true<br>false |
| `canvas_width` | Dokument-Canvas-Breite. 0 leitet sie aus den platzierten Ebenen ab. (Standard: 0) | INT | Nein | 0 bis MAX_RESOLUTION |
| `canvas_height` | Dokument-Canvas-Höhe. 0 leitet sie aus den platzierten Ebenen ab. (Standard: 0) | INT | Nein | 0 bis MAX_RESOLUTION |

Hinweise:

- `bboxes` und `mask` müssen indexgleich mit `image` sein: Die n-te Box und der n-te Masken-Frame entsprechen dem n-ten Bild-Frame. Frames ohne passende Box werden am Ursprung platziert.
- Wenn `bboxes` normalisierte Elemente enthält (mit einer "bbox"), müssen `canvas_width` und `canvas_height` angegeben werden, damit diese normalisierten Positionen in Pixel aufgelöst werden können.
- `canvas_width` und `canvas_height` müssen beide größer als 0 sein, um das Dokument-Canvas explizit festzulegen. Wenn einer der Werte 0 ist, wird das Canvas aus den platzierten Ebenen abgeleitet oder vom verbundenen `layers`-Stapel übernommen.
- Wenn `layers` verbunden ist, werden neue Ebenen daran angehängt und erhalten Z-Index-Werte oberhalb des höchsten bereits im Stapel vorhandenen Z-Index.
- Wenn `crop_to_content` aktiviert ist und ein Frame ein metadata.content_rect hat, wird der Frame auf dieses Rect zugeschnitten und die Breiten-/Höhenskalierung der Box wird nicht angewendet; stattdessen wird der Offset des Rects zur Box-Position addiert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `LAYERS` | Der Ebenenstapel, bereit für Create Layered Image. | LAYERS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LayersFromBoundingBoxes/de.md)

---
**Source fingerprint (SHA-256):** `a70956bf0d7ea8bdbd16767ed8b19600b274a6eeb745728f95219578adc73712`
