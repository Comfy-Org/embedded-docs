# RegexMatch

Der RegexMatch-Node prüft, ob eine Textzeichenfolge eine Übereinstimmung für ein gegebenes Muster eines regulären Ausdrucks enthält. Er durchsucht die Eingabezeichenfolge und gibt ein einfaches Ja/Nein-Ergebnis zurück, das angibt, ob das Muster irgendwo im Text gefunden wurde. Sie können die Funktionsweise der Suche anpassen, indem Sie Optionen wie die Suche ohne Berücksichtigung der Groß-/Kleinschreibung oder den Multiline-Modus aktivieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Die Textzeichenfolge, in der nach Übereinstimmungen gesucht wird | STRING | Ja | - |
| `regex_pattern` | Das Muster des regulären Ausdrucks, das mit der Zeichenfolge abgeglichen werden soll | STRING | Ja | - |
| `case_insensitive` | Ob die Groß-/Kleinschreibung bei der Übereinstimmung ignoriert werden soll (Standard: True) | BOOLEAN | Nein | - |
| `multiline` | Ob der Multiline-Modus für den Regex-Abgleich aktiviert werden soll (Standard: False) | BOOLEAN | Nein | - |
| `dotall` | Ob der Dotall-Modus für den Regex-Abgleich aktiviert werden soll (Standard: False) | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `matches` | Gibt True zurück, wenn das Regex-Muster auf einen beliebigen Teil der Eingabezeichenfolge passt, andernfalls False | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/de.md)

---
**Source fingerprint (SHA-256):** `4f0fa717bde7406e42d9a99599eab546690140166d2bb01bb4fde3c5d60e0397`
