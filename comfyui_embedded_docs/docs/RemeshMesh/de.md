# Mesh neu vernetzen (Narrow-Band DC)

Remesh Mesh vernetzt ein Mesh mit einer sauberen, gleichmäßigen Tessellierung neu, indem ein Schmalband-Distanzfeld um die ursprüngliche Oberfläche abgetastet und mit Dual Contouring extrahiert wird. Dadurch wird unordentliche, nicht-mannigfaltige oder selbstschneidende Topologie normalisiert, und der Node ist dafür gedacht, vor Decimate Mesh ausgeführt zu werden, um eine exakte Flächenanzahl zu erreichen. Die Verarbeitung läuft auf dem aktiven Compute-Gerät und das Ausgabe-Mesh bleibt verschweißt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `mesh` | Das Eingabe-Mesh, das neu vernetzt werden soll. | MESH | Ja | — |
| `resolution` | Voxel-Rasterauflösung (Ausgabedichte). 256 ~ 100k Flächen, 512 ~ 1M. Für eine exakte Flächenanzahl anschließend Decimate Mesh verwenden. (Standard: 512) | INT | Ja | 32 - 2048 |
| `sign_mode` | Modus der Oberflächenextraktion. "udf" ist robust gegenüber unordentlichen/nicht-mannigfaltigen Eingaben; "sdf" erzeugt eine saubere einzelne Oberfläche mit QEF (Quadratic Error Function)-Wiederherstellung scharfer Merkmale, benötigt aber eine konsistente Windungsrichtung. Die Auswahl eines Modus blendet seine spezifischen Unteroptionen ein. (Standard: "udf") | DYNAMIC_COMBO | Ja | "udf"<br>"sdf" |
| `band` | Breite des Schmalbands in Voxeleinheiten. Im UDF-Modus verschiebt sie außerdem die Oberfläche. (erweitert, Standard: 1.0) | FLOAT | Ja | 0.5 - 4.0 |
| `project_back` | Interpoliert Vertices linear zur ursprünglichen Oberfläche (0 = reines DC, 1 = eingerastet). (erweitert, Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 |
| `fix_poles` | Kollabiert Valenz-3-Vertex-Paare (DC-T-Kreuzungs-Artefakt). (erweitert, Standard: false) | BOOLEAN | Ja | true / false |
| `smooth_iters` | Taubin-Glättungsiterationen (0 = aus). 2-3 bereinigt treppenartige DC-Artefakte; höhere Werte glätten QEF-Kanten übermäßig. (Standard: 0) | INT | Ja | 0 - 20 |
| `drop_small_components` | Verwirft Komponenten unterhalb dieses Anteils an der Flächenanzahl der größten Komponente. 0 deaktiviert. (erweitert, Standard: 0.01) | FLOAT | Ja | 0.0 - 0.5 |
| `precluster_max_verts` | Begrenzt die Anzahl der Eingabe-Vertices vor den Feldabfragen; Eingaben darüber werden zuerst per Cluster-Decimation auf diesen Wert reduziert. Verhindert OOM bei riesigen Meshes. (erweitert, Standard: 20,000,000) | INT | Ja | 0 - 100,000,000 |

### "udf"-Modus-Eingaben

Diese Parameter werden angezeigt, wenn `sign_mode` auf `"udf"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `qef` | QEF (Quadratic Error Function)-Dual-Vertex-Platzierung für schärfere Kanten. (erweitert, Standard: false) | BOOLEAN | Nein | true / false |
| `drop_inverted_components` | Verwirft geschlossene Komponenten mit nach innen gerichteter Normale (negatives Volumen) – die innere UDF-Schale. (erweitert, Standard: false) | BOOLEAN | Nein | true / false |
| `drop_enclosed_components` | Verwirft Komponenten innerhalb der Bounding-Box der größten Komponente, die einen Point-in-Mesh-Raycast nicht bestehen. Für legitime verschachtelte Teile deaktivieren. (erweitert, Standard: false) | BOOLEAN | Nein | true / false |

### "sdf"-Modus-Eingaben

Diese Parameter werden angezeigt, wenn `sign_mode` auf `"sdf"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `qef` | QEF (Quadratic Error Function)-Dual-Vertex-Platzierung (stellt scharfe Merkmale wieder her) im Vergleich zum kantenkreuzenden Schwerpunkt. (Standard: true) | BOOLEAN | Nein | true / false |
| `manifold` | Manifold Dual Contouring: 1-4 Dual-Vertices/Voxel für Mehrschichtfälle. Langsamer. (Standard: false) | BOOLEAN | Nein | true / false |

Hinweis: Die Option `qef` hat je nach ausgewähltem Modus einen anderen Standardwert – false im Modus "udf", true im Modus "sdf". Wenn `precluster_max_verts` größer als 0 ist und das Eingabe-Mesh mehr Vertices als dieser Wert hat, wird das Mesh vor den Feldabfragen per Cluster-Decimation auf dieses Ziel reduziert. Nach der Verarbeitung zeigt der Node die Änderung der Flächenanzahl von Eingabe zu Ausgabe am Node an (zum Beispiel "faces: 1.23M → 200K (-84%)").

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `mesh` | Das neu vernetzte Mesh mit gleichmäßiger Tessellierung und verschweißter Topologie. Vertex-Farben bleiben erhalten, wenn sie in der Eingabe vorhanden sind; UVs, Normalen und Tangenten werden nicht übernommen. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/de.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
