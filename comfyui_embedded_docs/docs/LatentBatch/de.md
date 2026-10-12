# LatentBatch

Der Node `LatentBatch` ist dafür konzipiert, zwei Sätze latenter Samples zu einem einzigen Batch zusammenzuführen, wobei ein Satz vor der Verkettung möglicherweise an die Abmessungen des anderen angepasst wird. Diese Operation erleichtert die Kombination unterschiedlicher latenter Repräsentationen für weitere Verarbeitungs- oder Generierungsaufgaben.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples1` | Der erste Satz latenter Samples, der zusammengeführt werden soll. Er spielt eine entscheidende Rolle bei der Bestimmung der endgültigen Form des zusammengeführten Batches. | `LATENT` |
| `samples2` | Der zweite Satz latenter Samples, der zusammengeführt werden soll. Wenn seine Abmessungen von denen des ersten Satzes abweichen, wird er angepasst, um vor dem Zusammenführen die Kompatibilität sicherzustellen. | `LATENT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Der zusammengeführte Satz latenter Samples, der nun für die weitere Verarbeitung zu einem einzigen Batch kombiniert wurde. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/de.md)
