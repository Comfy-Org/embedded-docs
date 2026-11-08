# Grok Image Edit

Ändert ein oder mehrere vorhandene Bilder basierend auf einem Text-Prompt. Der Node sendet die verbundenen Referenzbilder und den Prompt unter Verwendung des ausgewählten Modells an die Grok-Bildbearbeitungs-API und gibt anschließend die bearbeiteten Bilder zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Das zu verwendende Grok-Bildmodell. Die unten angezeigten Unterparameter ändern sich je nach ausgewähltem Modell. | DYNAMIC_COMBO | Ja | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Der Text-Prompt, der zum Generieren des Bildes verwendet wird. (Standard: "") | STRING | Ja | N/A |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Ja | 0 bis 2147483647 |

**Hinweis:** `grok-imagine-image-quality` und `grok-imagine-image-pro` wurden von xAI eingestellt und laufen jetzt als `grok-imagine-image-2.0` mit niedriger Qualität.

### grok-imagine-image-2.0 Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `resolution` | Ausgabeauflösung der bearbeiteten Bilder. | COMBO | Ja | "1K"<br>"2K" |
| `number_of_images` | Anzahl der zu generierenden bearbeiteten Bilder. (Standard: 1) | INT | Ja | 1 bis 10 |
| `quality` | Qualitätsstufe der generierten Bilder. | COMBO | Ja | "medium"<br>"low" |
| `aspect_ratio` | Seitenverhältnis des bearbeiteten Bildes. (Standard: "auto") | COMBO | Ja | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `resolution` | Ausgabeauflösung der bearbeiteten Bilder. | COMBO | Ja | "1K"<br>"2K" |
| `number_of_images` | Anzahl der zu generierenden bearbeiteten Bilder. (Standard: 1) | INT | Ja | 1 bis 10 |
| `aspect_ratio` | Seitenverhältnis des bearbeiteten Bildes. (Standard: "auto") | COMBO | Ja | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `resolution` | Ausgabeauflösung der bearbeiteten Bilder. | COMBO | Ja | "1K"<br>"2K" |
| `number_of_images` | Anzahl der zu generierenden bearbeiteten Bilder. (Standard: 1) | INT | Ja | 1 bis 10 |
| `aspect_ratio` | Nur erlaubt, wenn mehrere Bilder verbunden sind. (Standard: "auto") | COMBO | Ja | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `resolution` | Ausgabeauflösung der bearbeiteten Bilder. | COMBO | Ja | "1K"<br>"2K" |
| `number_of_images` | Anzahl der zu generierenden bearbeiteten Bilder. (Standard: 1) | INT | Ja | 1 bis 10 |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `images` | Erweiterbarer Slot: Verbinden Sie 1 bis N Referenzbilder zum Bearbeiten. Die Slots verwenden die Vorlagennamen `image_1`, `image_2`, `image_3`; die maximale Anzahl der Slots hängt vom ausgewählten Modell ab. | IMAGE | Ja | 1 Bild für `grok-imagine-image-pro`<br>1 bis 3 Bilder für `grok-imagine-image-2.0`, `grok-imagine-image-quality` und `grok-imagine-image` |

**Hinweis zu Einschränkungen:**
- `prompt` muss mindestens ein Zeichen enthalten, das kein Leerzeichen ist.
- Für die Bearbeitung ist mindestens ein Referenzbild erforderlich; der Node löst einen Fehler aus, wenn kein Bild verbunden ist.
- Die maximale Anzahl an Eingabebildern beträgt 1 für `grok-imagine-image-pro` und 3 für `grok-imagine-image-2.0`, `grok-imagine-image-quality` und `grok-imagine-image`. Das Verbinden von mehr Bildern, als das Modell unterstützt, löst einen Fehler aus.
- Das Bildlimit zählt jedes Bild in den verbundenen Eingaben; ein Batch mit mehreren Bildern zählt daher als mehrere Bilder für das Limit.
- Für `grok-imagine-image` ist ein benutzerdefiniertes `aspect_ratio` (alles außer "auto") nur erlaubt, wenn mehrere Bilder verbunden sind. Bei einem einzelnen Bild muss `aspect_ratio` "auto" sein.
- Für `grok-imagine-image-2.0` und `grok-imagine-image-quality` kann `aspect_ratio` auch bei einem einzelnen Bild frei festgelegt werden.
- Der Unterparameter `quality` ist nur mit `grok-imagine-image-2.0` verfügbar.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
|------------------|--------------|----------|
| `IMAGE` | Das/die von der Grok-API zurückgegebenen bearbeiteten Bild(er). Wenn ein einzelnes Bild generiert wird, wird es direkt zurückgegeben. Wenn mehrere Bilder generiert werden, werden sie zu einem einzelnen Batch-Tensor zusammengefügt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/de.md)

---
**Source fingerprint (SHA-256):** `b8f4a86a3dd3a9cf1a24531fad4c62642e4c6de75a598fbe263ff8d3d16800d5`
