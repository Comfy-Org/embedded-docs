# TripoSplatPreprocessImage

Dieser Node schneidet jedes Eingabebild auf ein zentriertes Quadrat auf schwarzem Hintergrund zu und fügt Padding hinzu, um die angegebene Ausgabegröße zu erreichen. Er ist darauf ausgelegt, Bilder für das TripoSplat-3D-Modell vorzubereiten, indem er eine einheitliche quadratische Rahmung und eine optionale Erosion der Alpha-Matte gewährleistet, um Randartefakte zu vermeiden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das/die Eingabebild(er), die vorverarbeitet werden sollen. | IMAGE | Ja | - |
| `mask` | Alpha-Maske für das Bild, die verwendet wird, um den Zuschneidebereich zu bestimmen. | MASK | Ja | - |
| `erode_radius` | Erodiert die Alpha-Matte um diesen Pixelradius vor dem Zuschneiden (vermeidet Randüberlauf). Standard: 1. Auf 0 setzen, um die Erosion zu deaktivieren. | INT | Ja | 0 bis 16 |
| `size` | Quadratische Bildgröße. Das Modell ist auf 1024 trainiert; andere Größen funktionieren, liegen jedoch außerhalb der Verteilung. Standard: 1024. | INT | Ja | 256 bis 4096 (Schrittweite 16) |

**Hinweis:** Die Eingabe `mask` ist erforderlich und muss bereitgestellt werden. Wenn die Maske eine andere Batch-Größe als das Bild hat, wird sie automatisch wiederholt, um sie anzugleichen. Wenn die Maskenabmessungen von den Bildabmessungen abweichen, wird die Maske mithilfe bilinearer Interpolation an das Bild angepasst. Die Ausgabegröße wird automatisch auf das nächstniedrigere Vielfache von 16 abgerundet (Minimum 16), um die Kompatibilität mit den Patch-Anforderungen von DINOv3 und den Stride-Anforderungen des Flux2-VAE sicherzustellen. Der Node löst einen Fehler aus, wenn die Maske keine Vordergrundpixel enthält (leere Maske). Wenn `erode_radius` 0 ist, wird keine Erosion angewendet. Der quadratische Zuschnitt wird auf dem Alpha-Begrenzungsrahmen der Maske zentriert und auf das 1,2-Fache der größeren Abmessung des Begrenzungsrahmens dimensioniert; alle Bereiche außerhalb der Bildgrenzen werden mit Schwarz gefüllt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das/die vorverarbeitete(n) Bild(er), zugeschnitten auf ein zentriertes Quadrat auf schwarzem Hintergrund mit Padding, in der angeforderten `size`-Auflösung. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatPreprocessImage/de.md)

---
**Source fingerprint (SHA-256):** `ec66941846398ee6637576b11ae9d2f9576f6b05ed2ef730cdbf99a68fe9b838`
