# Pixal3DConditioning

Der Node Pixal3DConditioning bereitet die Bildkonditionierung für die Trellis2-3D-Generierungspipeline vor. Er verwendet ein DINOv3-Vision-Modell, um visuelle Merkmale aus dem Eingabebild in zwei Auflösungen (512 und 1024) zu extrahieren, und organisiert sie anschließend in Feature-Maps pro Stufe, die optional durch ein NAF-Modell verbessert werden können. Kamerainformationen werden aus dem horizontalen Sichtfeld abgeleitet, um die Projektions-Transformationsmatrix zu erstellen, und der Node gibt ein positives Conditioning-Paar (aus dem Bild abgeleitete Merkmale plus Projektionsdaten) sowie ein negatives Conditioning-Paar (genullte Feature-Tensoren) für Classifier-Free-Guidance aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Ja | — |
| `image` | Vorverarbeitetes Bild aus ImageCropToMask (pad_factor=1.1 für Pixal3D). | IMAGE | Ja | — |
| `camera_angle_x` | Horizontales FOV in Grad (angezeigt als `fov`). Verbinden Sie ein MoGeGeometryToFOV (axis='horizontal', unit='degrees') für ein FoV pro Bild (entspricht dem Upstream-Standard). Standard: 49.13. | FLOAT | Ja | 1.0 – 170.0 (step 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die positive Conditioning-Ausgabe, die die aus dem Bild abgeleiteten Feature-Maps und Projektionsdaten für die Trellis2-Generierung enthält. | CONDITIONING |
| `negative` | Die negative Conditioning-Ausgabe mit genullten Feature-Tensoren, die für Classifier-Free-Guidance verwendet wird. | CONDITIONING |

Hinweis: Der Wert `camera_angle_x` wird intern von Grad in Bogenmaß umgerechnet, und daraus wird die Kameradistanz berechnet, um die Projektions-Transformationsmatrix zu erstellen. Wenn das bereitgestellte Vision-Modell eine NAF-Komponente enthält, erzeugt der Node zusätzlich hochauflösende Feature-Maps für die Form- und Textur-Stufen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/de.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
