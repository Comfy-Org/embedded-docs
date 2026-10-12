# Mesh reduzieren

Vereinfacht ein 3D-Mesh auf eine Zielanzahl von Flächen mithilfe der QEM-Vereinfachung (Quadric Error Metric), wobei die Berechnung auf dem aktiven Compute-Gerät ausgeführt wird. Der Platzierungsmodus `"midpoint"` ist die cumesh-faithful-Voreinstellung, die die beste Qualität bietet und dünne Merkmale wie Haare bewahrt, während `"qem"` Vertices an der QEM-optimalen Position platziert, mit optionalen Linien- und Feature-Edge-Steuerungen. Das Ausgabe-Mesh bleibt verschweißt.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das zu vereinfachende 3D-Mesh. | MESH | Ja | - |
| `target_face_count` | Maximale Zielanzahl an Flächen. 0 deaktiviert. (Standard: 200000) | INT | Ja | 0 bis 50000000 |
| `placement_mode` | midpoint: cumesh-faithful (empfohlen). qem: QEM-optimale Platzierung. (Standard: `"midpoint"`) | DYNAMIC_COMBO | Ja | `"midpoint"`<br>`"qem"` |

### Midpoint-Eingaben

Der Platzierungsmodus `"midpoint"` stellt keine zusätzlichen Unterparameter bereit; er verwendet die Standardvoreinstellung für die Midpoint-Platzierung.

### QEM-Eingaben

Die folgenden Unterparameter erscheinen in der Benutzeroberfläche nur, wenn `placement_mode` auf `"qem"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | Linien-Quadrik-Gewicht pro Kante; bewahrt scharfe Grate/Täler. 0 = aus. (Standard: 0.0) | FLOAT | Nein | 0.0 bis 100.0 |
| `feature_edge_quadric_weight` | Zusätzliches Quadrik-Gewicht auf Dieder-Feature-Kanten (Knicke). 0 = aus. (Standard: 0.0) | FLOAT | Nein | 0.0 bis 1000.0 |
| `feature_edge_min_dihedral_deg` | Minimaler Diederwinkel (Grad), damit eine Kante als Feature-Kante zählt. (Standard: 30.0) | FLOAT | Nein | 0.0 bis 180.0 |
| `clamp_v_to_edge` | Projiziert die QEM-optimale Position auf das kollabierte Kantensegment. (Standard: true) | BOOLEAN | Nein | `true`<br>`false` |

Hinweis: Die Dezimierung wird übersprungen, wenn `target_face_count` 0 ist oder wenn das Mesh bereits nicht mehr Flächen als das Ziel hat. Der Node zeigt selbst eine Zusammenfassung der Flächenreduzierung an, zum Beispiel `faces: 1.23M → 200K (-84%)`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das vereinfachte Mesh mit reduzierter Flächenanzahl; die Konnektivität bleibt verschweißt. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/de.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
