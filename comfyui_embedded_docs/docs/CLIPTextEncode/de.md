# ClipTextEncode

Kodiert einen Text-Prompt mithilfe eines CLIP-Modells in ein Embedding, das verwendet werden kann, um das Diffusionsmodell bei der Generierung bestimmter Bilder zu steuern.

`CLIP Text Encode (CLIPTextEncode)` fungiert als Übersetzer und wandelt Ihre Textbeschreibungen in ein Format um, das die KI verstehen kann. Dies hilft der KI, Ihre Eingabe zu interpretieren und das gewünschte Bild zu generieren.

Stellen Sie sich das wie die Kommunikation mit einem Künstler vor, der eine andere Sprache spricht. Das CLIP-Modell, das auf riesigen Bild-Text-Paaren trainiert wurde, überbrückt diese Lücke, indem es Ihre Beschreibungen in "Anweisungen" umwandelt, denen das KI-Modell folgen kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `text` | Der zu kodierende Text. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | Beliebiger Text |
| `clip` | Das CLIP-Modell, das zur Kodierung des Textes verwendet wird. | CLIP | Ja | Geladene CLIP-Modelle |

Hinweis: Wenn der `clip`-Eingang None ist (zum Beispiel, wenn er von einem Checkpoint-Loader stammt, dessen Checkpoint kein gültiges CLIP- oder Textencoder-Modell enthält), löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Eine Konditionierung, die den eingebetteten Text enthält, der zur Steuerung des Diffusionsmodells verwendet wird. | CONDITIONING |

## Prompt-Funktionen

### Embedding-Modelle

Embedding-Modelle ermöglichen es Ihnen, bestimmte künstlerische Effekte oder Stile anzuwenden. Unterstützte Formate sind `.safetensors`, `.pt` und `.bin`. So verwenden Sie ein Embedding-Modell:

1. Legen Sie die Datei im Ordner `ComfyUI/models/embeddings` ab.
2. Verweisen Sie in Ihrem Text darauf mit `embedding:model_name`.

Beispiel: Wenn Sie ein Modell namens `EasyNegative.pt` in Ihrem Ordner `ComfyUI/models/embeddings` haben, können Sie es wie folgt verwenden:

```
worst quality, embedding:EasyNegative, bad quality
```

**WICHTIG**: Wenn Sie Embedding-Modelle verwenden, stellen Sie sicher, dass der Dateiname übereinstimmt und mit der Architektur Ihres Modells kompatibel ist. Beispielsweise funktioniert ein für SD1.5 entwickeltes Embedding nicht korrekt mit einem SDXL-Modell.

### Anpassung der Prompt-Gewichtung

Sie können die Wichtigkeit bestimmter Teile Ihrer Beschreibung mithilfe von Klammern anpassen. Zum Beispiel:

- `(beautiful:1.2)` erhöht die Gewichtung von "beautiful".
- `(beautiful:0.8)` verringert die Gewichtung von "beautiful".
- Einfache Klammern `(beautiful)` wenden eine Standardgewichtung von 1.1 an.

Sie können die Tastaturkürzel `ctrl + up/down arrow` verwenden, um Gewichtungen schnell anzupassen. Die Schrittweite der Gewichtungsanpassung kann in den Einstellungen geändert werden.

Wenn Sie wörtliche Klammern in Ihrem Prompt verwenden möchten, ohne die Gewichtung zu ändern, können Sie sie mit einem Backslash maskieren, z. B. `\(word\)`.

### Wildcard-/Dynamische Prompts

Verwenden Sie `{}`, um dynamische Prompts zu erstellen. Zum Beispiel wählt `{day|night|morning}` bei jeder Verarbeitung des Prompts zufällig eine Option aus.

Wenn Sie wörtliche geschweifte Klammern in Ihrem Prompt verwenden möchten, ohne dynamisches Verhalten auszulösen, können Sie sie mit einem Backslash maskieren, z. B. `\{word\}`.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/de.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
