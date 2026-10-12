# TripoSplat-Sampling-Vorschau

Dieser Node patcht ein TripoSplat-Modell, sodass bei Verwendung mit dem standardmäßigen KSampler-Node bei jedem Sampling-Schritt eine Live-Vorschau des dekodierten Gaussian Splat angezeigt wird. Er funktioniert, indem der Callback des Samplers umschlossen wird, um die Ausgabe des Modells nach jedem Schritt in ein Vorschaubild zu dekodieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Das TripoSplat-Modell, das für die Live-Vorschau gepatcht werden soll (liefert die Conditioning-Token-Länge, die zur Schätzung des Speicherbedarfs verwendet wird) | MODEL | Ja | |
| `vae` | TripoSplat-VAE-Decoder | VAE | Ja | |
| `octree_level` | Octree-Tiefe für die Vorschau-Dekodierung (niedriger = sparsamer/grobkörniger). Standard: 5 | INT | Nein | 2 bis 8 |
| `num_gaussians` | Anzahl der für die Vorschau zu erzeugenden Gaussians (auf ein Vielfaches von 32 gerundet). Standard: 16384 | INT | Nein | 1024 bis 262144 (Schritt: 32) |
| `yaw` | Gierwinkel der Vorschaukamera in Grad. Standard: 90.0 | FLOAT | Nein | -360.0 bis 360.0 (Schritt: 1.0) |
| `pitch` | Nickwinkel der Vorschaukamera in Grad. Standard: 15.0 | FLOAT | Nein | -89.0 bis 89.0 (Schritt: 1.0) |
| `point_size` | Maximaler Splat-Radius in Pixeln. Jeder Gaussian wird anhand seiner Skalierung dimensioniert und hier begrenzt; niedriger = feiner/punktiger, höher = klobiger/gröber. Standard: 3 | INT | Nein | 1 bis 16 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MODEL` | Das gepatchte TripoSplat-Modell mit hinzugefügter Live-Vorschau-Funktionalität | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/de.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
