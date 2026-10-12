# ByteDanceImageEditNode

Der ByteDance Image Edit-Node ermöglicht es Ihnen, Bilder mithilfe der KI-Modelle von ByteDance über eine API zu bearbeiten. Sie geben ein Eingabebild und einen Text-Prompt an, der die gewünschten Änderungen beschreibt, und der Node verarbeitet das Bild gemäß Ihren Anweisungen. Der Node übernimmt die API-Kommunikation automatisch und gibt das bearbeitete Bild zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `model` | Modellname | MODEL | COMBO | seededit_3 | Image2ImageModelName options |
| `image` | Das Basisbild, das bearbeitet werden soll | IMAGE | IMAGE | - | - |
| `prompt` | Anweisung zum Bearbeiten des Bildes | STRING | STRING | "" | - |
| `seed` | Seed für die Generierung | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | Ein höherer Wert bewirkt, dass sich das Bild stärker nach dem Prompt richtet | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | Ob ein "AI generated"-Wasserzeichen zum Bild hinzugefügt werden soll | BOOLEAN | BOOLEAN | True | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Das von der ByteDance-API zurückgegebene bearbeitete Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/de.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
