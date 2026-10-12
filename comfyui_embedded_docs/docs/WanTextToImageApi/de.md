# Wan Text zu Bild

Der Wan Text to Image-Node generiert Bilder auf Grundlage von Textbeschreibungen. Er verwendet KI-Modelle, um visuelle Inhalte aus geschriebenen Prompts zu erstellen, und unterstützt sowohl englische als auch chinesische Texteingaben. Der Node bietet verschiedene Steuerelemente, um Bildgröße, Qualität und Stilvorgaben der Ausgabe anzupassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model` | Zu verwendendes Modell (Standard: "wan2.5-t2i-preview") | STRING | Ja | "wan2.5-t2i-preview" |
| `prompt` | Prompt, der die Elemente und visuellen Merkmale beschreibt. Unterstützt Englisch und Chinesisch (Standard: leer) | STRING | Ja | - |
| `negative_prompt` | Negativer Prompt, der beschreibt, was vermieden werden soll (Standard: leer) | STRING | Nein | - |
| `width` | Bildbreite in Pixeln (Standard: 1024, Schritt: 32) | INT | Nein | 768-1440 |
| `height` | Bildhöhe in Pixeln (Standard: 1024, Schritt: 32) | INT | Nein | 768-1440 |
| `seed` | Seed, der für die Generierung verwendet wird (Standard: 0) | INT | Nein | 0-2147483647 |
| `prompt_extend` | Ob der Prompt mit KI-Unterstützung erweitert werden soll (Standard: True) | BOOLEAN | Nein | - |
| `watermark` | Ob dem Ergebnis ein KI-generiertes Wasserzeichen hinzugefügt werden soll (Standard: False) | BOOLEAN | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `output` | Das basierend auf dem Text-Prompt generierte Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/de.md)

---
**Source fingerprint (SHA-256):** `208b7c839da45316aeb1a14a3e9d176eeb09b2f931f764fb8a296da15ae3bd4e`
