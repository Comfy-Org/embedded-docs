# Normal Map aus Mesh backen

Dieser Node backt eine Tangentenraum-Normalmap von einem High-Poly-Mesh auf das UV-Layout eines Low-Poly-Meshs und erfasst dabei Oberflächendetails, die während der Dezimierung verloren gingen. Verbinden Sie das UV-entfaltete Low-Poly-Mesh und das High-Poly-Mesh, aus dem es hervorgegangen ist; der Node gibt ein Bild aus, das für den `normal_map`-Eingang von Apply Texture To Mesh bereit ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | Das UV-entfaltete Low-Poly-Mesh, das die gebackenen Details aufnimmt. Muss vorhandene UVs besitzen; der Node führt niemals ein Unwrapping durch. | MESH | Ja | — |
| `high_poly` | Das High-Poly-Mesh, dessen Oberflächendetails in das UV-Layout des Low-Poly-Meshs gebacken werden. | MESH | Ja | — |
| `resolution` | Kantenlänge in Pixeln der quadratischen Ausgabe-Normalmap (Standardwert: 1024). | INT | Ja | 64 bis 8192 (Schritt 64) |
| `cage_distance` | Oberflächen-Suchband als Bruchteil der Bounding-Box-Diagonale. Erhöhen Sie den Wert bei falschen/fehlenden Patches unter starker Dezimierung; verringern Sie ihn, wenn über Lücken hinweg gegriffen wird. Standardwert: 0.05. | FLOAT | Ja | 0.001 bis 0.5 (Schritt 0.001) |
| `ignore_backfaces` | Überspringt High-Poly-Oberflächen, die vom Texel abgewandt sind, damit Spalten/eingeschlossene Bereiche nicht die gegenüberliegende Wand erfassen. Nur deaktivieren, wenn die Windungsreihenfolge des High-Poly-Meshs inkonsistent ist. Standardwert: true. | BOOLEAN | Ja | true / false |

Hinweis: `low_poly` muss UV-Koordinaten besitzen. Wenn keine vorhanden sind, löst der Node einen Fehler aus, da er auf das vorhandene UV-Layout backt und das Mesh nicht entfaltet. Wenn `low_poly` ein Batch ist, wird jedes Element der Reihe nach gebacken; wenn `high_poly` nur ein Element enthält, wird dieses Element für jedes Batch-Element wiederverwendet. Leere Meshes im Batch werden mit einer Warnung übersprungen und erzeugen eine flache mittelgraue (0.5) Normalmap. Wenn die Low-Poly-UVs außerhalb des Bereichs [0,1] liegen, werden sie gleichmäßig in [0,1] eingepasst (mit einer Warnung, wenn das Layout gekachelt/UDIM aussieht), sodass der Bake-Vorgang und Apply Texture To Mesh dieselben UVs verwenden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `normal_map` | Die gebackene Tangentenraum-Normalmap (glTF/OpenGL +Y-Konvention) als quadratisches RGB-Bild mit resolution × resolution und Werten in [0,1]. Verbinden Sie sie mit dem `normal_map`-Eingang von Apply Texture To Mesh. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeNormalMapFromMesh/de.md)

---
**Source fingerprint (SHA-256):** `29df10014b5998b741d71db21d0c982d7bca85ad966a720063af15062e203322`
