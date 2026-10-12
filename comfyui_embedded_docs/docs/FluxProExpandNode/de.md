# FluxProExpandNode

Erweitert ein Bild per Outpainting basierend auf dem Prompt. Dieser Node erweitert ein Bild, indem er Pixel oben, unten, links und rechts hinzufügt, während er neuen Inhalt generiert, der der angegebenen Textbeschreibung entspricht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Eingabebild, das erweitert werden soll | IMAGE | Ja | - |
| `prompt` | Prompt für die Bildgenerierung (Standard: "") | STRING | Nein | - |
| `prompt_upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung verändert, die Ergebnisse sind jedoch nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: False) | BOOLEAN | Nein | - |
| `top` | Anzahl der Pixel, um die das Bild oben erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `bottom` | Anzahl der Pixel, um die das Bild unten erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `left` | Anzahl der Pixel, um die das Bild links erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `right` | Anzahl der Pixel, um die das Bild rechts erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `guidance` | Guidance-Stärke für den Bildgenerierungsprozess (Standard: 60) | FLOAT | Nein | 1.5-100 |
| `steps` | Anzahl der Schritte für den Bildgenerierungsprozess (Standard: 50) | INT | Nein | 15-50 |
| `seed` | Der Zufalls-Seed, der zur Erzeugung des Rauschens verwendet wird. (Standard: 0) | INT | Nein | 0-18446744073709551615 |

## Ausgaben

| Output Name | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das erweiterte Ausgabebild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/de.md)

---
**Source fingerprint (SHA-256):** `faff1e1311a3208066a499a358923c6e335ea1785baeafe3761484641f7f12d6`
