# VAEDecodeTripoSplat

Dekodiert eine latente TripoSplat-Repräsentation in einen 3D-Gaussian-Splat. Dieser Node nimmt das gesampelte Latent aus einem TripoSplat-Modell und rekonstruiert es als eine Menge von 3D-Gaussians, deren Dichte durch Ändern der Anzahl der erzeugten Gaussians angepasst werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|-----------|--------------|---------|
| `samples` | Die zu dekodierenden latenten Samples. Wenn die Samples neben dem Latent einen verschachtelten Kamera-Stream enthalten, wird nur der Latent-Stream dekodiert. | LATENT | Ja | - |
| `vae` | TripoSplat VAE-Decoder | VAE | Ja | - |
| `num_gaussians` | Anzahl der zu erzeugenden Gaussians (auf ein Vielfaches von 32 gerundet). 262144 entspricht der Punktdichte des Octrees; höhere Werte überabtasten dieselben Punkte (dichter, aber ohne neue Details) und verbrauchen proportional mehr VRAM/Zeit. Standard: 262144 | INT | Ja | 32 bis 1048576 (Schritt: 32) |
| `seed` | Legt den Seed für den Octree-Punktsampler (globaler RNG) fest, um deterministische Dekodierungen zu ermöglichen. Standard: 0 | INT | Ja | 0 bis 18446744073709551615 |

**Hinweis:** Der Wert für `num_gaussians` wird automatisch auf den zulässigen Bereich begrenzt und auf ein Vielfaches der Einstellung „Gaussians pro Punkt“ des VAE-Decoders gerundet. Die tatsächlich verwendete Anzahl kann leicht vom Eingabewert abweichen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|-----------|
| `splat` | Der dekodierte 3D-Gaussian-Splat, der Positionen, Skalierungen, Rotationen, Opazitäten und Koeffizienten der sphärischen Harmonischen enthält | SPLAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/de.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
