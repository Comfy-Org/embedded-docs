# Bria FIBO-Bildbearbeitung

Der Bria FIBO Image Edit-Node bearbeitet ein vorhandenes Bild anhand einer Textanweisung. Er sendet das Bild und Ihren Prompt an die Bria API, wo das FIBO-Modell eine bearbeitete Version erstellt. Eine optionale Maske kann die Änderungen auf einen bestimmten Bereich beschränken.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Die Modellversion, die für die Bildbearbeitung verwendet werden soll. | COMBO | Ja | `"FIBO"` |
| `image` | Das Eingabebild, das Sie bearbeiten möchten. | IMAGE | Ja | - |
| `prompt` | Anweisung zum Bearbeiten des Bildes (Standard: leer). | STRING | Ja | - |
| `negative_prompt` | Text, der beschreibt, was im bearbeiteten Bild nicht erscheinen soll (Standard: leer). | STRING | Ja | - |
| `structured_prompt` | Eine Zeichenkette, die den strukturierten Bearbeitungs-Prompt im JSON-Format enthält. Verwenden Sie diesen anstelle des üblichen Prompts für eine präzise, programmatische Steuerung (Standard: leer). | STRING | Ja | - |
| `seed` | Eine Zahl, die zur Initialisierung der Zufallsgenerierung verwendet wird, um reproduzierbare Ergebnisse zu gewährleisten (Standard: 1). | INT | Ja | 1 bis 2147483647 |
| `guidance_scale` | Ein höherer Wert bewirkt, dass sich das Bild stärker an den Prompt hält (Standard: 3). | FLOAT | Ja | 3.0 bis 5.0 |
| `steps` | Die Anzahl der Denoising-Schritte, die vom Modell ausgeführt werden (Standard: 50). | INT | Ja | 20 bis 50 |
| `moderation` | Moderationseinstellungen. Die Auswahl von `"true"` zeigt zusätzliche Moderationsoptionen an. | DYNAMIC_COMBO | Ja | `"false"`<br>`"true"` |
| `mask` | Wenn weggelassen, wird die Bearbeitung auf das gesamte Bild angewendet. | MASK | Nein | - |

### Moderationseingaben

Wenn `moderation` auf `"true"` gesetzt ist, werden diese zusätzlichen Eingaben verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt_content_moderation` | Ob der Prompt-Text auf unangemessene Inhalte moderiert werden soll (Standard: false). | BOOLEAN | Nein | `true`<br>`false` |
| `visual_input_moderation` | Ob das Eingabebild auf unangemessene Inhalte moderiert werden soll (Standard: false). | BOOLEAN | Nein | `true`<br>`false` |
| `visual_output_moderation` | Ob das bearbeitete Ausgabebild auf unangemessene Inhalte moderiert werden soll (Standard: true). | BOOLEAN | Nein | `true`<br>`false` |

**Wichtige Einschränkungen:**

- Genau einer der Werte `prompt` oder `structured_prompt` muss nicht leer sein. Sind beide leer oder beide gesetzt, gibt der Node einen Fehler aus.
- Wenn `mask` verbunden ist, muss es dieselbe Breite und Höhe wie `image` haben, sonst gibt der Node einen Fehler aus.
- Wenn `moderation` auf `"true"` gesetzt ist, werden die drei oben genannten Moderationseingaben angezeigt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `IMAGE` | Das von der Bria API zurückgegebene bearbeitete Bild. | IMAGE |
| `structured_prompt` | Der strukturierte Prompt, der während des Bearbeitungsprozesses verwendet oder generiert wurde. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/de.md)

---
**Source fingerprint (SHA-256):** `0dac537902d73f0cf1803433afa3ede27ed4e3e9cd543bc2e1909b3d49606dd2`
