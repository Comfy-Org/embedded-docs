# Ambient Occlusion backen

Backt eine Ambient-Occlusion-Map aus einem High-Poly-Mesh in das UV-Layout eines Low-Poly-Mesh. Die Ausgabe ist ein Graustufenbild, in dem weiße Texel offen und dunkle Texel in Vertiefungen liegen; es ist für den `occlusion`-Eingang des Nodes Apply Texture To Mesh gedacht. Verbinden Sie das UV-entfaltete Low-Poly-Mesh und das High-Poly-Mesh, aus dem es durch Dezimierung erzeugt wurde.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `low_poly` | Das UV-entfaltete Low-Poly-Mesh, in das gebacken wird. Muss UVs besitzen; der Node löst einen Fehler aus, wenn sie fehlen. | MESH | Ja | - |
| `high_poly` | Das High-Poly-Mesh, aus dem das Low-Poly-Mesh durch Dezimierung erzeugt wurde; dient als Quellgeometrie für die Occlusion. | MESH | Ja | - |
| `resolution` | Texturauflösung in Pixeln; jeder Texel erhält einen Occlusion-Wert. Standard: 1024. | INT | Ja | 64 bis 8192 (Schritt 64) |
| `samples` | Strahlen pro Texel. Mehr = glatter, langsamer. Erhöhen, wenn das Ergebnis körnig ist. Standard: 64. | INT | Ja | 4 bis 1024 (Schritt 4) |
| `max_distance` | Strahlenlänge als Bruchteil der Diagonalen der Bounding-Box. Kleiner = engere, lokalere Occlusion. Standard: 0.5. | FLOAT | Ja | 0.01 bis 2.0 (Schritt 0.01) |
| `strength` | Skaliert die Occlusion. >1 dunkelt ab, <1 hellt auf. Standard: 1.0. | FLOAT | Ja | 0.0 bis 2.0 (Schritt 0.05) |
| `bias` | Anhebung des Strahlenursprungs von der Oberfläche als Bruchteil der Diagonalen der Bounding-Box. Erhöhen, wenn selbst ebene Flächen dunkle Flecken/Löcher zeigen. Standard: 0.01. | FLOAT | Ja | 0.0001 bis 0.2 (Schritt 0.0005) |

Hinweis: `low_poly` muss UV-Koordinaten besitzen — dieser Node entfaltet das Mesh niemals. Wenn `high_poly` nur ein Batch-Element enthält, wird es für jedes Batch-Element von `low_poly` wiederverwendet; Batch-Elemente von `low_poly` ohne Flächen werden übersprungen und durch ein vollständig weißes Bild ersetzt, wobei eine Warnung protokolliert wird. Wenn die UVs von `low_poly` über den Bereich 0-1 hinausragen, werden sie gleichmäßig wieder in diesen Bereich eingepasst, und eine Warnung wird protokolliert, wenn ein gekacheltes/UDIM-artiges Layout erkannt wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `occlusion` | Graustufen-Ambient-Occlusion-Bild mit Werten in [0,1] (weiß = offen, dunkel = Vertiefungen), ein Bild pro Batch-Element von `low_poly`. Gedacht für den `occlusion`-Eingang des Nodes Apply Texture To Mesh (gepackt in die ORM-Map / occlusionTexture). | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/de.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
