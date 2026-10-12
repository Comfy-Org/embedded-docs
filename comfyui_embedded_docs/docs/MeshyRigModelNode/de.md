# Meshy: Modell riggen

Der Node Meshy: Rig Model nimmt ein 3D-Modell aus einer vorherigen Meshy-Aufgabe und erstellt automatisch ein Skelett dafür, wodurch ein geriggter Charakter entsteht, der posiert und animiert werden kann. Der Node gibt das geriggte Modell sowohl im GLB- als auch im FBX-Dateiformat aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `meshy_task_id` | Die eindeutige Aufgaben-ID aus einem vorherigen Meshy-Vorgang (z. B. Text-zu-3D oder Bild-zu-3D), der das zu riggende Modell erzeugt hat. | MESHY_TASK_ID | Ja | N/A |
| `height_meters` | Die ungefähre Höhe des Charaktermodells in Metern. Dies trägt zur Genauigkeit von Skalierung und Rigging bei (Standard: 1,7). | FLOAT | Ja | 0.1 bis 15.0 |
| `texture_image` | Das UV-entfaltete Basisfarbtextur-Bild des Modells. | IMAGE | Nein | N/A |

**Hinweis:** Der automatische Rigging-Prozess ist derzeit nicht für untexturierte Meshes, nicht humanoide Assets oder humanoide Assets mit unklarer Gliedmaßen- und Körperstruktur geeignet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_file` | Eine Legacy-Ausgabe, die nur aus Gründen der Abwärtskompatibilität beibehalten wird und den Dateinamen des GLB-Modells enthält. | STRING |
| `rig_task_id` | Die eindeutige Aufgaben-ID für diesen Rigging-Vorgang, die verwendet werden kann, um auf das Ergebnis in späteren Meshy-Nodes zu verweisen. | MESHY_RIGGED_TASK_ID |
| `GLB` | Das geriggte 3D-Charaktermodell, gespeichert im GLB-Dateiformat. | FILE3DGLB |
| `FBX` | Das geriggte 3D-Charaktermodell, gespeichert im FBX-Dateiformat. | FILE3DFBX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/de.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
