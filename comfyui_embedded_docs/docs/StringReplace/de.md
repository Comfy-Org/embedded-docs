# StringReplace

Der StringReplace-Node führt Textersetzungsoperationen auf Eingabezeichenfolgen aus. Er sucht nach einer angegebenen Teilzeichenfolge im Eingabetext und ersetzt alle Vorkommen durch eine andere Teilzeichenfolge. Dieser Node gibt die geänderte Zeichenfolge mit allen angewendeten Ersetzungen zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Die Eingabezeichenfolge, in der Ersetzungen vorgenommen werden | STRING | Ja | - |
| `find` | Die Teilzeichenfolge, nach der im Eingabetext gesucht wird | STRING | Ja | - |
| `replace` | Der Ersetzungstext, der alle gefundenen Vorkommen ersetzt | STRING | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die geänderte Zeichenfolge, bei der alle Vorkommen des Suchtexts durch den Ersetzungstext ersetzt wurden | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringReplace/de.md)

---
**Source fingerprint (SHA-256):** `7f384aff132eb6919b58f04163c4611a7b5545e1af9217f9aca60dc416c06d60`
