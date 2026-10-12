# MagnificImageStyleTransferNode

Dieser Node wendet den visuellen Stil eines Referenzbildes auf Ihr Eingabebild an. Er verwendet einen externen KI-Dienst zur Verarbeitung der Bilder, sodass Sie die Stärke der Stilübertragung und die Beibehaltung der Struktur des Originalbildes steuern können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, auf das die Stilübertragung angewendet werden soll. | IMAGE | Ja | - |
| `reference_image` | Das Referenzbild, aus dem der Stil extrahiert wird. | IMAGE | Ja | - |
| `prompt` | Ein optionaler Text-Prompt zur Steuerung der Stilübertragung. | STRING | Nein | - |
| `style_strength` | Prozentsatz der Stilstärke (Standard: 100). | INT | Nein | 0 to 100 |
| `structure_strength` | Behält die Struktur des Originalbildes bei (Standard: 50). | INT | Nein | 0 to 100 |
| `flavor` | Variante der Stilübertragung. | COMBO | Nein | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | Auswahl der Verarbeitungs-Engine. | COMBO | Nein | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | Porträtmodus für Gesichtsverbesserungen aktivieren. | COMBO | Nein | "disabled"<br>"enabled" |
| `portrait_style` | Visueller Stil, der auf Porträtbilder angewendet wird. Diese Eingabe ist nur verfügbar, wenn `portrait_mode` auf "enabled" gesetzt ist. | COMBO | Nein | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | Intensität der Gesichtsverschönerung bei Porträts. Diese Eingabe ist nur verfügbar, wenn `portrait_mode` auf "enabled" gesetzt ist. | COMBO | Nein | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | Wenn deaktiviert, bringt jede Generierung ein gewisses Maß an Zufälligkeit mit sich, was zu vielfältigeren Ergebnissen führt (Standard: True). | BOOLEAN | Nein | - |

**Einschränkungen:**

* Es sind genau ein `image` und ein `reference_image` erforderlich.
* Beide Bilder müssen ein Seitenverhältnis zwischen 1:3 und 3:1 haben.
* Beide Bilder müssen eine Mindesthöhe und Mindestbreite von 160 Pixeln aufweisen.
* Die Parameter `portrait_style` und `portrait_beautifier` sind nur aktiv, wenn `portrait_mode` auf "enabled" gesetzt ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das resultierende Bild nach Anwendung der Stilübertragung. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/de.md)

---
**Source fingerprint (SHA-256):** `edffec024ebe7cbf7c42008e14c1b99d6fafcf5b9da62b0b560d194a585dc9ad`
