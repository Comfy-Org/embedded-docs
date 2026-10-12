# Trellis2Conditioning

Trellis2Conditioning wandelt ein Eingabebild in Conditioning-Daten für das TRELLIS.2-Modell um. Es verwendet ein CLIP-Vision-Modell, um das Bild in zwei Feature-Sets (mit 512er- und 1024er-Skalierung) zu kodieren, und bündelt diese zu einem positiven Conditioning-Paar. Zusätzlich wird ein passendes, mit Nullen gefülltes negatives Conditioning-Paar erzeugt, das als leere Referenz dient.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | Das CLIP-Vision-Modell, das verwendet wird, um das Bild in Conditioning-Merkmale zu kodieren. | CLIP_VISION | Ja | Jedes verfügbare CLIP-Vision-Modell |
| `image` | Vorverarbeitetes Bild aus ImageCropToMask (pad_factor=1.0 für TRELLIS.2). | IMAGE | Ja | Jedes Bild |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Conditioning, das die kodierten Bildmerkmale in 512er- und 1024er-Skalierung enthält und als positives Conditioning für das TRELLIS.2-Modell verwendet wird. | CONDITIONING |
| `negative` | Mit Nullen gefülltes Conditioning mit derselben Form wie das positive Conditioning; wird als leere negative Referenz verwendet. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
