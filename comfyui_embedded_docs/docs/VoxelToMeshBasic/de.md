# VoxelToMeshBasic

Der Node VoxelToMeshBasic konvertiert 3D-Voxeldaten in Mesh-Geometrie. Er verarbeitet Voxelvolumen, indem er einen Schwellenwert anwendet, um zu bestimmen, welche Teile des Volumens zu festen Oberflächen im resultierenden Mesh werden. Der Node gibt eine vollständige Mesh-Struktur mit Eckpunkten und Flächen aus, die für 3D-Rendering und Modellierung verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voxel` | Die 3D-Voxeldaten, die in ein Mesh umgewandelt werden sollen | VOXEL | Ja | - |
| `threshold` | Der Schwellenwert, der verwendet wird, um zu bestimmen, welche Voxel Teil der Mesh-Oberfläche werden (Standard: 0.6) | FLOAT | Ja | -1.0 to 1.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `MESH` | Das generierte 3D-Mesh, das Eckpunkte und Flächen enthält | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/de.md)

---
**Source fingerprint (SHA-256):** `95d729463e9d32fb0b8a82a397c6ed7fccaf190ec8a183d71a99fef170747fd1`
