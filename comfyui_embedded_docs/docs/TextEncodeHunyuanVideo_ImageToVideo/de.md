# TextEncodeHunyuanVideo_ImageToVideo

Der Node TextEncodeHunyuanVideo_ImageToVideo erzeugt Konditionierungsdaten für die Bild-zu-Video-Generierung, indem er einen Text-Prompt mit visuellen Informationen aus einem Referenzbild kombiniert. Er verwendet ein CLIP-Modell, um sowohl den Text als auch die Bild-Embeddings aus einer CLIP-Vision-Ausgabe zu verarbeiten, und erzeugt dann Tokens, die diese beiden Quellen gemäß der Einstellung `image_interleave` kombinieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das für Tokenisierung und Kodierung verwendet wird. | CLIP | Ja | - |
| `clip_vision_output` | Die visuellen Embeddings aus einem CLIP-Vision-Modell, die Bildkontext für das Referenzbild bereitstellen. | CLIP_VISION_OUTPUT | Ja | - |
| `prompt` | Die Textbeschreibung, die die Videogenerierung steuert. Unterstützt mehrzeilige Eingaben und dynamische Prompts. Der Prompt wird mithilfe einer Vorlage formatiert, die das Modell auffordert, das Video basierend auf dem Referenzbild zu beschreiben, und dabei Aspekte wie Hauptinhalt, Objektdetails, Aktionen, Hintergrund und Kamerawinkel abdeckt. | STRING | Ja | - |
| `image_interleave` | Wie stark das Bild im Vergleich zum Text-Prompt Einfluss nimmt. Eine höhere Zahl bedeutet mehr Einfluss des Text-Prompts. Dies ist eine erweiterte Einstellung (Standard: 2). | INT | Ja | 1-512 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die Konditionierungsdaten, die Text- und Bildinformationen für die Videogenerierung kombinieren. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
