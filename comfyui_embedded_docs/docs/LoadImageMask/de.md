# LoadImageMask

Der LoadImageMask-Node dient zum Laden von Bildern und den zugehörigen Masken von einem angegebenen Pfad. Er verarbeitet sie, um die Kompatibilität mit weiteren Bildbearbeitungs- oder Analyseaufgaben sicherzustellen. Der Schwerpunkt liegt auf der Handhabung verschiedener Bildformate und Bedingungen, wie z. B. dem Vorhandensein eines Alphakanals für Masken, und er bereitet die Bilder und Masken für die nachgelagerte Verarbeitung vor, indem er sie in ein standardisiertes Format konvertiert.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Parameter `image` gibt die zu ladende und zu verarbeitende Bilddatei an. Er ist entscheidend für die Ausgabe, da er das Quellbild für die Maskenextraktion und Formatkonvertierung bereitstellt. | COMBO[STRING] |
| `channel` | Der Parameter `channel` gibt den Farbkanal des Bildes an, der zur Erzeugung der Maske verwendet wird. Dies ermöglicht Flexibilität bei der Maskenerstellung basierend auf verschiedenen Farbkanälen und erhöht den Nutzen des Nodes in verschiedenen Bildverarbeitungsszenarien. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Dieser Node gibt die aus dem angegebenen Bild und Kanal erzeugte Maske aus, aufbereitet in einem standardisierten Format, das für die weitere Verarbeitung in Bildbearbeitungsaufgaben geeignet ist. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/de.md)
