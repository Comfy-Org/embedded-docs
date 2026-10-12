# Text verketten

Der Node StringConcatenate kombiniert zwei Textzeichenfolgen zu einer, indem er sie mit einem angegebenen Trennzeichen verbindet. Er nimmt zwei Eingabezeichenfolgen sowie ein Trennzeichen (ein Zeichen oder eine Zeichenfolge) entgegen und gibt dann eine einzelne Zeichenfolge aus, in der die beiden Eingaben mit dem dazwischen eingefügten Trennzeichen verbunden sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string_a` | Die erste zu verkettende Textzeichenfolge | STRING | Ja | - |
| `string_b` | Die zweite zu verkettende Textzeichenfolge | STRING | Ja | - |
| `delimiter` | Das Zeichen oder die Zeichenfolge, die zwischen den beiden Eingabezeichenfolgen eingefügt wird (Standard: leere Zeichenfolge) | STRING | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die kombinierte Zeichenfolge mit dem zwischen `string_a` und `string_b` eingefügten Trennzeichen | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/de.md)

---
**Source fingerprint (SHA-256):** `ea6fa7948d07e87b7ea3aeaf4f38c4cfdbfa5c5bd56d9f2935f94f1775686d08`
