# ModelMergeSubtract

Dieser Node ist für fortgeschrittene Modell-Merging-Operationen konzipiert, insbesondere um die Parameter eines Modells anhand eines angegebenen Multiplikators von einem anderen Modell zu subtrahieren. Er ermöglicht die Anpassung von Modellverhalten, indem der Einfluss der Parameter eines Modells auf ein anderes reguliert wird, und erleichtert die Erstellung neuer, hybrider Modelle.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model1` | Das Basismodell, von dem die Parameter subtrahiert werden. | `MODEL` |
| `model2` | Das Modell, dessen Parameter vom Basismodell subtrahiert werden. | `MODEL` |
| `multiplier` | Ein Gleitkommawert, der den Subtraktionseffekt auf die Parameter des Basismodells skaliert. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das resultierende Modell nach dem Subtrahieren der Parameter eines Modells von einem anderen, skaliert durch den Multiplikator. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/de.md)
