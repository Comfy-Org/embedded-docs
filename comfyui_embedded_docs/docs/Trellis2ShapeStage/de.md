# Trellis2-Formphase

Dieser Node richtet den ersten Sampling-Durchlauf der Shape-Generierung der Trellis2-Pipeline ein. Er nimmt das dichte Struktur-Voxel entgegen, das von VaeDecodeStructureTrellis2 erzeugt wurde, extrahiert die Sparse-Koordinaten der gefüllten Voxel, erstellt ein leeres Sparse-Latent und hängt die Sampling-Metadaten an die Konditionierung an, sodass das Modell sie während des Samplings lesen kann. Für den zweiten Shape-Durchlauf nach dem Upsampling verwenden Sie stattdessen Trellis2UpsampleStage, das die Kaskade und die Einrichtung der zweiten Stufe kombiniert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Die positive Konditionierung, die für die Shape-Stufe vorbereitet werden soll. Kann eine standardmäßige Trellis2-Konditionierung oder eine Pixal3D-Konditionierung sein, die ein Projektions-Feature-Paket bereitstellt; wenn Projektionsfeatures vorhanden sind, werden sie für die ausgewählte Stufe berechnet und an die Ausgabe-Konditionierung angehängt. | CONDITIONING | Ja | Beliebige Trellis2- oder Pixal3D-Konditionierung |
| `negative` | Die negative Konditionierung, die für die Shape-Stufe vorbereitet werden soll. Dieselben Metadaten der Shape-Stufe werden an sie angehängt wie an die positive Konditionierung. | CONDITIONING | Ja | Beliebige Trellis2- oder Pixal3D-Konditionierung |
| `voxel` | Dichtes Struktur-Voxel von VaeDecodeStructureTrellis2. | VOXEL | Ja | Jedes Voxelgitter; die Gitterauflösung (Voxel pro Achse) wählt die Pipeline-Stufe aus |

### Hinweise

- Die Auflösung des Voxelgitters wählt die Pipeline-Stufe aus: Eine Auflösung von 32 oder niedriger verwendet den Modus `shape_generation_512` mit der Stufe `shape_512`; eine Auflösung größer als 32 verwendet den Modus `shape_generation` mit der Stufe `shape_1024`.
- Das Voxel muss mindestens ein gefülltes Voxel enthalten; ein leeres Voxel löst einen Fehler aus. Die aus dem Voxel abgeleiteten Batch-Indizes müssen nichtnegativ und zusammenhängend sein.
- Wenn die Konditionierung `positive` ein `proj_feat_pack` enthält (wie von der Pixal3D-Konditionierung bereitgestellt), werden Projektionsfeatures für die ausgewählte Stufe berechnet und der Modellrahmen des Ausgabe-Latents wird auf `y_up` gesetzt. Andernfalls werden keine Projektionsfeatures angehängt und der Modellrahmen wird auf `z_up` gesetzt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die positive Konditionierung mit angehängten Metadaten der Shape-Stufe: Generierungsmodus, Sparse-Koordinaten, Koordinatenanzahl pro Batch und Projektionsfeatures, wenn die Quellkonditionierung sie bereitstellt. | CONDITIONING |
| `negative` | Die negative Konditionierung mit denselben angehängten Metadaten der Shape-Stufe. | CONDITIONING |
| `latent` | Ein leerer Sparse-Latent-Tensor (Form: Batch-Größe, 32, Token-Anzahl, 1) zusammen mit den extrahierten Sparse-Koordinaten, der Koordinatenanzahl pro Batch, der Koordinatenauflösung, dem Typmarker `trellis2` und der Orientierung des Modellrahmens. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/de.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
