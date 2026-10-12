# VaeDecodeShapeTrellis

Dieser Node dekodiert Trellis2-Shape-Latent-Repräsentationen in ein 3D-Mesh. Er verwendet ein VAE, um Sparse-Shape-Latent-Daten in Mesh-Geometrie umzuwandeln, und gibt außerdem Shape-Unterteilungsdaten aus, die während der Dekodierung erzeugt werden. Der Node unterstützt sowohl einzelne als auch gebatchte Latent-Eingaben und passt die Mesh-Ausrichtung automatisch an das erwartete Koordinatensystem an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `samples` | Die zu dekodierenden Latent-Samples, einschließlich des Sample-Tensors und der Sparse-Koordinatendaten. Das Latent-Dictionary kann außerdem optionale Felder enthalten: `coord_counts` für gebatchte Shapes, `coord_resolution` zur Steuerung der Mesh-Auflösung und `model_frame` für die Koordinatenausrichtung. | LATENT | Ja | None |
| `vae` | Das VAE-Modell, das zum Dekodieren des Shape-Latents in ein Mesh verwendet wird. | VAE | Ja | None |

### Hinweise zu `samples`

- Die Eingabe `samples` ist ein Latent-Dictionary, das den `samples`-Tensor und die Sparse-Koordinaten `coords` enthalten muss.
- Wenn `coord_counts` vorhanden ist, muss es ein 1D-Tensor aus nicht negativen Ganzzahlen sein, und die Summe aller Zählwerte muss der Gesamtzahl der Koordinatenzeilen entsprechen. Jeder Zählwert repräsentiert eine Shape im Batch.
- Wenn `coord_resolution` angegeben ist, wird die Mesh-Auflösung als `coord_resolution * 16` berechnet. Andernfalls wird der integrierte Auflösungspuffer des VAE verwendet (Standardwert: 1024).
- Wenn `model_frame` auf `"z_up"` gesetzt ist, werden die dekodierten Mesh-Vertices vom Z-up-Koordinatensystem in die von glTF verwendete Y-up-Konvention gedreht. Der Standardwert ist `"y_up"`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das dekodierte 3D-Mesh, das Vertex-Positionen und Face-Indizes enthält. Beim Dekodieren mehrerer Shapes werden die Meshes als einzelner gestapelter Tensor zurückgegeben, wenn sie alle dieselbe Shape haben, andernfalls als gepackter Batch variabler Größe. | MESH |
| `shape_subdivides` | Shape-Unterteilungsdaten, die in jeder Phase des Dekodierungsprozesses erzeugt werden. | SHAPE_SUBDIVIDES |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/de.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
