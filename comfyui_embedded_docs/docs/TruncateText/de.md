# TruncateText

Dieser Node kürzt Text, indem er ihn bei einer angegebenen maximalen Länge abschneidet. Er nimmt einen beliebigen Eingabetext entgegen und gibt nur den ersten Teil bis zur eingestellten Zeichenanzahl zurück. Dies ist eine einfache Möglichkeit, um sicherzustellen, dass Text eine bestimmte Größe nicht überschreitet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `text` | Der Textstring, der gekürzt werden soll. | STRING | Ja | N/A |
| `max_length` | Maximale Textlänge. Der Text wird nach dieser Anzahl von Zeichen abgeschnitten (Standard: 77). | INT | Ja | 1 bis 10000 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `string` | Der gekürzte Text, der nur die ersten `max_length` Zeichen aus der Eingabe enthält. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/de.md)

---
**Source fingerprint (SHA-256):** `b23c92af425be8f7b15d793bbe7f321cab6f7f3137a995bb9724948ae00145e4`
