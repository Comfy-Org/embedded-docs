# Pixal3D Multi-View-Conditioning

Der Node Pixal3D Multi-View Conditioning erstellt Conditioning-Daten aus einem festen Orbit-Kamera-Rig: Vorder-, linke, hintere und rechte Ansichten, die in 90-Grad-Schritten angeordnet sind und genau so verwendet werden, wie sie gerahmt sind. Verbinden Sie mindestens eine quadratische Ansicht des Objekts, und er bereitet passende positive und negative Conditioning-Daten für Pixal3D-Modelle vor.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision mit gebündelten NAF-Gewichten. | CLIP_VISION | Ja | N/A |
| `fov` | Horizontaler FOV in Grad der Ansichten wie gerahmt: 20 für Rig-Renderings und die meisten Multi-View-Generatoren oder MoGeGeometryToFOV auf einer der Ansichten für Fotos. Standard: 20.0. | FLOAT | Ja | 1.0 - 170.0 |
| `front` | Quadratische Ansicht der Vorderseite des Objekts, mit Alpha oder auf schwarzem Hintergrund, wie das Rig gerahmt: Das Objekt füllt an seiner breitesten Stelle etwa 1/1,1 des Bildes, im gleichen Maßstab in jeder Ansicht. Die erste verbundene Ansicht (Reihenfolge: front, left, back, right) ist die Vorderseite, auf die das Mesh ausgerichtet wird. | IMAGE | Nein | N/A |
| `left` | Quadratische Ansicht der linken Seite des Objekts, mit Alpha oder auf schwarzem Hintergrund, wie das Rig gerahmt: Das Objekt füllt an seiner breitesten Stelle etwa 1/1,1 des Bildes, im gleichen Maßstab in jeder Ansicht. Die erste verbundene Ansicht (Reihenfolge: front, left, back, right) ist die Vorderseite, auf die das Mesh ausgerichtet wird. | IMAGE | Nein | N/A |
| `back` | Quadratische Ansicht der Rückseite des Objekts, mit Alpha oder auf schwarzem Hintergrund, wie das Rig gerahmt: Das Objekt füllt an seiner breitesten Stelle etwa 1/1,1 des Bildes, im gleichen Maßstab in jeder Ansicht. Die erste verbundene Ansicht (Reihenfolge: front, left, back, right) ist die Vorderseite, auf die das Mesh ausgerichtet wird. | IMAGE | Nein | N/A |
| `right` | Quadratische Ansicht der rechten Seite des Objekts, mit Alpha oder auf schwarzem Hintergrund, wie das Rig gerahmt: Das Objekt füllt an seiner breitesten Stelle etwa 1/1,1 des Bildes, im gleichen Maßstab in jeder Ansicht. Die erste verbundene Ansicht (Reihenfolge: front, left, back, right) ist die Vorderseite, auf die das Mesh ausgerichtet wird. | IMAGE | Nein | N/A |

### Hinweise

- Mindestens eine Ansicht muss verbunden sein; der Node löst einen Fehler aus, wenn alle vier Ansichtseingaben leer sind.
- Die erste verbundene Ansicht, in der Reihenfolge front, left, back, right, wird als Vorderseite behandelt, und das Mesh wird auf diese Ansicht ausgerichtet. Wenn die erste verbundene Ansicht nicht `front` ist, wird eine Warnung protokolliert, die besagt, dass das Mesh mit dieser Ansicht als Vorderseite ausgerichtet wird.
- Ansichten werden in der Reihenfolge front, left, back, right gelesen und auf dem Orbit an ihren festen Azimuten relativ zur ersten verbundenen Ansicht platziert.
- Bei Eingabeansichten mit einem Alpha-Kanal wird das Alpha über Schwarz angewendet. Ansichten, die nicht 1024 x 1024 groß sind, werden auf 1024 x 1024 skaliert.
- Die Batch-Größe wird von der ersten verbundenen Ansicht übernommen. Wenn die verbundenen Ansichten unterschiedliche Batch-Größen haben, werden die kleineren zyklisch wiederholt, um sie anzugleichen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die positive Conditioning-Ausgabe, aufgebaut aus den kodierten Ansichten und ihren projizierten Merkmalen. | CONDITIONING |
| `negative` | Die negative Conditioning-Ausgabe, aufgebaut aus genullten Embeddings mit denselben projizierten Merkmalen. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/de.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
