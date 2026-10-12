# QwenImageTextToImageApi

Qwen Image 3 Text-zu-Bild erzeugt ein oder mehrere Bilder aus einem Text-Prompt mithilfe der Qwen-Image 3.0-Modelle. Sie wählen ein Modell aus und geben einen Prompt an; der Node gibt die generierten Bilder als Batch zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell, das verwendet werden soll (Standard: "qwen-image-3.0-pro"). Dieser zusammengesetzte Selektor stellt außerdem den Prompt, den negativen Prompt, die Bildbreite und die Bildhöhe bereit. | DYNAMIC_COMBO | Ja | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Anzahl der zu generierenden Bilder, die als Batch zurückgegeben werden (Standard: 1). | INT | Nein | 1 bis 6 |
| `seed` | Seed, der für die Generierung verwendet wird (Standard: 42). Kann so eingestellt werden, dass er nach jeder Generierung automatisch aktualisiert wird. | INT | Nein | 0 bis 2147483647 |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung erweitert werden soll (Standard: true). Erweiterte Option. | BOOLEAN | Nein | true<br>false |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: false). Erweiterte Option. | BOOLEAN | Nein | true<br>false |

### qwen-image-3.0-pro und qwen-image-3.0 Eingaben

Gilt gemeinsam für qwen-image-3.0-pro und qwen-image-3.0.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt, der das Bild beschreibt. Unterstützt Englisch und Chinesisch. Muss mindestens 1 Zeichen enthalten. | STRING | Ja | Freitext |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll (Standard: ""). | STRING | Nein | Freitext |
| `width` | Die gesamte Pixelfläche muss zwischen 512x512 und 2560x2560 liegen; jedes Seitenverhältnis innerhalb dieser Fläche ist möglich. (Standard: 1024) | INT | Nein | 256 bis 2560 (Schrittweite 16) |
| `height` | Die gesamte Pixelfläche muss zwischen 512x512 und 2560x2560 liegen; jedes Seitenverhältnis innerhalb dieser Fläche ist möglich. (Standard: 1024) | INT | Nein | 256 bis 2560 (Schrittweite 16) |

Hinweis: Die Eingabe `model` ist ein zusammengesetzter Selektor mit den Unterfeldern `model` (Modell-ID), `prompt` (erforderlich, muss mindestens 1 Zeichen enthalten), `negative_prompt` (optional), `width` und `height`. Die kombinierte Pixelfläche von `width` und `height` muss zwischen 262.144 Pixeln (512x512) und 6.553.600 Pixeln (2560x2560) liegen, und das Seitenverhältnis muss zwischen 1:8 und 8:1 bleiben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das oder die generierten Bilder, als Batch zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
