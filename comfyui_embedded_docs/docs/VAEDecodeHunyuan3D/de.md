# VAEDecodeHunyuan3D

Der VAEDecodeHunyuan3D-Node wandelt latente Repräsentationen mithilfe eines VAE-Decoders in 3D-Voxeldaten um. Er verarbeitet die latenten Samples durch das VAE-Modell mit konfigurierbaren Chunking- und Auflösungseinstellungen, um volumetrische Daten zu erzeugen, die für 3D-Anwendungen geeignet sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die latente Repräsentation, die in 3D-Voxeldaten dekodiert werden soll | LATENT | Ja | - |
| `vae` | Das VAE-Modell, das zum Dekodieren der latenten Samples verwendet wird | VAE | Ja | - |
| `num_chunks` | Die Anzahl der Chunks, in die die Verarbeitung zur Speicherverwaltung aufgeteilt wird. Erweiterter Parameter (Standard: 8000) | INT | Ja | 1000-500000 |
| `octree_resolution` | Die Auflösung der Octree-Struktur, die für die 3D-Voxelgenerierung verwendet wird. Erweiterter Parameter (Standard: 256) | INT | Ja | 16-512 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `voxels` | Die generierten 3D-Voxeldaten aus der dekodierten latenten Repräsentation | VOXEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/de.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
