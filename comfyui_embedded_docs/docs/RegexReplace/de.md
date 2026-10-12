# RegexReplace

Der RegexReplace-Node sucht und ersetzt Text in Zeichenketten mithilfe von Mustern regulärer Ausdrücke. Er ermöglicht die Suche nach Textmustern und deren Ersetzung durch neuen Text, mit Optionen zur Steuerung der Mustererkennung, einschließlich Groß-/Kleinschreibung, Mehrzeilenübereinstimmung und Begrenzung der Anzahl der Ersetzungen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Die Eingabe-Zeichenkette, in der gesucht und ersetzt wird | STRING | Ja | - |
| `regex_pattern` | Das Muster des regulären Ausdrucks, nach dem in der Eingabe-Zeichenkette gesucht wird | STRING | Ja | - |
| `replace` | Der Ersetzungstext, der für übereinstimmende Muster eingesetzt wird | STRING | Ja | - |
| `case_insensitive` | Wenn aktiviert, ignoriert der Musterabgleich Unterschiede bei der Groß-/Kleinschreibung (Standard: True) | BOOLEAN | Nein | - |
| `multiline` | Wenn aktiviert, ändert sich das Verhalten von ^ und $, sodass sie am Anfang/Ende jeder Zeile übereinstimmen statt nur am Anfang/Ende der gesamten Zeichenkette (Standard: False) | BOOLEAN | Nein | - |
| `dotall` | Wenn aktiviert, stimmt das Punktzeichen (.) mit jedem Zeichen überein, einschließlich Zeilenumbruchzeichen. Wenn deaktiviert, stimmen Punkte nicht mit Zeilenumbrüchen überein (Standard: False) | BOOLEAN | Nein | - |
| `count` | Maximale Anzahl der vorzunehmenden Ersetzungen. Auf 0 setzen, um alle Vorkommen zu ersetzen (Standard). Auf 1 setzen, um nur den ersten Treffer zu ersetzen, 2 für die ersten beiden Treffer usw. (Standard: 0) | INT | Nein | 0-100 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die geänderte Zeichenkette, auf die die angegebenen Ersetzungen angewendet wurden | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/de.md)

---
**Source fingerprint (SHA-256):** `58d4ec055aa5901b0e536bb2ca6993053ea85a9269d09cdcdf584df935d6876d`
