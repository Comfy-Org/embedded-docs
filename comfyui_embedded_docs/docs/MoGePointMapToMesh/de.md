# MoGePointMapToMesh

Dieser Node konvertiert eine MoGe-Punktkarte in ein 3D-Mesh. Er nimmt Geometriedaten, die von einem MoGe-Node zur Tiefenschätzung erzeugt wurden, und trianguliert sie zu einem Mesh mit UV-Koordinaten und einer optionalen Textur.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Die MoGe-Geometriedaten, die Punktkarten, Tiefe und optional das Quellbild enthalten. | MOGE_GEOMETRY | Ja | N/A |
| `batch_index` | Welches Bild einer gebatchten MoGe-Geometrie als Mesh ausgegeben werden soll. Die Vertexanzahl unterscheidet sich pro Bild, daher können Batches nicht zu einem einzelnen MESH gestapelt werden (Standard: 0). | INT | Ja | 0 bis 4096 |
| `decimation` | Vertex-Schrittweite; 1 = volle Auflösung (Standard: 1). | INT | Ja | 1 bis 8 |
| `discontinuity_threshold` | Pixel verwerfen, deren 3x3-Tiefenspanne diesen Bruchteil überschreitet. 0 = aus (Standard: 0.04). | FLOAT | Ja | 0.0 bis 1.0 |
| `texture` | Das Quellbild als baseColor-Textur durchreichen (Standard: True). | BOOLEAN | Ja | True/False |

Hinweis: `batch_index` muss kleiner als die Batch-Größe der Eingabe `moge_geometry` sein; die Auswahl eines Index außerhalb des gültigen Bereichs löst einen Fehler aus. Die Eingabe muss eine Points-Ausgabe enthalten, andernfalls löst der Node einen Fehler aus. Wenn die Triangulation ein leeres Mesh erzeugt, löst der Node einen Fehler aus — das Setzen von `discontinuity_threshold` auf 0 deaktiviert den Tiefendiskontinuitätsfilter. Das Ausgabe-Mesh wird in glTF-Koordinaten konvertiert: perspektivische MoGe-Daten (X rechts, Y nach unten, Z nach vorn) werden umgedreht, um glTF zu entsprechen (Y nach oben, Z nach hinten), und panoramische Daten (Geometrie ohne intrinsische Parameter) werden entsprechend mit korrigierter Windungsrichtung rotiert. Wenn `texture` aktiviert ist, wird das Quellbild aus `moge_geometry` als baseColor-Textur verwendet.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `MESH` | Ein 3D-Mesh mit Vertices, Faces, UV-Koordinaten und einer optionalen baseColor-Textur aus dem Quellbild. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/de.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
