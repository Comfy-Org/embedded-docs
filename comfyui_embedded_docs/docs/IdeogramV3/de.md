# IdeogramV3

Der Ideogram V3-Node erzeugt Bilder mit dem Ideogram V3-Modell. Er unterstützt sowohl die reguläre Bilderzeugung aus Text-Prompts als auch die Bildbearbeitung, wenn sowohl ein Bild als auch eine Maske bereitgestellt werden. Der Node bietet verschiedene Steuerungsmöglichkeiten für Seitenverhältnis, Auflösung, Generierungsgeschwindigkeit und optionale Charakter-Referenzbilder.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt für die Bilderzeugung oder Bildbearbeitung (Standard: leer) | STRING | Ja | - |
| `image` | Optionales Referenzbild für die Bildbearbeitung | IMAGE | Nein | - |
| `mask` | Optionale Maske für Inpainting (weiße Bereiche werden ersetzt) | MASK | Nein | - |
| `aspect_ratio` | Das Seitenverhältnis für die Bilderzeugung. Wird ignoriert, wenn `resolution` nicht auf Auto gesetzt ist (Standard: "1:1") | COMBO | Nein | "1:1"<br>"1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4" |
| `resolution` | Die Auflösung für die Bilderzeugung. Wenn nicht auf Auto gesetzt, überschreibt dies die Einstellung `aspect_ratio` (Standard: "Auto") | COMBO | Nein | "Auto"<br>"512x1536"<br>"576x1408"<br>"576x1472"<br>"576x1536"<br>"640x1344"<br>"640x1408"<br>"640x1472"<br>"640x1536"<br>"704x1152"<br>"704x1216"<br>"704x1280"<br>"704x1344"<br>"704x1408"<br>"704x1472"<br>"736x1312"<br>"768x1088"<br>"768x1216"<br>"768x1280"<br>"768x1344"<br>"800x1280"<br>"832x960"<br>"832x1024"<br>"832x1088"<br>"832x1152"<br>"832x1216"<br>"832x1248"<br>"864x1152"<br>"896x960"<br>"896x1024"<br>"896x1088"<br>"896x1120"<br>"896x1152"<br>"960x832"<br>"960x896"<br>"960x1024"<br>"960x1088"<br>"1024x832"<br>"1024x896"<br>"1024x960"<br>"1024x1024"<br>"1088x768"<br>"1088x832"<br>"1088x896"<br>"1088x960"<br>"1120x896"<br>"1152x704"<br>"1152x832"<br>"1152x864"<br>"1152x896"<br>"1216x704"<br>"1216x768"<br>"1216x832"<br>"1248x832"<br>"1280x704"<br>"1280x768"<br>"1280x800"<br>"1312x736"<br>"1344x640"<br>"1344x704"<br>"1344x768"<br>"1408x576"<br>"1408x640"<br>"1408x704"<br>"1472x576"<br>"1472x640"<br>"1472x704"<br>"1536x512"<br>"1536x576"<br>"1536x640" |
| `magic_prompt_option` | Legt fest, ob MagicPrompt bei der Generierung verwendet werden soll (Standard: "AUTO") | COMBO | Nein | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Zufälliger Seed für die Generierung (Standard: 0) | INT | Nein | 0-2147483647 |
| `num_images` | Anzahl der zu generierenden Bilder (Standard: 1) | INT | Nein | 1-8 |
| `rendering_speed` | Steuert den Kompromiss zwischen Generierungsgeschwindigkeit und Qualität (Standard: "DEFAULT") | COMBO | Nein | "DEFAULT"<br>"TURBO"<br>"QUALITY" |
| `character_image` | Bild, das als Charakter-Referenz verwendet werden soll | IMAGE | Nein | - |
| `character_mask` | Optionale Maske für das Charakter-Referenzbild | MASK | Nein | - |

**Parametereinschränkungen:**

- Wenn sowohl `image` als auch `mask` bereitgestellt werden, wechselt der Node in den Bearbeitungsmodus
- Wenn nur eines von `image` oder `mask` bereitgestellt wird, tritt ein Fehler auf
- `character_mask` erfordert, dass `character_image` vorhanden ist
- Der Parameter `aspect_ratio` wird ignoriert, wenn `resolution` nicht auf "Auto" gesetzt ist
- Weiße Bereiche in der Maske werden beim Inpainting ersetzt
- Charakter-Maske und Charakter-Bild müssen dieselbe Größe haben

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Die generierten oder bearbeiteten Bilder | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/de.md)

---
**Source fingerprint (SHA-256):** `d5005a9cdbdad79762dfd24eaa73e6c293d28b72813e96883ecdfccb8339ca75`
