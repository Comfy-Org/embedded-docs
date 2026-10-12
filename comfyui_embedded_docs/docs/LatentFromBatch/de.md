# latent aus Batch abrufen

Dieser Node ist darauf ausgelegt, eine bestimmte Teilmenge von Latent-Samples aus einem gegebenen Batch basierend auf dem angegebenen Batch-Index und der Länge zu extrahieren. Er ermöglicht die selektive Verarbeitung von Latent-Samples und erleichtert Operationen an kleineren Segmenten des Batches für Effizienz oder gezielte Manipulation.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Die Sammlung von Latent-Samples, aus der eine Teilmenge extrahiert wird. Dieser Parameter ist entscheidend, um den Quell-Batch der zu verarbeitenden Samples zu bestimmen. | `LATENT` |
| `batch_index` | Gibt den Startindex innerhalb des Batches an, an dem die Teilmenge der Samples beginnt. Dieser Parameter ermöglicht die gezielte Extraktion von Samples von bestimmten Positionen im Batch. | `INT` |
| `length` | Definiert die Anzahl der Samples, die ab dem angegebenen Startindex extrahiert werden sollen. Dieser Parameter steuert die Größe der zu verarbeitenden Teilmenge und ermöglicht eine flexible Bearbeitung von Batch-Segmenten. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die extrahierte Teilmenge von Latent-Samples, die nun für die weitere Verarbeitung oder Analyse verfügbar ist. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/de.md)
