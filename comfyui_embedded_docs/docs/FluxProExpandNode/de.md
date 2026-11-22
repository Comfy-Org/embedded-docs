# Flux.1 Bild erweitern

Erweitert ein Bild per Outpainting basierend auf dem Prompt. Dieser Node erweitert ein Bild, indem er Pixel oben, unten, links und rechts hinzufügt, während er neuen Inhalt generiert, der der angegebenen Textbeschreibung entspricht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Bild` | Das Eingabebild, das erweitert werden soll | IMAGE | Ja | - |
| `Prompt` | Prompt für die Bildgenerierung (Standard: "") | STRING | Nein | - |
| `Prompt-Upsampling` | Ob ein Upsampling des Prompts durchgeführt werden soll. Wenn aktiviert, wird der Prompt automatisch für eine kreativere Generierung verändert, die Ergebnisse sind jedoch nicht deterministisch (derselbe Seed erzeugt nicht exakt dasselbe Ergebnis). (Standard: False) | BOOLEAN | Nein | - |
| `Oben` | Anzahl der Pixel, um die das Bild oben erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `Unten` | Anzahl der Pixel, um die das Bild unten erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `Links` | Anzahl der Pixel, um die das Bild links erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `Rechts` | Anzahl der Pixel, um die das Bild rechts erweitert wird (Standard: 0) | INT | Nein | 0-2048 |
| `Guidance` | Guidance-Stärke für den Bildgenerierungsprozess (Standard: 60) | FLOAT | Nein | 1.5-100 |
| `Schritte` | Anzahl der Schritte für den Bildgenerierungsprozess (Standard: 50) | INT | Nein | 15-50 |
| `Seed` | Der Zufalls-Seed, der zur Erzeugung des Rauschens verwendet wird. (Standard: 0) | INT | Nein | 0-18446744073709551615 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das erweiterte Ausgabebild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/de.md)

---
**Source fingerprint (SHA-256):** `faff1e1311a3208066a499a358923c6e335ea1785baeafe3761484641f7f12d6`
