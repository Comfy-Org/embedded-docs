# WanMoveVisualizeTracks

Der Node WanMoveVisualizeTracks überlagert Bewegungsverfolgungsdaten auf eine Sequenz von Bildern oder Videoframes. Er zeichnet visuelle Darstellungen der verfolgten Punkte, einschließlich ihrer Bewegungspfade und aktuellen Positionen, wodurch die Bewegungsdaten sichtbar und leichter analysierbar werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Die Sequenz der Eingabebilder oder Videoframes, auf denen die Tracks visualisiert werden sollen. | IMAGE | Ja | - |
| `tracks` | Die Bewegungsverfolgungsdaten mit Punktpfaden und Sichtbarkeitsinformationen. Wenn nicht angegeben, werden die Eingabebilder unverändert durchgereicht. | TRACKS | Nein | - |
| `line_resolution` | Die Anzahl der vorherigen Frames, die beim Zeichnen der nachlaufenden Pfadlinie für jeden Track verwendet werden (Standard: 24). | INT | Ja | 1 - 1024 |
| `circle_size` | Die Größe des Kreises, der an der aktuellen Position jedes Tracks gezeichnet wird (Standard: 12). Als erweiterter Parameter gekennzeichnet. | INT | Ja | 1 - 128 |
| `opacity` | Die Deckkraft der gezeichneten Track-Überlagerungen (Standard: 0.75). | FLOAT | Ja | 0.0 - 1.0 |
| `line_width` | Die Breite der Linien, mit denen die Track-Pfade gezeichnet werden (Standard: 16). Als erweiterter Parameter gekennzeichnet. | INT | Ja | 1 - 128 |

**Hinweis:** Wenn die Anzahl der Eingabebilder nicht mit der Anzahl der Frames in den bereitgestellten `tracks`-Daten übereinstimmt, wird die Bildsequenz wiederholt, um sie an die Länge der Tracks anzupassen.

**Hinweis:** Track-Punkte werden mit einer begrenzten Auswahl sich wiederholender Farben gezeichnet, und ein Punkt wird in einem Frame übersprungen, wenn sein Sichtbarkeits-Flag für diesen Frame null ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `IMAGE` | Die Sequenz der Bilder mit den als Überlagerungen visualisierten Bewegungsverfolgungsdaten. Wenn keine `tracks` bereitgestellt wurden, werden die ursprünglichen Eingabebilder zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/de.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
