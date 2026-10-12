# ImageFromBatch

Der `ImageFromBatch`-Node ist dafür konzipiert, ein bestimmtes Segment von Bildern aus einem Batch basierend auf dem angegebenen Index und der Länge zu extrahieren. Er ermöglicht eine feinere Steuerung der gebündelten Bilder und erlaubt Operationen an einzelnen Bildern oder Teilmengen von Bildern innerhalb eines größeren Batches.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Batch von Bildern, aus dem ein Segment extrahiert wird. Dieser Parameter ist entscheidend, um den Quell-Batch anzugeben. | `IMAGE` |
| `batch_index` | Der Startindex innerhalb des Batches, ab dem die Extraktion beginnt. Er bestimmt die Anfangsposition des aus dem Batch zu extrahierenden Segments. | `INT` |
| `length` | Die Anzahl der Bilder, die ab dem `batch_index` aus dem Batch extrahiert werden sollen. Dieser Parameter definiert die Größe des zu extrahierenden Segments. | `INT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das extrahierte Segment von Bildern aus dem angegebenen Batch. Diese Ausgabe stellt eine Teilmenge des ursprünglichen Batches dar, die durch die Parameter `batch_index` und `length` bestimmt wird. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/de.md)
