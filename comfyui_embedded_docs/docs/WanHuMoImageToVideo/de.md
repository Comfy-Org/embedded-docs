# WanHuMoImageToVideo

Der Node WanHuMoImageToVideo bereitet Konditionierungsdaten und ein leeres latentes Video für die Wan HuMo Videogenerierungspipeline vor. Er kann ein Referenzbild und Audio-Embeddings an die positiven und negativen Konditionierungseingaben anhängen und erstellt ein mit Nullen gefülltes Latent in der angeforderten Breite, Höhe, Länge und Batch-Größe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungseingabe, die die Videogenerierung in Richtung gewünschter Inhalte lenkt. | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungseingabe, die die Videogenerierung von unerwünschten Inhalten weglenkt. | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Referenzbildern in den latenten Raum verwendet wird. | VAE | Ja | - |
| `width` | Breite der Frames des Ausgabevideos in Pixeln. Standard: 832. | INT | Ja | 16 bis MAX_RESOLUTION, Schritt 16 |
| `height` | Höhe der Frames des Ausgabevideos in Pixeln. Standard: 480. | INT | Ja | 16 bis MAX_RESOLUTION, Schritt 16 |
| `length` | Anzahl der Frames in der generierten Videosequenz. Standard: 97. | INT | Ja | 1 bis MAX_RESOLUTION, Schritt 4 |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videosequenzen. Standard: 1. | INT | Ja | 1 bis 4096 |
| `audio_encoder_output` | Optionale Audiodaten aus der Kodierung, die die Videogenerierung basierend auf dem Audioinhalt beeinflussen können. | AUDIOENCODEROUTPUT | Nein | - |
| `ref_image` | Optionales Referenzbild, das Stil und Inhalt der Videogenerierung vorgibt. Nur das erste Bild im Batch wird verwendet. | IMAGE | Nein | - |

**Hinweis:** Wenn ein Referenzbild bereitgestellt wird, wird das erste Bild im Batch mithilfe bilinearer Interpolation auf die angeforderte `width` und `height` hochskaliert und mit dem VAE kodiert. Dieses Referenz-Latent wird an die positive Konditionierung angehängt, während ein mit Nullen gefülltes Latent derselben Form an die negative Konditionierung angehängt wird. Wenn `audio_encoder_output` bereitgestellt wird, werden die Audio-Embeddings interpoliert und an die positive Konditionierung angehängt, während ein mit Nullen gefülltes Audio-Embedding an die negative Konditionierung angehängt wird. Wenn eine der optionalen Eingaben weggelassen wird, werden mit Nullen gefüllte Platzhalter-Tensoren verwendet: ein Null-Referenz-Latent der Form `[batch_size, 16, 1, height // 8, width // 8]` und/oder Null-Audio-Embeddings der Form `[batch_size, latent_t + 1, 8, 5, 1280]`, wobei `latent_t = ((length - 1) // 4) + 1`.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Modifizierte positive Konditionierung mit eingebundenen Referenzbild- und/oder Audio-Embeddings. | CONDITIONING |
| `negative` | Modifizierte negative Konditionierung mit eingebundenen Referenzbild- und/oder Audio-Embeddings. | CONDITIONING |
| `latent` | Null-initialisierte latente Repräsentation für die Videosequenz, dimensioniert gemäß `width`, `height`, `length` und `batch_size`. Form: `[batch_size, 16, latent_t, height // 8, width // 8]`, wobei `latent_t = ((length - 1) // 4) + 1`. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
