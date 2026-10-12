# MoGe-Panorama-Inferenz ausführen

Dieser Node führt eine Tiefenschätzung auf equirektangularen Panoramabildern durch. Er teilt das Panorama in 12 perspektivische Ansichten auf, führt das MoGe-Tiefenschätzungsmodell auf jeder Ansicht aus und führt die Ergebnisse pro Ansicht wieder zu einer einzelnen Tiefenkarte zusammen, die das gesamte Panorama abdeckt. Die pro Ansicht vorhergesagten Normalen und der metrische Maßstab werden ignoriert, da die Maßstäbe pro Ansicht an den Überlappungsnähten nicht ausgerichtet werden könnten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | Das MoGe-Modell, das für die Inferenz verwendet werden soll. | MOGE_MODEL | Ja |  |
| `image` | Equirektangulares Panorama (beliebiges Seitenverhältnis). Der Node akzeptiert nur ein einzelnes Bild; die Übergabe eines Bildstapels führt zu einem Fehler. Es werden nur die ersten 3 Farbkanäle (RGB) verwendet. | IMAGE | Ja |  |
| `resolution_level` | Detailgrad pro Ansicht (0 = schnellste, 9 = detaillierteste) (Standard: 9). | INT | Ja | 0 bis 9 |
| `split_resolution` | Auflösung jeder perspektivischen Aufteilung (Standard: 512). | INT | Ja | 256 bis 1024 |
| `merge_resolution` | Auflösung der langen Seite der zusammengeführten equirektangularen Distanzkarte (Standard: 1920). | INT | Ja | 256 bis 8192 |
| `batch_size` | Ansichten pro Inferenzstapel (insgesamt 12 Aufteilungen) (Standard: 4). | INT | Ja | 1 bis 12 |
| `refine_steps` | Nur MoGe-3: spärliche volumetrische Verfeinerungsdurchläufe über die vorhergesagte Tiefe. Mehr Durchläufe schärfen feine Details und Kanten bei ungefähr linear steigenden Kosten. 0 deaktiviert die Verfeinerung. Wird von MoGe-1 / MoGe-2 ignoriert (Standard: 3). | INT | Ja | 0 bis 8 |

**Hinweise:**

- Die Eingabe muss ein einzelnes Bild sein. Wenn `image` mehr als ein Bild im Stapel enthält, löst der Node einen Fehler aus.
- `merge_resolution` wird als maximale Größe der langen Seite behandelt. Wenn das Panorama kleiner als dieser Wert ist, wird die zusammengeführte Karte in der ursprünglichen Panoramagröße erzeugt, anstatt hochskaliert zu werden. Das zusammengeführte Ergebnis wird vor der Rückgabe wieder auf die ursprüngliche Panoramaauflösung skaliert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `moge_geometry` | Ein Wörterbuch, das die geschätzte Geometrie enthält: `points` (3D-Punktwolke), `depth` (Tiefenkarte), `mask` (Maske des gültigen Bereichs) und `image` (das Eingabebild). | MOGE_GEOMETRY |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/de.md)

---
**Source fingerprint (SHA-256):** `7f21452d035b2fe9d30b0cd15ddad10916439492b1d682a8b28f1a79e375df58`
