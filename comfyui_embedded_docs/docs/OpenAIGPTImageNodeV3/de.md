# OpenAI GPT Image 2.6

## Überblick

OpenAI GPT Image 2.6 erzeugt Bilder aus einem Prompt und bearbeitet sie, wenn Sie Referenzbilder verbinden, wobei die GPT Image-Modelle von OpenAI zum Einsatz kommen. Der Node bietet vier Modelle: `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` und `gpt-image-2.5-sunburst`. Zeichnen Sie Anmerkungen auf das erste Referenzbild und verbinden Sie diese als Markup-Paar, um dem Modell genau zu zeigen, wo bearbeitet werden soll.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu verwendende GPT Image-Modell. Bei Auswahl eines Modells werden die Parameter für dieses Modell eingeblendet. | DYNAMIC_COMBO | Ja | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"` |

### gpt-image-2.6-flare und gpt-image-2.6-sunburst Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-2.6-flare` oder `gpt-image-2.6-sunburst` gesetzt ist. Beide Modelle teilen dieselben Parameter.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.prompt` | Was generiert oder welche Bearbeitung vorgenommen werden soll. (Standard: `""`) | STRING | Ja | N/A |
| `model.size` | Bildgröße. Wählen Sie "Custom", um die benutzerdefinierte Breite und Höhe zu verwenden. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein. (Standard: `1024`) | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.custom_height` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein. (Standard: `1024`) | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.background` | Gibt das Bild mit oder ohne Hintergrund zurück. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Bildqualität. Höhere Stufen kosten mehr und dauern länger. (Standard: `"low"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Wie stark das Modell das Bild vor dem Rendern plant. (Standard: `"high"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Optionale Referenzbilder zum Bearbeiten. Bis zu 16. | AUTOGROW | Nein | 0 bis 16 |
| `model.markup` | Über das erste Referenzbild gezeichnete Anmerkungen, die zeigen, wo bearbeitet werden soll. Muss der Größe dieses Bildes entsprechen und zusammen mit `model.markup_alpha` verbunden werden. | IMAGE | Nein | N/A |
| `model.markup_alpha` | Weiß markiert die Anmerkungen in `model.markup`. Der MASK-Ausgang des Painter-Nodes passt direkt; eine Load Image-Maske benötigt zuvor Invert Mask. | MASK | Nein | N/A |
| `model.seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: `42`) | INT | Ja | 0 bis 2147483647 |

### gpt-image-2.5-flare und gpt-image-2.5-sunburst Eingaben

Diese Eingaben erscheinen, wenn `model` auf `gpt-image-2.5-flare` oder `gpt-image-2.5-sunburst` gesetzt ist. Sie entsprechen den 2.6-Modellen, mit der Ausnahme, dass `model.complexity` nicht angeboten wird.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.prompt` | Was generiert oder welche Bearbeitung vorgenommen werden soll. (Standard: `""`) | STRING | Ja | N/A |
| `model.size` | Bildgröße. Wählen Sie "Custom", um die benutzerdefinierte Breite und Höhe zu verwenden. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein. (Standard: `1024`) | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.custom_height` | Wird nur verwendet, wenn `model.size` auf "Custom" gesetzt ist. Muss ein Vielfaches von 16 sein. (Standard: `1024`) | INT | Nein | 480 bis 3840 (Schritt 16) |
| `model.background` | Gibt das Bild mit oder ohne Hintergrund zurück. (Standard: `"auto"`) | COMBO | Ja | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Bildqualität. Höhere Stufen kosten mehr und dauern länger. (Standard: `"low"`) | COMBO | Ja | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Optionale Referenzbilder zum Bearbeiten. Bis zu 16. | AUTOGROW | Nein | 0 bis 16 |
| `model.markup` | Über das erste Referenzbild gezeichnete Anmerkungen, die zeigen, wo bearbeitet werden soll. Muss der Größe dieses Bildes entsprechen und zusammen mit `model.markup_alpha` verbunden werden. | IMAGE | Nein | N/A |
| `model.markup_alpha` | Weiß markiert die Anmerkungen in `model.markup`. Der MASK-Ausgang des Painter-Nodes passt direkt; eine Load Image-Maske benötigt zuvor Invert Mask. | MASK | Nein | N/A |
| `model.seed` | Steuert, ob der Node erneut ausgeführt wird; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: `42`) | INT | Ja | 0 bis 2147483647 |

**Parametereinschränkungen und -beschränkungen:**

- Bei `model.size` auf "Custom" müssen sowohl `model.custom_width` als auch `model.custom_height` Vielfache von 16 sein, die längste Kante darf 3840 nicht überschreiten, das Seitenverhältnis darf 3:1 nicht überschreiten und die Gesamtpixelzahl muss zwischen 655.360 und 8.294.400 liegen.
- `model.markup` und `model.markup_alpha` müssen zusammen verbunden werden. Markup erfordert mindestens ein Referenzbild, und seine Breite und Höhe müssen mit dem ersten Referenzbild übereinstimmen.
- Ohne `model.images` generiert der Node Bilder allein aus dem Prompt; mit Referenzbildern bearbeitet und kombiniert er diese.
- Referenzbilder werden herunterskaliert, bevor sie an die API gesendet werden.
- `model.complexity` gibt es nur bei `gpt-image-2.6-flare` und `gpt-image-2.6-sunburst`; die 2.5-Modelle verwenden eine feste Planungstiefe.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das generierte Bild oder die generierten Bilder. Alle zurückgegebenen Bilder werden zu einem Batch zusammengefasst; wenn ihre Abmessungen voneinander abweichen, werden sie an das erste Bild angepasst. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV3/de.md)

---
**Source fingerprint (SHA-256):** `33f5d91af56c215cc7f7c704f9b123fe1c35bf287012072b818b76b551c04667`
