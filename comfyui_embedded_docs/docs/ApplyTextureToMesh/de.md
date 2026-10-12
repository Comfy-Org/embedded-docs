# ApplyTextureToMesh

Dieser Node hängt gebackene Texturbilder an das UV-Layout eines Meshes, sodass sie zusammen mit dem Mesh vom SaveGLB-Node exportiert werden können. Übergeben Sie ihm dasselbe UV-entfaltete Mesh, von dem Sie die Texturen gebacken haben, zusammen mit den gebackenen Bild-Maps. Optionale Metallic-, Roughness- und Occlusion-Maps werden in einer einzigen ORM-Textur gepackt, und wenn eine Normal-Map bereitgestellt wird, werden zusätzlich die glatten Vertex-Normalen und die für korrektes Shading erforderliche Tangentenbasis gespeichert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das UV-entfaltete Mesh, an das die gebackenen Texturen angehängt werden. Muss dasselbe Mesh sein, das beim Backen verwendet wurde; es wird ein Fehler ausgelöst, wenn das Mesh keine UVs hat. | MESH | Ja | — |
| `base_color` | Das gebackene Base-Color-Bild. Wird als Textur des Meshes gespeichert und auf den Bereich 0-1 begrenzt. | IMAGE | Ja | — |
| `metallic` | Die gebackene Metallic-Map. Wird als blauer Kanal der kombinierten ORM-Textur verwendet; standardmäßig 0, wenn nicht angegeben. | IMAGE | Nein | — |
| `roughness` | Die gebackene Roughness-Map. Wird als grüner Kanal der kombinierten ORM-Textur verwendet; standardmäßig 1, wenn nicht angegeben. | IMAGE | Nein | — |
| `occlusion` | Die gebackene Ambient-Occlusion-Map. Wird als roter Kanal der kombinierten ORM-Textur verwendet; standardmäßig 1, wenn nicht angegeben. Wenn angegeben, wird die ORM-Textur außerdem als Occlusion-Textur für SaveGLB markiert. | IMAGE | Nein | — |
| `normal_map` | Die gebackene Tangent-Space-Normal-Map. Wenn angegeben, berechnet der Node die Tangenten pro Vertex neu und exportiert glatte Vertex-Normalen, damit die Normal-Map korrekt schattiert wird. | IMAGE | Nein | — |

Hinweis: Die Eingabe `mesh` muss UV-Koordinaten haben; wenn nicht, löst der Node einen Fehler aus, der Sie auffordert, dasselbe UV-entfaltete Mesh anzuschließen, das zum Backen verwendet wurde.

Hinweis: Wenn eine der Eingaben `metallic`, `roughness` oder `occlusion` verbunden ist, werden alle drei in einer einzigen glTF-ORM-Textur gepackt, mit den Kanälen R = Occlusion, G = Roughness, B = Metallic. Fehlende Maps werden mit Standardwerten gefüllt (Occlusion 1, Roughness 1, Metallic 0), und Maps mit unterschiedlichen Auflösungen werden auf die größte Breite und Höhe unter den bereitgestellten Maps skaliert.

Hinweis: Wenn `normal_map` verbunden ist, werden die gespeicherten Normalen des Meshes durch berechnete glatte Vertex-Normalen ersetzt und eine Tangentenbasis pro Vertex hinzugefügt. UV-Koordinaten, die außerhalb des Bereichs [0,1] liegen, werden gleichmäßig in [0,1] skaliert, wobei das Seitenverhältnis erhalten bleibt; eine Warnung wird protokolliert, wenn die UV-Ausdehnung wie ein gekacheltes/UDIM-Layout aussieht. Bei Meshes im Batch wird die UV-Normalisierung separat auf jedes Element im Batch angewendet, wobei dieselbe Logik wie beim Back-Schritt verwendet wird, sodass beide ausgerichtet bleiben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das Eingabe-Mesh mit den an sein UV-Layout angehängten Texturbildern, bereit zum Speichern durch SaveGLB. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/de.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
