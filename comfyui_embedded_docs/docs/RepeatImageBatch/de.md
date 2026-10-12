# Bild-Batch wiederholen

Der Node RepeatImageBatch ist darauf ausgelegt, ein gegebenes Bild eine bestimmte Anzahl von Malen zu replizieren und so eine Batch identischer Bilder zu erzeugen. Diese Funktionalität ist nützlich für Vorgänge, die mehrere Instanzen desselben Bildes erfordern, wie Batch-Verarbeitung oder Datenaugmentierung.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Parameter `image` stellt das zu replizierende Bild dar. Er ist entscheidend für die Definition des Inhalts, der über die Batch hinweg dupliziert wird. | `IMAGE` |
| `amount` | Der Parameter `amount` gibt an, wie oft das Eingabebild repliziert werden soll. Er beeinflusst direkt die Größe der Ausgabe-Batch und ermöglicht eine flexible Batch-Erstellung. | `INT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe ist eine Batch von Bildern, von denen jedes mit dem Eingabebild identisch ist und gemäß dem angegebenen `amount` repliziert wurde. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/de.md)
