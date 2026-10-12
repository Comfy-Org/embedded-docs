# JoinImageWithAlpha

Dieser Node ist für Compositing-Operationen konzipiert, insbesondere um ein Bild mit seiner zugehörigen Alpha-Maske zu einem einzelnen Ausgabebild zusammenzufügen. Er kombiniert visuellen Inhalt effektiv mit Transparenzinformationen, wodurch Bilder erstellt werden können, bei denen bestimmte Bereiche transparent oder halbtransparent sind.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Hauptbildinhalt, der mit einer Alpha-Maske kombiniert werden soll. Er stellt das Bild ohne Transparenzinformationen dar. | `IMAGE` |
| `alpha` | Die Alpha-Maske, die die Transparenz des zugehörigen Bildes definiert. Sie wird verwendet, um zu bestimmen, welche Teile des Bildes transparent oder halbtransparent sein sollen. | `MASK` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe ist ein einzelnes Bild, das das Eingabebild mit der Alpha-Maske kombiniert und Transparenzinformationen in den visuellen Inhalt integriert. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/de.md)
