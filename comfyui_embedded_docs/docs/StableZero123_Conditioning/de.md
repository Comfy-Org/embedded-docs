# StableZero123_Conditioning

Der Knoten StableZero123_Conditioning verarbeitet ein Eingabebild und Kamerawinkel, um Konditionierungsdaten und latente Repräsentationen für die 3D-Modellgenerierung zu erzeugen. Er verwendet ein CLIP-Visionsmodell, um die Bildeigenschaften zu kodieren, kombiniert sie mit Kameraeinbettungsinformationen basierend auf Elevations- und Azimutwinkeln und erzeugt positive und negative Konditionierung sowie eine latente Repräsentation für nachgelagerte 3D-Generierungsaufgaben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip_vision` | Das CLIP-Visionsmodell, das zur Kodierung der Bildeigenschaften verwendet wird | CLIP_VISION | Ja | - |
| `init_image` | Das Eingabebild, das verarbeitet und kodiert werden soll | IMAGE | Ja | - |
| `vae` | Das VAE-Modell, das zur Kodierung von Pixeln in den latenten Raum verwendet wird | VAE | Ja | - |
| `width` | Ausgabebreite für die latente Repräsentation (Standard: 256, Schritt: 8) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Ausgabehöhe für die latente Repräsentation (Standard: 256, Schritt: 8) | INT | Ja | 16 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der im Batch zu generierenden Samples (Standard: 1) | INT | Ja | 1 bis 4096 |
| `elevation` | Kamera-Elevationswinkel in Grad (Standard: 0.0, Schritt: 0.1) | FLOAT | Ja | -180.0 bis 180.0 |
| `azimuth` | Kamera-Azimutwinkel in Grad (Standard: 0.0, Schritt: 0.1) | FLOAT | Ja | -180.0 bis 180.0 |

**Hinweis:** Die Parameter `width` und `height` verwenden einen Schritt von 8, daher werden Werte in 8er-Schritten festgelegt. Der Knoten teilt sie durch 8, um die Dimensionen der latenten Repräsentation zu bestimmen. Das Bild wird vor der VAE-Kodierung mithilfe bilinearer Hochskalierung mit mittigem Zuschnitt auf die angegebene `width` und `height` skaliert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierungsdaten, die Bildeigenschaften und Kameraeinbettungen kombinieren, einschließlich des VAE-kodierten Eingabebilds als latenten Wert zum Verketten | CONDITIONING |
| `negative` | Negative Konditionierungsdaten mit auf null initialisierten Merkmalen und einem auf null initialisierten latenten Wert | CONDITIONING |
| `latent` | Auf null initialisierte latente Repräsentation mit Dimensionen [batch_size, 4, height//8, width//8] | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
