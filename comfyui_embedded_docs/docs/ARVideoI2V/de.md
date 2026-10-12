# ARVideoI2V

Dieser Node bereitet ein Setup zur Bild-zu-Video-Generierung für AR-Videomodelle (autoregressiv) vor, die Causal Forcing oder Self-Forcing verwenden. Er kodiert ein Startbild mithilfe eines VAE in den latenten Raum und speichert es in den Transformer-Optionen des Modells, sodass der Video-Sampling-Prozess den KV-Cache vor der Entrauschung initialisieren kann. Er verwendet denselben Text-zu-Video-Modell-Checkpoint, sodass keine separate Bild-zu-Video-Architektur erforderlich ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das AR-Videomodell, das für die Generierung verwendet wird. | MODEL | Ja | - |
| `vae` | Das VAE-Modell, das zum Kodieren des Startbilds in den latenten Raum verwendet wird. | VAE | Ja | - |
| `start_image` | Das Anfangsbild, das als erstes Einzelbild des generierten Videos dient. Es wird nur das erste Bild im Eingabe-Batch verwendet, und nur dessen RGB-Kanäle werden kodiert. | IMAGE | Ja | - |
| `width` | Die Breite der generierten Video-Frames (Standard: 832). | INT | Ja | 16 bis 8192 (Schritt: 16) |
| `height` | Die Höhe der generierten Video-Frames (Standard: 480). | INT | Ja | 16 bis 8192 (Schritt: 16) |
| `length` | Die Gesamtzahl der Frames des generierten Videos (Standard: 81). | INT | Ja | 1 bis 1024 (Schritt: 4) |
| `batch_size` | Die Anzahl der Videosequenzen, die in einem einzelnen Batch generiert werden sollen (Standard: 1). | INT | Ja | 1 bis 64 |

Hinweis: Das Startbild wird vor der Kodierung auf die angegebenen `width` und `height` skaliert. Die latente zeitliche Dimension wird als `((length - 1) // 4) + 1` berechnet, und die latenten räumlichen Dimensionen sind `height / 8` und `width / 8`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das geklonte Modell mit dem kodierten Startbild in seinen Transformer-Optionen (`ar_config.initial_latent`); der Sampler verwendet diese, um den KV-Cache vor der Entrauschung zu initialisieren. | MODEL |
| `LATENT` | Ein mit Nullen gefüllter latenter Tensor mit der Form `[batch_size, 16, lat_t, height // 8, width // 8]`, wobei `lat_t = ((length - 1) // 4) + 1`. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/de.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
