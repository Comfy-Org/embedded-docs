# Hunyuan3Dv2Conditioning

Der Node `Hunyuan3Dv2Conditioning` verarbeitet die Ausgabe von CLIP Vision, um Konditionierungsdaten für 3D-Modelle zu erzeugen. Er extrahiert die Embeddings des letzten verborgenen Zustands aus der Vision-Ausgabe und erstellt sowohl positive als auch negative Konditionierungspaare. Die positive Konditionierung verwendet die tatsächlichen Embeddings, während die negative Konditionierung Embeddings mit Nullwerten derselben Form verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `clip_vision_output` | Die Ausgabe eines CLIP-Vision-Modells, die visuelle Embeddings enthält | CLIP_VISION_OUTPUT | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `positive` | Positive Konditionierungsdaten, die die CLIP-Vision-Embeddings enthalten | CONDITIONING |
| `negative` | Negative Konditionierungsdaten, die Embeddings mit Nullwerten enthalten, die der Form der positiven Embeddings entsprechen | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
