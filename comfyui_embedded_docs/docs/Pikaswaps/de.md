# Pikaswaps

Der Pika Swaps-Node ersetzt Objekte oder Bereiche in Ihrem Video durch ein neues Bild. Sie definieren die zu ersetzenden Bereiche mithilfe einer Maske, und der Node ersetzt den angegebenen Inhalt nahtlos während der gesamten Videosequenz.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `video` | Das Video, in dem ein Objekt ersetzt werden soll. | VIDEO | Ja | - |
| `image` | Das Bild, das verwendet wird, um das maskierte Objekt im Video zu ersetzen. | IMAGE | Ja | - |
| `mask` | Verwenden Sie die Maske, um Bereiche im Video zu definieren, die ersetzt werden sollen. | MASK | Ja | - |
| `prompt_text` | Text-Prompt, der die gewünschte Ersetzung beschreibt. | STRING | Ja | - |
| `negative_prompt` | Text-Prompt, der beschreibt, was bei der Ersetzung vermieden werden soll. | STRING | Ja | - |
| `seed` | Zufälliger Seed-Wert für konsistente Ergebnisse. | INT | Ja | 0 bis 4294967295 |

**Hinweis:** Dieser Node erfordert die Angabe aller Eingabeparameter. Die Parameter `video`, `image` und `mask` wirken zusammen, um die Ersetzungsoperation zu definieren, wobei die Maske angibt, welche Bereiche des Videos durch das bereitgestellte Bild ersetzt werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Das verarbeitete Video, in dem das angegebene Objekt oder der angegebene Bereich ersetzt wurde. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/de.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
