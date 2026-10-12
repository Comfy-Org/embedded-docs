# Trellis2 VAE-Texturdekodierung

Dieser Node dekodiert ein Trellis2-Textur-Latent mithilfe eines VAE in Voxelfarben. Das eingegebene Latent enthält sparse Feature-Stichproben mit Koordinaten; der Node rekonstruiert die Farbe für jeden Voxel und gibt das Ergebnis als Voxelgitter zurück, das nachgelagerte Nodes wie PaintMesh verwenden können, um ein 3D-Mesh einzufärben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `samples` | Das zu dekodierende Textur-Latent. Es enthält die Sample-Features und sparse Koordinaten und kann optionale Metadaten wie Koordinatenanzahlen (`coord_counts`), Modell-Frame (`model_frame`, Standard: "y_up") und Koordinatenauflösung (`coord_resolution`) enthalten. | LATENT | Ja | — |
| `vae` | Das Trellis2-VAE, das zum Dekodieren des Textur-Latents in Voxelfarben verwendet wird. | VAE | Ja | — |
| `shape_subdivides` | Forminformationen, die verwendet werden, um die Rekonstruktion mit höherem Detail während der Dekodierung zu steuern. Hilft, die Strukturkonsistenz bei höheren Auflösungen zu bewahren. | SHAPE_SUBDIVIDES | Ja | — |

Hinweis: Wenn das `samples`-Latent `coord_counts` enthält, müssen die Anzahlen nicht negativ sein, ihre Summe muss der Anzahl der Koordinatenzeilen entsprechen, und jeder Batch muss genau die erwartete Anzahl an Zeilen enthalten; andernfalls löst der Node einen Fehler aus. Wenn `model_frame` des Latents "z_up" ist, werden die dekodierten Voxelkoordinaten auf Y-up umgesetzt, sodass sie mit den Mesh-Vertices ausgerichtet sind. Wenn `coord_resolution` angegeben ist, entspricht die Auflösung der Ausgabetextur diesem Wert multipliziert mit 16. Andernfalls wird sie aus der größten Voxelkoordinate plus eins abgeleitet und auf einen der Werte 256, 512, 1024, 1536 oder 2048 aufgerundet; wenn der benötigte Wert 2048 überschreitet, wird dieser größere Wert verwendet. Wenn keine Koordinaten verfügbar sind, ist die Auflösung standardmäßig 1024.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `voxel_colors` | Dekodierte Voxeldaten, die Koordinaten, Farb-Features und Texturauflösung enthalten. Jeder Voxel hat 6 Farbkanäle: Basisfarbe (RGB), Metallic, Rauheit und Alpha, alle im Bereich [0, 1]. Konsumenten von Vertexfarben wie PaintMesh verwenden die ersten 3 Kanäle. | VOXEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/de.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
