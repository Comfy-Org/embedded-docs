# Text kodieren Ming Image Edit

Text Encode Ming Image Edit kodiert einen Text-Prompt in Conditioning für die Ming-Bildbearbeitung und mischt optional Referenzbilder ein. Der Prompt und die Referenzbilder werden von einem CLIP-Modell tokenisiert, und wenn ein VAE verbunden ist, werden die Referenzbilder zusätzlich in latente Frames kodiert, die an das Conditioning angehängt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `clip` | Das CLIP-Modell, das zum Tokenisieren des Prompts und der Referenzbilder verwendet wird. | CLIP | Ja | - |
| `vae` | Optionales VAE, das die Referenzbilder in latente Frames kodiert, die an das Conditioning angehängt werden. Ohne VAE konditionieren die Bilder den Textencoder nur über den Vision Tower. | VAE | Nein | - |
| `prompt` | Text-Prompt zum Kodieren. Unterstützt mehrzeilige Eingabe und dynamische Prompts. | STRING | Ja | Mehrzeiliger Text |
| `images` | Erweiterbarer Slot: optionale Referenzbilder, die vom Textencoder gesehen und als saubere Frames an die latente Sequenz angehängt werden. Verbinden Sie 1..8 Bilder (`image_1`, `image_2`, ...); spätere Bilder werden auf das erste skaliert und das gesampelte Latent sollte zu dessen Größe passen. Es werden nur die RGB-Kanäle verwendet. | IMAGE | Nein | 0 bis 8 |

**Hinweis:** Referenzbilder werden in numerischer Reihenfolge ihrer Slot-Namen gelesen, leere Slots werden ignoriert. Referenz-Latents werden nur erzeugt, wenn sowohl `vae` als auch mindestens ein Bild bereitgestellt werden.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `CONDITIONING` | Conditioning, das den kodierten Prompt enthält, plus die Referenz-Latents, wenn ein VAE und Referenzbilder bereitgestellt werden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/de.md)

---
**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`
