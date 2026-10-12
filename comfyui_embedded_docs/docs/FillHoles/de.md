# Löcher füllen

Dieser Node füllt Löcher in einem 3D-Mesh, indem er offene Randkanten erkennt und neue Flächen erstellt, um sie zu schließen. Er läuft auf der GPU, bewahrt vorhandene Geometrie und UVs und kann einzelne Meshes, Listen von Meshes oder Batches von Meshes verarbeiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das zu verarbeitende 3D-Mesh. Akzeptiert ein einzelnes Mesh, eine Liste von Meshes oder ein gebatchtes Mesh. | MESH | Ja | - |
| `max_perimeter` | Maximaler Lochumfang zum Füllen. 0 deaktiviert. (Standard: 0.03) | FLOAT | Ja | 0.0 bis unbegrenzt (Schrittweite 0.0001) |
| `weld_epsilon_rel` | Toleranz für das Vorverschweißen (Anteil der Bounding-Box-Diagonale); die Randerkennung benötigt verschweißte Vertices. 0 überspringt. (Standard: 1e-5) | FLOAT | Ja | 0.0 bis unbegrenzt (Schrittweite 1e-6) |
| `max_vertices` | Begrenzt die Rand-Vertices pro Zyklus; Centroid-Fan funktioniert nur bei kleinen, nahezu planaren Löchern. ≤16 beibehalten. (Standard: 16) | INT | Ja | 3 bis 1024 |
| `fill_chains` | Füllt auch offene Ketten (nicht nur Zyklen). Verrauscht; OFF entspricht cumesh. (Standard: False) | BOOLEAN | Ja | True or False |

Hinweis: Wenn `max_perimeter` größer als 0 ist, füllt der Node Löcher; wenn er 0 ist, wird das Füllen von Löchern vollständig übersprungen. Wenn `weld_epsilon_rel` größer als 0 ist, verschweißt der Node doppelte Vertices vor der Locherkennung. Die Schweißtoleranz beginnt beim angegebenen Anteil der Bounding-Box-Diagonale und erhöht sich automatisch durch Verdopplung, bis das Mesh als verschweißt gilt oder die Toleranz eine Obergrenze von 1e-2 erreicht. Löcher mit mehr als 8 Rand-Vertices verwenden eine Zentroid-Fan-Füllung (Einfügen eines neuen Zentroid-Vertices), während kleinere Löcher eine Vertex-Fan-Füllung verwenden, die einen vorhandenen Rand-Vertex wiederverwendet. Standardmäßig werden nur geschlossene Randzyklen gefüllt; setzen Sie `fill_chains` auf True, um auch offene Ketten zu schließen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das Mesh mit gefüllten Löchern, passend zum Batch-Format der Eingabe. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FillHoles/de.md)

---
**Source fingerprint (SHA-256):** `c0fd7f0c2d6eea098efb1dcfd80eaa52997e185b9c442b483f75318eea082196`
