# OpenAIGPTImage1

Erzeugt Bilder synchron über den GPT Image-Endpunkt von OpenAI. Es kann neue Bilder aus einem Text-Prompt erstellen oder vorhandene Bilder bearbeiten, wenn ein Eingabebild und eine optionale Maske bereitgestellt werden. Der Node unterstützt die Modelle `gpt-image-1`, `gpt-image-1.5` und `gpt-image-2` und ist als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text-Prompt für GPT Image (Standard: "") | STRING | Ja | - |
| `seed` | Zufälliger Seed für die Generierung; im Backend noch nicht implementiert (Standard: 0) | INT | Nein | 0 to 2147483647 |
| `quality` | Bildqualität; beeinflusst Kosten und Generierungszeit (Standard: "low") | COMBO | Nein | "low"<br>"medium"<br>"high" |
| `background` | Gibt das Bild mit oder ohne Hintergrund zurück (Standard: "auto") | COMBO | Nein | "auto"<br>"opaque"<br>"transparent" |
| `size` | Bildgröße. Wählen Sie "Custom", um die benutzerdefinierte Breite und Höhe zu verwenden (nur GPT Image 2) (Standard: "auto") | COMBO | Nein | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Anzahl der zu generierenden Bilder (Standard: 1) | INT | Nein | 1 to 8 |
| `image` | Optionales Referenzbild für die Bildbearbeitung | IMAGE | Nein | - |
| `mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt) | MASK | Nein | - |
| `model` | Zu verwendendes GPT Image-Modell (Standard: "gpt-image-2") | COMBO | Nein | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Wird nur verwendet, wenn `size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein (nur GPT Image 2) (Standard: 1024) | INT | Nein | 1024 to 3840, step 16 |
| `custom_height` | Wird nur verwendet, wenn `size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein (nur GPT Image 2) (Standard: 1024) | INT | Nein | 1024 to 3840, step 16 |

**Parametereinschränkungen:**

- Wenn `image` bereitgestellt wird, verwendet der Node den Bildbearbeitungs-Endpunkt.
- `mask` kann nur verwendet werden, wenn `image` bereitgestellt wird.
- Bei Verwendung von `mask` werden nur einzelne Bilder unterstützt (Batch-Größe muss 1 sein).
- `mask` und `image` müssen dieselbe Größe haben.
- Benutzerdefinierte Auflösung (`size` = "Custom") wird nur vom Modell `gpt-image-2` unterstützt.
- Benutzerdefinierte Breite und Höhe müssen Vielfache von 16 sein.
- Die längste Kante einer benutzerdefinierten Auflösung darf höchstens 3840 betragen.
- Das Seitenverhältnis einer benutzerdefinierten Auflösung darf 3:1 nicht überschreiten.
- Die Gesamtpixelzahl einer benutzerdefinierten Auflösung muss zwischen 655.360 und 8.294.400 liegen.
- Die Modelle `gpt-image-1` und `gpt-image-1.5` unterstützen nur die Größen `auto`, `1024x1024`, `1024x1536` und `1536x1024`. Andere Größen werden nur vom Modell `gpt-image-2` unterstützt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Generiertes oder bearbeitetes Bild(er). Mehrere Bilder werden als Batch zurückgegeben; wenn die zurückgegebenen Bilder unterschiedliche Abmessungen haben, werden sie an die Größe des ersten Bildes angepasst. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/de.md)

---
**Source fingerprint (SHA-256):** `f0f0db7fd2cdf8efd2155522b289aa8f3f939fa79a6e9060b0ffbb2dd20efa1e`
