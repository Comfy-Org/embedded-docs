# Text ersetzen (VERALTET)

Der Replace Text-Node führt eine einfache Textersetzung durch. Er sucht in der Eingabe nach einem angegebenen Textstück und ersetzt jedes Vorkommen durch ein neues Textstück. Der Vorgang wird auf alle Text-Eingaben angewendet, die dem Node bereitgestellt werden.

**Hinweis:** Dieser Node ist veraltet und wurde durch den anderen Replace Text-Node ersetzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `text` | Der zu verarbeitende Text. | STRING | Ja | - |
| `find` | Zu suchender Text (Standard: leerer String). | STRING | Ja | - |
| `replace` | Text, durch den ersetzt wird (Standard: leerer String). | STRING | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `text` | Der verarbeitete Text, bei dem alle Vorkommen des `find`-Textes durch den `replace`-Text ersetzt wurden. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/de.md)

---
**Source fingerprint (SHA-256):** `38beeabc232b19efedf2dcf4e2490f537d9a07d60c89de2811b7a4bddb98cf57`
