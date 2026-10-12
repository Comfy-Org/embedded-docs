# RotateMesh

Dreht ein 3D-Mesh um die Weltachsen, entweder mit Euler-XYZ-Winkeln (in Grad) oder mit einem Quaternion. Im Euler-XYZ-Modus werden die Rotationen als X, dann Y, dann Z angewendet; im Quaternion-Modus wird das (w, x, y, z)-Quaternion automatisch normalisiert. Die Rotation wird auf die Vertices des Meshes angewendet, und die Normalen und Tangenten werden ebenfalls gedreht, damit Beleuchtung und Schattierung korrekt bleiben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `mode` | Der zu verwendende Rotationsmodus. `"euler_xyz"` wendet die Rotation als X-, dann Y-, dann Z-Winkel um die Weltachsen an (in Grad). `"quaternion"` verwendet ein (w, x, y, z)-Quaternion, das automatisch normalisiert wird. | DYNAMIC_COMBO | Ja | `"euler_xyz"`<br>`"quaternion"` |
| `mesh` | Das zu drehende 3D-Mesh. | MESH | Ja | — |

### euler_xyz Eingaben

Diese Eingaben werden angezeigt, wenn `mode` auf `"euler_xyz"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `angle_x` | Drehung um die X-Achse in Grad. (Standard: 0.0) | FLOAT | Nein | -360.0 bis 360.0 (Schrittweite: 0.1) |
| `angle_y` | Drehung um die Y-Achse in Grad. (Standard: 0.0) | FLOAT | Nein | -360.0 bis 360.0 (Schrittweite: 0.1) |
| `angle_z` | Drehung um die Z-Achse in Grad. (Standard: 0.0) | FLOAT | Nein | -360.0 bis 360.0 (Schrittweite: 0.1) |

### quaternion Eingaben

Diese Eingaben werden angezeigt, wenn `mode` auf `"quaternion"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `qw` | W-Komponente des Quaternions (w, x, y, z). (Standard: 1.0) | FLOAT | Nein | -1.0 bis 1.0 (Schrittweite: 0.001) |
| `qx` | X-Komponente des Quaternions (w, x, y, z). (Standard: 0.0) | FLOAT | Nein | -1.0 bis 1.0 (Schrittweite: 0.001) |
| `qy` | Y-Komponente des Quaternions (w, x, y, z). (Standard: 0.0) | FLOAT | Nein | -1.0 bis 1.0 (Schrittweite: 0.001) |
| `qz` | Z-Komponente des Quaternions (w, x, y, z). (Standard: 0.0) | FLOAT | Nein | -1.0 bis 1.0 (Schrittweite: 0.001) |

**Hinweis:** Wenn `mode` `"euler_xyz"` ist und alle drei Winkel 0.0 sind, oder wenn `mode` `"quaternion"` ist und das Quaternion die Identität (1, 0, 0, 0) ist, wird das Mesh unverändert zurückgegeben. Das Quaternion wird vor der Verwendung automatisch normalisiert; wenn sein Betrag unter 1e-8 liegt, löst der Node einen Fehler aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `mesh` | Das gedrehte Mesh. Vertices werden gedreht, und Normalen werden als Richtungen gedreht. Bei Tangenten werden ihre X-, Y-, Z-Komponenten gedreht, während die W-Komponente (Händigkeit) unverändert bleibt. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RotateMesh/de.md)

---
**Source fingerprint (SHA-256):** `38b120a3f719264d1269275ecfefa145b507c688735e4a461bb89517c697674f`
