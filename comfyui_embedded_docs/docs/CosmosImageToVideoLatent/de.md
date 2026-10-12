# CosmosImageToVideoLatent

Der Knoten CosmosImageToVideoLatent erstellt eine Video-Latent-Darstellung aus Eingabebildern. Er erzeugt ein leeres Video-Latent mit der angeforderten Breite, Höhe und Anzahl von Frames und kodiert dann optional ein Startbild in die Anfangsframes und/oder ein Endbild in die Endframes. Wenn Bilder bereitgestellt werden, erzeugt er außerdem eine Rauschmaske, damit die kodierten Frames während der Generierung fixiert bleiben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | Das VAE-Modell, das verwendet wird, um die Bilder in den Video-Latentraum zu kodieren. | VAE | Ja | - |
| `width` | Die Breite des Ausgabevideos in Pixeln (Standard: 1280). | INT | Ja | 16 bis MAX_RESOLUTION (Schritt: 16) |
| `height` | Die Höhe des Ausgabevideos in Pixeln (Standard: 704). | INT | Ja | 16 bis MAX_RESOLUTION (Schritt: 16) |
| `length` | Die Gesamtzahl der Frames im Video (Standard: 121). | INT | Ja | 1 bis MAX_RESOLUTION (Schritt: 8) |
| `batch_size` | Die Anzahl der zu generierenden Video-Latents (Standard: 1). | INT | Ja | 1 bis 4096 |
| `start_image` | Optionales Bild oder optionale Bildsequenz, die am Anfang des Videos kodiert wird. | IMAGE | Nein | - |
| `end_image` | Optionales Bild oder optionale Bildsequenz, die am Ende des Videos kodiert wird. | IMAGE | Nein | - |

**Hinweis:**
- Wenn weder `start_image` noch `end_image` bereitgestellt wird, gibt der Knoten ein leeres Latent ohne Rauschmaske zurück.
- Wenn `start_image` bereitgestellt wird, wird es in die ersten Frames des Latents kodiert, und diese Frames werden mit dem Rauschmaskenwert 0 markiert (beibehalten). Wenn `end_image` bereitgestellt wird, wird es in die letzten Frames kodiert, und diese Frames werden mit dem Rauschmaskenwert 0 markiert. Die übrigen Frames behalten einen Maskenwert von 1.
- Das Latent hat 16 Kanäle und seine räumlichen Abmessungen sind `height / 8` mal `width / 8`. Die Anzahl der Latent-Frames ist `((length - 1) // 8) + 1`.
- `batch_size` wiederholt das Latent und, sofern vorhanden, die Rauschmaske.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Das generierte Video-Latent, das die optional kodierten Start- und/oder Endbilder enthält und, wenn Bilder bereitgestellt werden, eine passende Rauschmaske mit dem Wert 0 für die beibehaltenen Frames. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/de.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
