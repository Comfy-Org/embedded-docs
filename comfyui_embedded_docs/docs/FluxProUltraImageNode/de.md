# Flux 1.1 [pro] Ultra Image

Erzeugt Bilder mit Flux Pro 1.1 Ultra über eine API basierend auf Prompt und Auflösung. Dieser Node verbindet sich mit einem externen Dienst, um Bilder gemäß Ihrer Textbeschreibung und den angegebenen Dimensionen zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `prompt` | Prompt für die Bilderzeugung (Standard: leerer String) | STRING | Ja | - |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung verändert, aber die Ergebnisse sind nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: False) | BOOLEAN | Nein | - |
| `seed` | Der Zufalls-Seed, der zur Erzeugung des Rauschens verwendet wird. (Standard: 0) | INT | Nein | 0 bis 18446744073709551615 |
| `aspect_ratio` | Seitenverhältnis des Bildes; muss zwischen 1:4 und 4:1 liegen. (Standard: "16:9") | STRING | Nein | - |
| `raw` | Wenn True, werden weniger verarbeitete, natürlicher wirkende Bilder erzeugt. (Standard: False) | BOOLEAN | Nein | - |
| `image_prompt` | Optionales Referenzbild zur Steuerung der Generierung | IMAGE | Nein | - |
| `image_prompt_strength` | Mischung zwischen dem Prompt und dem Bild-Prompt. (Standard: 0.1) | FLOAT | Nein | 0.0 bis 1.0 |

**Hinweis:** Der Parameter `aspect_ratio` muss zwischen 1:4 und 4:1 liegen. Wenn `image_prompt` bereitgestellt wird, wird `image_prompt_strength` aktiv und steuert, wie stark das Referenzbild die endgültige Ausgabe beeinflusst. Wenn `image_prompt` nicht bereitgestellt wird, wird der Parameter `prompt` validiert, um sicherzustellen, dass er nicht leer ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output_image` | Das von Flux Pro 1.1 Ultra erzeugte Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/de.md)

---
**Source fingerprint (SHA-256):** `6c9292ea666055ccd309d9e5d6d7cf8985f7b8f1e1faeda1e961b429b249f494`
