# Splat rendern

Rendern Sie einen Gaussian-Splat als Bild mithilfe eines anisotropen EWA-Rasterizers mit orientierten elliptischen Splats, Antialiasing und tiefensortiertem Front-to-Back-Rendering. Die Kamera stammt aus einer `camera_info`-Eingabe, oder Sie lassen sie leer, um den Splat automatisch einzupassen. Setzen Sie `frames` größer als 1 für einen Turntable-Batch von Bildern, der einen Video-Node speist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `splat` | Die zu rendernden Gaussian-Splat-Daten | SPLAT | Ja | - |
| `width` | Breite des Ausgabebilds (Standard: 1024) | INT | Ja | 64 bis 2048 (Schritt: 8) |
| `height` | Höhe des Ausgabebilds (Standard: 1024) | INT | Ja | 64 bis 2048 (Schritt: 8) |
| `frames` | Anzahl der zu rendernden Frames. -1, 0 oder 1 erzeugt ein einzelnes Standbild. Werte größer als 1 erzeugen eine Turntable-Animation, bei der die Kamera eine vollständige 360-Grad-Drehung ausführt. Negative Werte umkreisen in die entgegengesetzte Richtung (Standard: 1) | INT | Ja | -240 bis 240 |
| `splat_scale` | Multiplikator für die projizierte Grundfläche jedes Splats. Niedrigere Werte erzeugen schärfere Punkte, höhere Werte erzeugen weichere und vollere Oberflächen (Standard: 1.0) | FLOAT | Ja | 0.1 bis 5.0 (Schritt: 0.05) |
| `sharpen` | Steuert die Schärfe überlappender Splats. Ein Wert von 1.0 liefert physikalisch korrektes Blending. Werte über 1.0 gewichten jedes Pixel in Richtung seines dominanten (nächstgelegenen) Splats für schärfere Textur, ohne Splats zu verkleinern oder Lücken zu öffnen (Standard: 2.0) | FLOAT | Ja | 1.0 bis 8.0 (Schritt: 0.5) |
| `headlight_shading` | Diffuse Schattierung durch ein Licht an der Kameraposition, unter Verwendung der Surfel-Normalen des Splats. Dunkelt Oberflächen ab, die sich von der Ansicht abwenden, um Form und Krümmung sichtbar zu machen. 0 liefert flaches Albedo, 1 liefert die stärkste Schattierung (Standard: 0.0) | FLOAT | Ja | 0.0 bis 3.0 (Schritt: 0.05) |
| `opacity_threshold` | Verwirft Gaussians mit einer Opazität unterhalb dieses Schwellenwerts, wodurch schwache Floater entfernt werden (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |
| `render_style` | Was die Bildausgabe anzeigt. Optionen sind: color (vollfarbiges Rendering), clay (mit neutralem Albedo schattiert), depth (nahe Objekte erscheinen hell), normal (OpenGL-Normal Map) (Standard: "color") | COMBO | Ja | "color"<br>"clay"<br>"depth"<br>"normal" |
| `background` | Einfarbige Hintergrundfarbe für das Rendering (Standard: #000000) | COLOR | Ja | - |
| `bg_image` | Optionale Hintergrundplatte, die hinter dem Splat komponiert wird. Überschreibt die einfarbige Hintergrundfarbe. Wird auf die Rendergröße skaliert. Ein Stapel von Bildern wird pro Frame verwendet, ein einzelnes Bild wird für alle Frames verwendet. Funktioniert nur mit den Render-Stilen color und clay | IMAGE | Nein | - |
| `camera_info` | Kamera, aus der gerendert wird. Kann von einem Load3D-, Preview3D- oder Create Camera Info-Node stammen. Wenn leer, wird der Splat automatisch aus einer standardmäßigen 3/4-Ansicht eingepasst | CAMERA_3D | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das gerenderte Bild des Gaussian-Splats | IMAGE |
| `mask` | Die Alpha-Maske des gerenderten Splats | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderSplat/de.md)

---
**Source fingerprint (SHA-256):** `038bd9fb032f347ecda665c03719a64b0cf907599b701606f5cf6d0606d19d98`
