# VoxelToMesh

Der VoxelToMesh-Node konvertiert 3D-Voxeldaten in eine Mesh-Geometrie, indem er eine Oberfläche bei einem angegebenen Schwellenwert extrahiert. Er bietet zwei Algorithmen zur Oberflächenextraktion: eine einfache Methode, die einfache kastenförmige Flächen erzeugt, und eine Surface-Net-Methode, die glattere, detailliertere Meshes erzeugt. Der Node verarbeitet jedes Voxelgitter in der Eingabe und erzeugt Vertices und Faces, die eine 3D-Mesh-Darstellung bilden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `voxel` | Die eingegebenen Voxeldaten, die in eine Mesh-Geometrie konvertiert werden sollen | VOXEL | Ja | - |
| `algorithm` | Der Algorithmus, der für die Oberflächenextraktion verwendet wird. `"surface net"` erzeugt glattere Meshes, während `"basic"` einfache kastenförmige Flächen erzeugt (Standard: `"surface net"`) | COMBO | Ja | `"surface net"`<br>`"basic"` |
| `threshold` | Der Schwellenwert für die Oberflächenextraktion. Voxel mit Werten über diesem Schwellenwert gelten als fest (Standard: 0.6) | FLOAT | Ja | -1.0 bis 1.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MESH` | Das generierte 3D-Mesh, das Vertices und Faces aus allen eingegebenen Voxelgittern enthält. Wenn alle Voxelgitter Meshes mit identischen Formen erzeugen, ist die Ausgabe ein gestapelter Tensor; andernfalls wird ein Batch variabler Länge zurückgegeben | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/de.md)

---
**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`
