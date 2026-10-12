# Qwen Image 3 bearbeiten

Dieser Node verwendet die Qwen-Image 3.0-Modelle, um bis zu 3 Referenzbilder anhand eines Text-Prompts zu bearbeiten oder zu kombinieren. Sie wählen ein Modell aus, geben den Prompt und die Referenzbilder an, und der Node gibt ein oder mehrere generierte Bilder zurück.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Modell zur Verwendung. Diese Auswahl umfasst auch den Text-Prompt, bis zu 3 Referenzbild-Eingaben und einen optionalen negativen Prompt. | DYNAMIC_COMBO | Ja | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Ausgabeauflösung. "match input" verwendet die Größe des ersten Referenzbilds erneut, "auto" lässt das Modell eine Größe mit demselben Seitenverhältnis wählen, "custom" legt eine explizite Breite und Höhe fest. | DYNAMIC_COMBO | Ja | "match input"<br>"auto"<br>"custom" |
| `n` | Anzahl der zu generierenden Bilder, zurückgegeben als Batch. (Standard: 1) | INT | Nein | 1 bis 6 |
| `seed` | Seed für die Generierung. (Standard: 42) | INT | Nein | 0 bis 2147483647 |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung erweitert werden soll. (Standard: True) | BOOLEAN | Nein | True<br>False |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll. (Standard: False) | BOOLEAN | Nein | True<br>False |

### qwen-image-3.0-pro und qwen-image-3.0 Eingaben

Beide Modelle verwenden dieselben Unterparameter.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Bearbeitungsanweisungen. Unterstützt Englisch und Chinesisch sowie @Image1-artige Referenzen auf die Eingabebilder. (Standard: "") | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll. (Standard: "") | STRING | Nein | - |

### Referenzeingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `images` | Erweiterbarer Slot: Verbinden Sie 1 bis 3 Referenzbilder (`image_1`, `image_2`, `image_3`). Verweisen Sie im Prompt mit @Image1, @Image2, @Image3 darauf, nummeriert in Eingabereihenfolge; eine Batch-Eingabe zählt einmal pro Bild. | IMAGE | Ja | 1 bis 3 |

### Eingaben für benutzerdefinierte Größe

Wird angezeigt, wenn `size` auf "custom" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `width` | Ausgabebreite. Die gesamte Pixelanzahl muss zwischen 512x512 und 2560x2560 liegen; jedes Seitenverhältnis innerhalb dieses Bereichs ist möglich. (Standard: 1024) | INT | Ja (wenn `size` den Wert "custom" hat) | 256 bis 2560, Schrittweite 16 |
| `height` | Ausgabehöhe. Die gesamte Pixelanzahl muss zwischen 512x512 und 2560x2560 liegen; jedes Seitenverhältnis innerhalb dieses Bereichs ist möglich. (Standard: 1024) | INT | Ja (wenn `size` den Wert "custom" hat) | 256 bis 2560, Schrittweite 16 |

### Einschränkungen

- Der Text-Prompt ist erforderlich und muss mindestens ein Zeichen enthalten.
- Maximal 3 Referenzbilder werden unterstützt; bei mehr wird ein Fehler ausgelöst (eine Batch-Eingabe zählt einmal pro Bild).
- Wenn `size` auf "custom" gesetzt ist, müssen explizite Werte für Breite und Höhe angegeben werden, die validiert werden: Die gesamte Pixelanzahl muss zwischen 262.144 (512x512) und 6.553.600 (2560x2560) Pixeln liegen, und das Seitenverhältnis muss zwischen 1:8 und 8:1 liegen.
- Wenn `size` auf "match input" gesetzt ist, ist mindestens ein Referenzbild erforderlich, da die Abmessungen des ersten Referenzbilds verwendet werden; die Abmessungen werden skaliert, um in den unterstützten Bereich und Seitenverhältnisbereich zu passen.
- Wenn `size` auf "auto" gesetzt ist, wählt das Modell die Ausgabegröße (1,9–4,2 Megapixel) unter Beibehaltung des Eingabeseitenverhältnisses.
- Prompt-Referenzen verwenden @Image1, @Image2, @Image3, nummeriert in Eingabereihenfolge; eine Referenz auf einen Index, der höher als die Anzahl der verbundenen Bilder ist, löst einen Fehler aus. Tags werden nur an Wortgrenzen erkannt, daher bleiben Adressen wie user@image1.com unverändert.
- Eingabe-Referenzbilder werden auf höchstens 2048x2048 Pixel herunterskaliert, bevor sie an die API gesendet werden. Wenn die PNG-Kodierung das API-Größenlimit überschreitet, wird stattdessen eine JPEG-Kodierung verwendet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `IMAGE` | Das oder die generierten Bilder, zurückgegeben als Batch. Es werden bis zu `n` Bilder zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/de.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
