# BerniniConditioning

Der BerniniConditioning-Node bereitet Video- und Bildkonditionierungsdaten für das Modell Wan2.2-A14B vor. Er kodiert Quellvideos, Referenzvideos und Referenzbilder mit dem bereitgestellten VAE und hängt sie dann als In-Context-Tokens an die Konditionierungsdaten an. Die Aufgabe wird automatisch daraus abgeleitet, welche Eingaben verbunden sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `positive` | Positive Konditionierungsdaten | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungsdaten | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Video- und Bildeingaben verwendet wird | VAE | Ja | - |
| `width` | Breite des Ausgabe-Latents (Standard: 832) | INT | Ja | 16 to 8192 (step: 16) |
| `height` | Höhe des Ausgabe-Latents (Standard: 480) | INT | Ja | 16 to 8192 (step: 16) |
| `length` | Anzahl der Frames im Ausgabe-Latent (Standard: 81) | INT | Ja | 1 to 8192 (step: 4) |
| `batch_size` | Anzahl der Videos, die in einem einzelnen Batch generiert werden sollen (Standard: 1) | INT | Ja | 1 to 4096 |
| `source_video` | Quellvideo, das bearbeitet oder umgestaltet werden soll (v2v, rv2v). Wird auf `width`/`height` skaliert und auf `length` gekürzt. | IMAGE | Nein | - |
| `reference_video` | Video, das in das Quellvideo eingefügt werden soll (ads2v). Wird auf `length` gekürzt und mit beibehaltenem Seitenverhältnis skaliert (lange Kante auf `ref_max_size` begrenzt). | IMAGE | Nein | - |
| `reference_images` | Referenzbilder, die als In-Context-Tokens eingefügt werden (r2v, rv2v). Jedes Bild wird unabhängig mit seinem eigenen nativen Seitenverhältnis kodiert (lange Kante auf `ref_max_size` begrenzt). Es können bis zu 8 Bilder bereitgestellt werden. | IMAGE | Nein | 0 to 8 images |
| `ref_max_size` | Maximale Größe für die lange Kante von `reference_video` und `reference_images`. Wird mit beibehaltenem Seitenverhältnis skaliert und auf 16 px gerundet (Standard: 848). | INT | Nein | 16 to 8192 (step: 16) |

**Hinweis:** Die Aufgabe wird daraus abgeleitet, welche Eingaben verbunden sind:
- Keine Eingaben verbunden → Text-zu-Video (t2v)
- Nur `source_video` → Video-zu-Video (v2v)
- `source_video` + `reference_images` → referenzgestützte Videobearbeitung (rv2v)
- Nur `reference_images` → Referenz-zu-Video (r2v)
- `source_video` + `reference_video` → Bild/Video in Video einfügen (ads2v)

Kontext-Streams werden in einer festen Reihenfolge angehängt: `source_video` (Quellen-ID 1), dann `reference_video` (Quellen-ID 2), dann jedes Referenzbild (Quellen-IDs 3, 4, ...). Eine Referenzbild-Eingabe, die mehrere Bilder enthält, trägt einen Stream pro Bild bei.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `positive` | Positive Konditionierung mit angehängten Kontext-Latents | CONDITIONING |
| `negative` | Negative Konditionierung mit angehängten Kontext-Latents | CONDITIONING |
| `latent` | Leerer Latent-Tensor mit Abmessungen, die den angegebenen Werten für Breite, Höhe, Länge und Batch-Größe entsprechen | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/de.md)

---
**Source fingerprint (SHA-256):** `70b5026f9479249bc5d1fe4695583193216e34e1b092764ac30e0ec3b7eba670`
