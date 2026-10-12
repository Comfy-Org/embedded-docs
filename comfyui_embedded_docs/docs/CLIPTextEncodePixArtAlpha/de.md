# CLIP-Textkodierung (PixArt Alpha)

Kodiert Text und legt die Auflösungskonditionierung für PixArt Alpha fest. Dieser Node verarbeitet Texteingaben und fügt Breiten- und Höheninformationen hinzu, um Konditionierungsdaten speziell für PixArt-Alpha-Modelle zu erstellen. Er gilt nicht für PixArt-Sigma-Modelle.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `width` | Die Breitendimension für die Auflösungskonditionierung (Standard: 1024) | INT | Ja | 0 bis MAX_RESOLUTION |
| `height` | Die Höhendimension für die Auflösungskonditionierung (Standard: 1024) | INT | Ja | 0 bis MAX_RESOLUTION |
| `text` | Zu kodierende Texteingabe. Unterstützt mehrzeilige Eingaben und dynamische Prompts. | STRING | Ja | - |
| `clip` | CLIP-Modell, das für Tokenisierung und Kodierung verwendet wird | CLIP | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `CONDITIONING` | Kodierte Konditionierungsdaten mit Text-Tokens und Auflösungsinformationen | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/de.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
