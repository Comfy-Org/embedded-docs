# Text enthält

Der Node StringContains prüft, ob ein gegebener String einen angegebenen Teilstring enthält. Er kann diese Prüfung entweder mit Beachtung oder ohne Beachtung der Groß-/Kleinschreibung durchführen und gibt ein boolesches Ergebnis zurück, das angibt, ob der Teilstring im Hauptstring gefunden wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `string` | Der Haupttext-String, in dem gesucht werden soll | STRING | Ja | - |
| `substring` | Der Text, nach dem im Hauptstring gesucht werden soll | STRING | Ja | - |
| `case_sensitive` | Legt fest, ob die Suche die Groß-/Kleinschreibung beachten soll (Standard: true) | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `contains` | Gibt true zurück, wenn der Teilstring im String gefunden wird, andernfalls false | BOOLEAN |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/de.md)

---
**Source fingerprint (SHA-256):** `9e85e51bc32c4041a66de8d5b11475aba3120eee1e8c5a37fedfaa470746888c`
