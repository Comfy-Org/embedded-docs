# LossGraphNode

Der LossGraphNode erstellt ein Liniendiagramm der Trainings-Loss-Werte über die Trainingsschritte und zeigt es als Vorschaubild an. Er liest Loss-Werte von einem Trainings-Node, stellt sie in einem Diagramm mit beschrifteten Achsen sowie minimalen/maximalen Loss-Werten dar und gibt das Diagramm als Bildvorschau in der UI zurück. Dieser Node ist als experimentell gekennzeichnet und ein Ausgabe-Node.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `loss` | Loss-Map vom Trainings-Node. Sie muss einen Schlüssel `loss` mit einer Liste numerischer Loss-Werte enthalten. | LOSS_MAP | Ja | - |
| `filename_prefix` | Präfix für das gespeicherte Loss-Diagrammbild. (Standard: "loss_graph") | STRING | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `ui.images` | Das generierte Loss-Diagrammbild, das als Vorschau angezeigt wird. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/de.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
