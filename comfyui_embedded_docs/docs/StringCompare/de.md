# Text vergleichen

Der Node StringCompare vergleicht zwei Textzeichenfolgen mithilfe verschiedener Vergleichsmethoden. Er kann prüfen, ob eine Zeichenfolge mit einer anderen beginnt, mit einer anderen endet oder ob beide Zeichenfolgen exakt gleich sind. Der Vergleich kann mit oder ohne Berücksichtigung von Groß-/Kleinschreibung durchgeführt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string_a` | Die erste zu vergleichende Zeichenfolge | STRING | Ja | - |
| `string_b` | Die zweite Zeichenfolge, mit der verglichen wird | STRING | Ja | - |
| `mode` | Die zu verwendende Vergleichsmethode (Standard: "Starts With") | COMBO | Ja | "Starts With"<br>"Ends With"<br>"Equal" |
| `case_sensitive` | Ob die Groß-/Kleinschreibung beim Vergleich berücksichtigt werden soll (Standard: true) | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Gibt true zurück, wenn die Vergleichsbedingung erfüllt ist, andernfalls false | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/de.md)

---
**Source fingerprint (SHA-256):** `18599228c31543f270afde0f3b838512ee12d1998b8de42c4d3e7852b1a5d8b2`
