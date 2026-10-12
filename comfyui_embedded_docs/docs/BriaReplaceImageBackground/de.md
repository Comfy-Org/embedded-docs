# Bria Bildhintergrund ersetzen

Dieser Node ersetzt den Hintergrund eines Bildes durch einen neuen, von Bria generierten Hintergrund. Der neue Hintergrund kann mit einem Text-Prompt beschrieben oder durch Referenzbilder gesteuert werden. Die Pixel des Motivs bleiben erhalten, während der Hintergrund um sie herum generiert wird.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, dessen Hintergrund ersetzt wird. | IMAGE | Ja | |
| `background` | Beschreiben Sie den neuen Hintergrund mit einem Prompt oder steuern Sie ihn mit Referenzbildern. | DYNAMIC_COMBO | Ja | `"prompt"`<br>`"reference images"` |
| `original_quality` | Gibt die exakte Pixelgröße der Eingabe zurück, anstatt das Ergebnis auf etwa 1 Megapixel zu skalieren. Eine große Eingabe gibt dann ein großes Bild zurück. (Standard: false) | BOOLEAN | Nein | `true`<br>`false` |
| `seed` | Derselbe Seed liefert normalerweise denselben Hintergrund; die automatische Prompt-Verfeinerung kann ihn dennoch variieren. (Standard: 42) | INT | Nein | 0 bis 2147483647 |
| `moderation` | Moderationseinstellungen. (Standard: "false") | DYNAMIC_COMBO | Nein | `"false"`<br>`"true"` |

### Prompt-Eingaben

Wird angezeigt, wenn `background` auf `"prompt"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Beschreibung des neuen Hintergrunds. Ein Hex-Farbcode wie #FF5733 erzeugt einen einfarbigen Hintergrund. Muss mindestens 1 Zeichen lang sein. | STRING | Ja | |
| `mode` | `high_control` folgt dem Prompt am genauesten, `base` ist ein ausgewogener Standard und `fast` opfert Details für Geschwindigkeit. | COMBO | Ja | `"high_control"`<br>`"base"`<br>`"fast"` |
| `refine_prompt` | Schreibt den Prompt für bessere Ergebnisse neu, was auch nicht-englische Prompts übersetzt. Deaktivieren Sie dies, um den Prompt genau wie geschrieben zu senden. (Standard: true) | BOOLEAN | Nein | `true`<br>`false` |

### Referenzbild-Eingaben

Wird angezeigt, wenn `background` auf `"reference images"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `ref_images` | Erweiterbarer Slot: Verbinden Sie 1 bis 10 Bilder, die den neuen Hintergrund steuern; sie müssen nicht dieselbe Größe haben. Jede Referenz verändert das Ergebnis, daher sind wenige konsistente Referenzen besser als viele widersprüchliche. Eine gebatchte Eingabe zählt einmal pro Bild. | IMAGE | Ja | 1 bis 10 Bilder |
| `enhance_ref_images` | Zusätzliche Verarbeitung der Referenzbilder für bessere Ergebnisse. (Standard: true) | BOOLEAN | Nein | `true`<br>`false` |

### Moderationseingaben

Wird angezeigt, wenn `moderation` auf `"true"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Moderation für Prompt-Inhalte aktivieren. (Standard: false) | BOOLEAN | Nein | `true`<br>`false` |
| `visual_input_moderation` | Moderation für visuelle Eingabe aktivieren. (Standard: false) | BOOLEAN | Nein | `true`<br>`false` |
| `visual_output_moderation` | Moderation für visuelle Ausgabe aktivieren. (Standard: false) | BOOLEAN | Nein | `true`<br>`false` |

**Hinweis:** Die Eingabe `ref_images` akzeptiert maximal 10 Bilder; werden mehr als 10 bereitgestellt, wird ein Fehler zurückgegeben. Das Feld `prompt` muss mindestens 1 Zeichen enthalten. Wenn `original_quality` false ist, wird das Eingabebild vor der Verarbeitung auf etwa 1 Megapixel herunterskaliert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das Bild mit dem neuen Hintergrund. | IMAGE |
| `refined_prompt` | Der Prompt, auf dessen Grundlage Bria generiert hat; auf dem Referenzbild-Pfad leer. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceImageBackground/de.md)

---
**Source fingerprint (SHA-256):** `62c29d61983c9656d2ea2954518404c62d76961c3deba0e10d63e787d0b0b106`
