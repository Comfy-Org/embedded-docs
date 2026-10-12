# Tripo: Intelligente Segmentierung

Zerlegt ein 3D-Modell in semantisch sinnvolle Teile und gibt jedem Teil einen Namen. Es kann entweder ein vorhandenes Modell segmentieren (das über eine Task-ID bereitgestellt wird) oder zuerst ein Modell aus einem Bild generieren und es dann segmentieren. Die resultierende `segment task_id` kann von anderen Tripo-Nodes wie Complete Mesh Parts, Retopology, Texture model und Convert model auf dieselbe Weise verwendet werden wie ein Tripo: Segment Model-Ergebnis.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `source` | Ein vorhandenes Modell segmentieren oder ein Modell aus einem Bild generieren und segmentieren. Die ausgewählte Option bestimmt, welche zusätzlichen Eingaben angezeigt werden. | DYNAMIC_COMBO | Ja | `"model"`<br>`"image"` |

### Modell-Eingaben

Wird angezeigt, wenn `source` auf `"model"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | Ein GLB-Ergebnis. Quad-(FBX)-Meshes müssen zuerst mit Tripo: Convert model (GLTF) konvertiert werden. | MODEL_TASK_ID | Ja | - |
| `granularity` | Wie fein das Modell in Teile aufgeteilt wird (Standard: "medium"). | COMBO | Nein | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Optionaler Text, der die Teile benennt, nach denen gesucht werden soll, z. B. 'Spielfigur mit Schwert und Rüstung' (Standard: leer). | STRING | Nein | - |

### Bild-Eingaben

Wird angezeigt, wenn `source` auf `"image"` gesetzt ist. Tripo generiert zuerst ein Modell aus dem Bild und segmentiert es dann.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Bild, das verwendet wird, um das Modell zu generieren, das segmentiert werden soll. | IMAGE | Ja | - |
| `granularity` | Wie fein das Modell in Teile aufgeteilt wird (Standard: "medium"). | COMBO | Nein | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Optionaler Text, der die Teile benennt, nach denen gesucht werden soll, z. B. 'Spielfigur mit Schwert und Rüstung' (Standard: leer). | STRING | Nein | - |

**Hinweise:**

- `granularity` und `hint` werden von beiden `source`-Optionen gemeinsam verwendet und sind optional. Wenn `hint` leer bleibt, wird kein Hinweis an den Dienst gesendet.
- Wenn `source` auf `"model"` gesetzt ist, werden nur GLB-Modelle akzeptiert. Andere Formate, z. B. Quad-(FBX)-Meshes, müssen zuerst mit Tripo: Convert model (GLTF) konvertiert werden.
- Die Aufgabe wird abgefragt (gepollt), bis sie einen Endzustand erreicht; die geschätzte Dauer beträgt etwa 180 Sekunden. Wenn Tripo ein unvollständiges Segmentierungsergebnis zurückgibt, meldet der Node einen Fehler.
- Preis-Badge: ungefähr 0,85 USD, wenn `source` auf `"image"` gesetzt ist, und ungefähr 0,55 USD, wenn `source` auf `"model"` gesetzt ist (Werte werden als ungefähr angezeigt).

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `segment task_id` | Task-ID der Segmentierungsaufgabe, verwendbar als Eingabe für andere Tripo-Nodes. | SEGMENT_TASK_ID |
| `model task_id` | Das Modell, das segmentiert wurde (aus dem Bild generiert oder importiert). | MODEL_TASK_ID |
| `GLB` | Die segmentierte 3D-Modell-Datei. | FILE3DGLB |
| `part_names` | Kommagetrennte Namen der Teile. | STRING |
| `parts` | Tripos Beschreibung der gefundenen Teile. | STRING |
| `mask` | Maskenbild, das durch die Segmentierung erzeugt wurde. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/de.md)

---
**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`
