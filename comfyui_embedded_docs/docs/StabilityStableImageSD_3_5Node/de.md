# StabilityStableImageSD_3_5Node

Dieser Node generiert Bilder synchron mit dem Stable Diffusion 3.5-Modell von Stability AI. Er erstellt Bilder basierend auf Text-Prompts und kann auch vorhandene Bilder ändern, wenn sie als Eingabe bereitgestellt werden. Der Node unterstützt verschiedene Seitenverhältnisse und Stil-Presets, um die Ausgabe anzupassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Was Sie im Ausgabebild sehen möchten. Ein starker, beschreibender Prompt, der Elemente, Farben und Motive klar definiert, führt zu besseren Ergebnissen. (Standard: leerer String) | STRING | Ja | - |
| `model` | Das für die Generierung zu verwendende Stable Diffusion 3.5-Modell. | COMBO | Ja | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` |
| `aspect_ratio` | Seitenverhältnis des generierten Bildes. (Standard: 1:1) | COMBO | Ja | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` |
| `style_preset` | Optionaler gewünschter Stil des generierten Bildes. Wählen Sie "None" für keinen Stil-Preset. | COMBO | Nein | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` |
| `cfg_scale` | Wie streng der Diffusionsprozess dem Prompt-Text folgt (höhere Werte halten Ihr Bild näher an Ihrem Prompt). (Standard: 4.0) | FLOAT | Ja | 1.0 bis 10.0 |
| `seed` | Der Zufallsstartwert (Seed), der zum Erzeugen des Rauschens verwendet wird. (Standard: 0) | INT | Ja | 0 bis 4294967294 |
| `image` | Optionales Eingabebild für die Bild-zu-Bild-Generierung. Wenn es bereitgestellt wird, wechselt der Node in den Bild-zu-Bild-Modus und der Parameter `aspect_ratio` wird ignoriert. | IMAGE | Nein | - |
| `negative_prompt` | Schlüsselwörter für das, was Sie im Ausgabebild nicht sehen möchten. Dies ist eine erweiterte Funktion. (Standard: leerer String) | STRING | Nein | - |
| `image_denoise` | Denoise-Stärke des Eingabebilds; 0.0 ergibt ein Bild, das mit der Eingabe identisch ist, 1.0 ist, als wäre kein Bild bereitgestellt worden. (Standard: 0.5) Dieser Parameter wird nur verwendet, wenn ein `image` bereitgestellt wird. | FLOAT | Nein | 0.0 bis 1.0 |

**Hinweis:** Wenn ein `image` bereitgestellt wird, wechselt der Node in den Bild-zu-Bild-Generierungsmodus und der Parameter `aspect_ratio` wird automatisch aus dem Eingabebild bestimmt. Wenn kein `image` bereitgestellt wird, wird der Parameter `image_denoise` ignoriert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das generierte oder modifizierte Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/de.md)

---
**Source fingerprint (SHA-256):** `0ef029d4651fb4a9132899a6df1a2c2de6152dd9091129573f366a2aac39bbae`
