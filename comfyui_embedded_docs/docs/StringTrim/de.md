# Text bereinigen

Der Node StringTrim entfernt Leerzeichen (wie Leerzeichen, Tabulatoren und Zeilenumbrüche) am Anfang, am Ende oder auf beiden Seiten einer Textzeichenfolge. Sie können wählen, ob Sie vom linken Rand, rechten Rand oder beiden Seiten der Zeichenfolge trimmen möchten. Dies ist nützlich, um Texteingaben durch Entfernen unerwünschter Leerzeichen zu bereinigen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Die zu verarbeitende Textzeichenfolge. Unterstützt mehrzeilige Eingabe. | STRING | Ja | - |
| `mode` | Gibt an, welche Seite(n) der Zeichenfolge getrimmt werden soll(en). „Both“ entfernt Leerzeichen an beiden Enden, „Left“ nur am Anfang, „Right“ nur am Ende. | COMBO | Ja | "Both"<br>"Left"<br>"Right" |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die getrimmte Textzeichenfolge, bei der Leerzeichen gemäß dem ausgewählten Modus entfernt wurden. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/de.md)

---
**Source fingerprint (SHA-256):** `b7d0694b752f3017a5f8ee9a6ca1d88260f761576b5960f2cb210e34efb09d18`
