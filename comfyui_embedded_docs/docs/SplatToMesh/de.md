# Mesh aus Splat extrahieren

Dieser Node wandelt einen 3D-Gaussian-Splat in eine farbige Mesh-Oberfläche um. Er funktioniert, indem die Gaussians auf ein Dichtegitter rasterisiert, eine Iso-Oberfläche bei einem gewählten Dichteschwellenwert extrahiert und anschließend optionale Glättung und Bereinigung angewendet werden, um ein sauberes, farbiges Dreiecksnetz zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `splat` | Der eingegebene Gaussian-Splat, der in ein Mesh umgewandelt werden soll | SPLAT | Ja | - |
| `resolution` | Auflösung des Dichtegitters entlang der längsten Achse. Höhere Werte erzeugen feinere Oberflächendetails, benötigen aber mehr VRAM und Verarbeitungszeit (wächst mit Auflösung^3). Standard: 512 | INT | Ja | 64 - 768 (Schrittweite 16) |
| `kernel` | Maximale Splat-Halbbreite in Voxeln. Jedes Gaussian wird über ein Fenster rasterisiert, dessen Größe auf sein eigenes 3-Sigma begrenzt ist, wobei dieser Wert als Obergrenze dient. Kleine Surfels bleiben günstig, während große nicht abgeschnitten werden. Erhöhen, wenn dünn besetzte Splats Lücken hinterlassen. Standard: 5 | INT | Ja | 1 - 8 |
| `smooth` | Iterationen der Taubin-Mesh-Glättung. Glättet die Oberfläche, ohne sie zu schrumpfen (volumenerhaltend), im Gegensatz zum Weichzeichnen der Dichte. 0 bedeutet keine Glättung. Standard: 3 | INT | Ja | 0 - 60 |
| `level` | Iso-Oberflächenniveau. Wird automatisch per Otsu-Schwellenwertbestimmung gewählt; dieser Wert beeinflusst die automatische Auswahl (1.0 = auto, niedrigere Werte erzeugen dickere/stärker verbundene Oberflächen, höhere Werte erzeugen dünnere/engere Oberflächen). Standard: 0.4 | FLOAT | Ja | 0.0 - 2.0 (Schrittweite 0.01) |
| `min_component` | Verwirft verbundene Komponenten, die kleiner als diese Anzahl an Vertices sind. Entfernt abgetrennte Floater-Blobs und die innere Hülle von Doppelwänden. 0 behält alle Komponenten. Standard: 500 | INT | Ja | 0 - 100000 (Schrittweite 50) |
| `min_opacity` | Ignoriert Gaussians, die schwächer als dieser Wert sind, vor der Mesh-Erstellung. Standard: 0.02 | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `color_sharpen` | Schärft die Vertex-Textur. 1.0 ergibt eine physikalisch korrekte Mischung; höhere Werte verschieben die Farbe jedes Voxels in Richtung seines dominanten Gaussians, statt Nachbarn zu mitteln (entfernt Verwischungen in der Textur). Beeinflusst nur die Farbe, nicht die Geometrie. Standard: 2.0 | FLOAT | Ja | 1.0 - 8.0 (Schrittweite 0.5) |
| `solid` | Füllt das Innere anhand der Ausrichtung der Gaussians, für eine einzige geschlossene Oberfläche. Ausgeschaltet bleibt die rohe Dichtekontur erhalten, die eine versteckte Innenwand hinter der Oberfläche zurücklässt. Standard: True | BOOLEAN | Nein | True / False |
| `fill` | Wird nur verwendet, wenn `solid` aktiviert ist. Kosten des Schließens einer Öffnung relativ zum Folgen der Oberfläche. Niedrigere Werte schließen größere Öffnungen: etwa 3 versiegelt hohle Objekte, setzt aber auch Deckel auf Tassen und Kragen. Standard: 20.0 | FLOAT | Nein | 0.0 - 1000.0 (Schritt 1.0) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `mesh` | Das extrahierte farbige Mesh mit Unlit-Rendering (emissiv-ähnlich), um dem Erscheinungsbild des Splats zu entsprechen | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToMesh/de.md)

---
**Source fingerprint (SHA-256):** `6aadf2bd2fca334af112f99ffc8f6272cd20252977f7ef156905b00947573a0c`
