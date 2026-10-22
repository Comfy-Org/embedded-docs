# RescaleCfg

Der Node RescaleCFG ist darauf ausgelegt, die Skalen für Konditionierung und Unkonditionierung der Ausgabe eines Modells basierend auf einem angegebenen Multiplikator anzupassen, um einen ausgewogeneren und kontrollierteren Generierungsprozess zu erreichen. Er arbeitet, indem er die Ausgabe des Modells neu skaliert, um den Einfluss der konditionierten und unkonditionierten Komponenten zu verändern, wodurch möglicherweise die Leistung des Modells oder die Qualität der Ausgabe verbessert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Der Parameter `model` repräsentiert das generative Modell, das angepasst werden soll. Er ist entscheidend, da der Node eine Neuskalierungsfunktion auf die Ausgabe des Modells anwendet und dadurch den Generierungsprozess direkt beeinflusst. | MODEL |
| `multiplier` | Der Parameter `multiplier` steuert das Ausmaß der Neuskalierung, die auf die Ausgabe des Modells angewendet wird. Er bestimmt die Balance zwischen den ursprünglichen und den neu skalierten Komponenten und beeinflusst die Eigenschaften der endgültigen Ausgabe. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angepassten Skalen für Konditionierung und Unkonditionierung. Dieses Modell soll aufgrund der angewendeten Neuskalierung Ausgaben mit potenziell verbesserten Eigenschaften erzeugen. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/de.md)
