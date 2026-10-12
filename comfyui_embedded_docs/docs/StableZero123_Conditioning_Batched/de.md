# StableZero123_Conditioning_Batched

Der Node StableZero123_Conditioning_Batched bereitet Conditioning-Daten für die Generierung eines 3D-Modells aus einem einzelnen Eingabebild vor. Er kodiert das Bild mit einem CLIP-Vision-Modell und einem VAE, kombiniert die visuellen Merkmale mit Kamera-Embeddings, die aus Elevations- und Azimutwinkeln erstellt werden, und erzeugt positive und negative Conditioning-Daten sowie einen Latent-Tensor für einen Batch von Samples. Wenn `batch_size` größer als 1 ist, werden die Elevations- und Azimutwinkel für jedes Element im Batch um ihre Batch-Inkrementwerte erhöht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | Das CLIP-Vision-Modell, das zum Kodieren des Eingabebilds verwendet wird | CLIP_VISION | Ja | - |
| `init_image` | Das anfängliche Eingabebild, das verarbeitet und kodiert werden soll | IMAGE | Ja | - |
| `vae` | Das VAE-Modell, das zum Kodieren von Bildpixeln in den Latent-Raum verwendet wird | VAE | Ja | - |
| `width` | Die Ausgabebreite für das verarbeitete Bild (Standard: 256) | INT | Ja | 16 bis MAX_RESOLUTION (Schrittweite 8) |
| `height` | Die Ausgabehöhe für das verarbeitete Bild (Standard: 256) | INT | Ja | 16 bis MAX_RESOLUTION (Schrittweite 8) |
| `batch_size` | Die Anzahl der Conditioning-Samples, die im Batch generiert werden sollen (Standard: 1) | INT | Ja | 1 bis 4096 |
| `elevation` | Der anfängliche Kamera-Elevationswinkel in Grad (Standard: 0.0) | FLOAT | Ja | -180.0 bis 180.0 (Schrittweite 0.1) |
| `azimuth` | Der anfängliche Kamera-Azimutwinkel in Grad (Standard: 0.0) | FLOAT | Ja | -180.0 bis 180.0 (Schrittweite 0.1) |
| `elevation_batch_increment` | Der Betrag, um den die Elevation für jedes Batch-Element erhöht wird (Standard: 0.0). Als erweiterte Eingabe markiert. | FLOAT | Ja | -180.0 bis 180.0 (Schrittweite 0.1) |
| `azimuth_batch_increment` | Der Betrag, um den der Azimut für jedes Batch-Element erhöht wird (Standard: 0.0). Als erweiterte Eingabe markiert. | FLOAT | Ja | -180.0 bis 180.0 (Schrittweite 0.1) |

**Hinweis:** Die Werte für `width` und `height` müssen Vielfache von 8 sein, da der Node diese Dimensionen beim Aufbau des Latent-Tensors intern durch 8 teilt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die positiven Conditioning-Daten, die die Bild-Embeddings und Kamera-Embeddings für jedes Batch-Element enthalten | CONDITIONING |
| `negative` | Die negativen Conditioning-Daten mit null-initialisierten Embeddings | CONDITIONING |
| `latent` | Ein null-initialisierter Latent-Tensor mit den Dimensionen batch_size x 4 x height/8 x width/8, zusammen mit Batch-Indexierungsinformationen | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/de.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
