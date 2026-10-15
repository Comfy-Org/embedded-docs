# Set Reference Multi Latent

Dieser Knoten kodiert ein oder mehrere Referenzbilder und hängt deren Latents an die Konditionierung an, die ein Editiermodell verwendet. Er ist das Multi-Bild-Gegenstück zu Set Reference Latent: Sie verbinden einen VAE plus eine Reihe von Referenzbildern, und der Knoten hängt jedes kodierte Latent an die positive Konditionierung und, sofern eine verbunden ist, auch an die negative Konditionierung an. Verwenden Sie ihn, wenn ein Modell mehrere Referenzbilder gleichzeitig statt eines einzelnen Latents erwartet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierung, die mit den Referenz-Latents geändert werden soll. | CONDITIONING | Ja | - |
| `negative` | Optionale negative Konditionierung, die dieselben Referenz-Latents erhält. Lassen Sie sie unverbunden, um die geänderte positive Konditionierung für die Ausgabe `negative` wiederzuverwenden. | CONDITIONING | Nein | - |
| `vae` | Der VAE, der zum Kodieren der verbundenen Referenzbilder verwendet wird. Wenn kein VAE verbunden ist, werden die Referenzbilder ignoriert. | VAE | Nein | - |
| `resolution` | Wie jedes Referenzbild vor der Kodierung vorbereitet wird. `"keep resolution"` kodiert es in seiner eingehenden Größe; `"resize"` skaliert es auf eine Ziel-Megapixelanzahl, wobei das Seitenverhältnis beibehalten wird, wodurch `megapixels` eingeblendet wird. (Standard: "keep resolution") | DYNAMIC_COMBO | Ja | `"keep resolution"`<br>`"resize"` |
| `images` | Erweiterbarer Slot: Verbinden Sie ein oder mehrere Referenzbilder (`image_1`, `image_2`, ...), die als Referenzen verwendet werden sollen. Bilder werden in Slot-Reihenfolge kodiert und in dieser Reihenfolge an die Konditionierung angehängt. | IMAGE | Nein | 1 bis 100 |

### Eingaben zur Größenänderung

Diese Optionen erscheinen, wenn `resolution` auf `"resize"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `megapixels` | Zielgröße jedes Referenzbilds unter Beibehaltung des Seitenverhältnisses. 1.0 entspricht etwa 1024 x 1024 Pixeln. (Standard: 1.0) | FLOAT | Ja | 0.01 bis 16.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierung mit den angehängten kodierten Referenz-Latents. | CONDITIONING |
| `negative` | Die negative Konditionierung mit denselben angehängten Referenz-Latents. Gibt die Ausgabe `positive` zurück, wenn keine negative Konditionierung verbunden ist. | CONDITIONING |
| `empty_latent` | Das erste Referenz-Latent multipliziert mit 0.0, bereit zum Initialisieren eines Samplers. Leer, wenn kein Referenzbild verbunden ist. | LATENT |

## Hinweise

- Die Latents werden angehängt statt ersetzt, sodass das Verketten mehrerer Knoten des Typs Set Reference Multi Latent Referenzen ansammelt.
- Jedes verbundene Bild wird separat kodiert, daher müssen die Referenzbilder nicht dieselbe Größe haben.
- Ohne verbundenes Bild werden `positive` und `negative` unverändert zurückgegeben und `empty_latent` ist leer.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/de.md)

---
**Source fingerprint (SHA-256):** `06f98e7c21e8750a2bdf365cb80fac990bcf01246f183c60ef83bd195fc1225b`
