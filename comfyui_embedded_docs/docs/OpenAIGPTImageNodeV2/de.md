# OpenAI GPT Image 2.6

Dieser Node erzeugt Bilder mithilfe der OpenAI GPT Image API. Er unterstützt sechs Modelle – `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2` und `gpt-image-1.5` –, ermöglicht das Anhängen von Referenzbildern zur Bildbearbeitung und kann eine Maske verwenden, um festzulegen, welche Bildbereiche ersetzt werden sollen.

## Eingaben

### Gemeinsame Eingaben

Diese Eingaben sind immer sichtbar.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu verwendende OpenAI GPT Image-Modell. Bei Auswahl eines Modells werden zusätzliche Parameter angezeigt, die für dieses Modell spezifisch sind. | DYNAMIC_COMBO | Ja | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"` |
| `Prompt` | Textaufforderung für GPT Image (Standard: `""`). | STRING | Ja | N/V |
| `n` | Anzahl der zu erzeugenden Bilder (Standard: `1`). | INT | Ja | 1 bis 8 |
| `seed` | Seed für die Reproduzierbarkeit (Standard: `0`). Im Backend noch nicht implementiert. | INT | Ja | 0 bis 2147483647 |

### gpt-image-2.6-flare- und gpt-image-2.6-sunburst-Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-2.6-flare` oder `gpt-image-2.6-sunburst` gesetzt ist. Beide Modelle verwenden denselben Parametersatz.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `size` | Bildgröße. Wählen Sie "Custom", um die benutzerdefinierte Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `custom_width` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `custom_height` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `background` | Bild mit oder ohne Hintergrund zurückgeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `quality` | Bildqualität, beeinflusst Kosten und Generierungszeit (Standard: `"low"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Optionales Referenzbild bzw. optionale Referenzbilder für die Bildbearbeitung. Bis zu 16 Bilder. Details siehe Referenzeingaben. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/V |
| `model.complexity` | Wie stark das Modell das Bild vor dem Rendern plant. Niedrigere Werte liefern schneller Ergebnisse, höhere Werte planen intensiver. Standard: `"high"`. | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-2-Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-2` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `size` | Bildgröße. Wählen Sie "Custom", um die benutzerdefinierte Breite und Höhe zu verwenden (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `custom_width` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `custom_height` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein (Standard: `1024`). | INT | Nein | 480 bis 3840 (Schritt 16) |
| `background` | Bild mit oder ohne Hintergrund zurückgeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"` |
| `quality` | Bildqualität, beeinflusst Kosten und Generierungszeit (Standard: `"low"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Optionales Referenzbild bzw. optionale Referenzbilder für die Bildbearbeitung. Bis zu 16 Bilder. Details siehe Referenzeingaben. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/V |

### gpt-image-1.5-Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-1.5` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `size` | Bildgröße (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `background` | Bild mit oder ohne Hintergrund zurückgeben (Standard: `"auto"`). | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `quality` | Bildqualität, beeinflusst Kosten und Generierungszeit (Standard: `"low"`). | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Optionales Referenzbild bzw. optionale Referenzbilder für die Bildbearbeitung. Bis zu 16 Bilder. Details siehe Referenzeingaben. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/V |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.images` | Erweiterbarer Slot: 1..N Elemente verbinden (z. B. `image_1`...`image_16`); bis zu 16 Referenzbilder für alle Modelle. | IMAGE | Nein | 0 bis 16 |
| `model.mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt). Erfordert genau ein Referenzbild. | MASK | Nein | N/V |

**Parametereinschränkungen und -beschränkungen:**

- Wenn `model.size` auf "Custom" gesetzt ist (nur `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` und `gpt-image-2`), müssen `model.custom_width` und `model.custom_height` beide Vielfache von 16 sein, die längste Kante darf 3840 nicht überschreiten, das Seitenverhältnis darf 3:1 nicht überschreiten und die Gesamtpixelzahl muss zwischen 655.360 und 8.294.400 liegen.
- `model.mask` erfordert genau ein Referenzbild in `model.images`: Es kann nicht ohne Bild verwendet werden und auch nicht mit mehr als einem Bild.
- Wenn `model.mask` verwendet wird, müssen Höhe und Breite der Maske mit Höhe und Breite des Referenzbildes übereinstimmen.
- Wenn `model.images` angegeben ist, läuft der Node im Bildbearbeitungsmodus; ohne `model.images` werden Bilder allein anhand der Aufforderung erzeugt.
- Referenzbilder und die Maske werden vor dem Senden an die API herunterskaliert.
- Die Qualitätsstufen `"xhigh"` und `"max"` sind nur für `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` und `gpt-image-2.5-sunburst` verfügbar.
- `model.complexity` ist nur für `gpt-image-2.6-flare` und `gpt-image-2.6-sunburst` verfügbar; die anderen Modelle verwenden eine feste Planungstiefe.
- `seed` ist derzeit im Backend nicht implementiert.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das bzw. die erzeugten Bilder. Alle zurückgegebenen Bilder werden zu einem Batch zusammengefasst; wenn ihre Abmessungen abweichen, werden sie an die Abmessungen des ersten Bildes angepasst. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `effc65978ac1cca52a8d8c85230784c23c9eb2afffd7f057aba9f9627e784a15`
