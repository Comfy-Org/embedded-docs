# OpenAI GPT Image 2.5

Dieser Node generiert Bilder mithilfe der GPT Image API von OpenAI. Er unterstützt fünf Modelle – `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` und `gpt-image-1` –, ermöglicht das Anhängen von Referenzbildern für die Bildbearbeitung und kann eine Maske verwenden, um anzugeben, welche Teile eines Bildes ersetzt werden sollen.

## Eingaben

### Gemeinsame Eingaben

Diese Eingaben sind immer sichtbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu verwendende OpenAI GPT Image-Modell. Wenn Sie ein Modell auswählen, werden zusätzliche Parameter angezeigt, die für dieses Modell spezifisch sind. | DYNAMIC_COMBO | Ja | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Text-Prompt für GPT Image (Standard: `""`). | STRING | Ja | N/A |
| `n` | Wie viele Bilder generiert werden sollen (Standard: `1`). | INT | Ja | 1 bis 8 |
| `seed` | Seed für Reproduzierbarkeit (Standard: `0`). Noch nicht im Backend implementiert. | INT | Ja | 0 bis 2147483647 |

### gpt-image-2.5-flare und gpt-image-2.5-sunburst Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-2.5-flare` oder `gpt-image-2.5-sunburst` gesetzt ist. Beide Modelle verwenden denselben Parametersatz.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.size` | Bildgröße. Wählen Sie „Custom“, um die benutzerdefinierte Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Wird nur verwendet, wenn `model.size` auf „Custom“ gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.custom_height` | Wird nur verwendet, wenn `model.size` auf „Custom“ gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.background` | Bild mit oder ohne Hintergrund zurückgeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Bildqualität; beeinflusst Kosten und Generierungszeit (Standard: `"low"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Optionale Referenzbilder für die Bildbearbeitung. Bis zu 16 Bilder. Siehe Referenzeingaben für Details. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/A |

### gpt-image-2 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-2` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.size` | Bildgröße. Wählen Sie „Custom“, um die benutzerdefinierte Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Wird nur verwendet, wenn `model.size` auf „Custom“ gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.custom_height` | Wird nur verwendet, wenn `model.size` auf „Custom“ gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.background` | Bild mit oder ohne Hintergrund zurückgeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"` |
| `model.quality` | Bildqualität; beeinflusst Kosten und Generierungszeit (Standard: `"low"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Optionale Referenzbilder für die Bildbearbeitung. Bis zu 16 Bilder. Siehe Referenzeingaben für Details. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/A |

### gpt-image-1.5 und gpt-image-1 Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-1.5` oder `gpt-image-1` gesetzt ist. Beide Modelle verwenden denselben Parametersatz.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.size` | Bildgröße (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Bild mit oder ohne Hintergrund zurückgeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Bildqualität; beeinflusst Kosten und Generierungszeit (Standard: `"low"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Optionale Referenzbilder für die Bildbearbeitung. Bis zu 16 Bilder. Siehe Referenzeingaben für Details. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/A |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.images` | Erweiterbarer Slot: 1..N Elemente verbinden (z. B. `image_1`...`image_16`); bis zu 16 Referenzbilder für alle Modelle. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/A |

**Parametereinschränkungen und Limitierungen:**

- Wenn `model.size` auf „Custom“ gesetzt ist (nur `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` und `gpt-image-2`), müssen `model.custom_width` und `model.custom_height` beide Vielfache von 16 sein, die längste Kante darf 3840 nicht überschreiten, das Seitenverhältnis darf 3:1 nicht überschreiten und die Gesamtpixelzahl muss zwischen 655.360 und 8.294.400 liegen.
- `model.mask` erfordert genau ein Referenzbild in `model.images`: Es kann nicht ohne Bild verwendet werden, und es kann nicht mit mehr als einem Bild verwendet werden.
- Wenn `model.mask` verwendet wird, müssen seine Höhe und Breite mit der Höhe und Breite des Referenzbilds übereinstimmen.
- Wenn `model.images` bereitgestellt wird, läuft der Node im Bildbearbeitungsmodus; ohne `model.images` generiert er Bilder nur anhand des Prompts.
- Referenzbilder und die Maske werden herunterskaliert, bevor sie an die API gesendet werden.
- Die Qualitätsstufen `"xhigh"` und `"max"` sind nur für `gpt-image-2.5-flare` und `gpt-image-2.5-sunburst` verfügbar.
- `seed` ist derzeit nicht im Backend implementiert.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das generierte Bild oder die generierten Bilder. Alle zurückgegebenen Bilder werden zu einem Batch gestapelt; wenn ihre Abmessungen abweichen, werden sie auf die Größe des ersten Bildes skaliert. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `9cf1a9fa3e2cd98aff6c42432164ac5e6c55b7bcdc9815043cb359c6968ac172`
