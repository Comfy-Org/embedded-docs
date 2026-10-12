# Bilder neu bündeln

Der RebatchImages-Node dient dazu, einen Batch von Bildern in eine neue Batch-Konfiguration umzuorganisieren und dabei die Batch-Größe wie angegeben anzupassen. Dieser Prozess ist wesentlich für die Verwaltung und Optimierung der Verarbeitung von Bilddaten in Batch-Operationen, damit Bilder entsprechend der gewünschten Batch-Größe gruppiert werden und effizient verarbeitet werden können.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `images` | Eine Liste von Bildern, die neu gebatcht werden sollen. Dieser Parameter ist entscheidend, um die Eingabedaten zu bestimmen, die dem Rebatching-Prozess unterzogen werden. | `IMAGE` |
| `batch_size` | Gibt die gewünschte Größe der Ausgabe-Batches an. Dieser Parameter beeinflusst direkt, wie die Eingabebilder gruppiert und verarbeitet werden, und wirkt sich auf die Struktur der Ausgabe aus. | `INT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe besteht aus einer Liste von Bild-Batches, die entsprechend der angegebenen Batch-Größe neu organisiert wurden. Dies ermöglicht eine flexible und effiziente Verarbeitung von Bilddaten in Batch-Operationen. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/de.md)
