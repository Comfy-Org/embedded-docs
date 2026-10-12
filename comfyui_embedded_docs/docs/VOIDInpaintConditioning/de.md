# VOIDInpaintConditioning

Der Node VOIDInpaintConditioning bereitet die für Inpainting mit CogVideoX-Modellen benötigten Konditionierungsdaten vor. Er nimmt ein Quellvideo und eine vorverarbeitete Quadmask, kodiert beide durch den VAE und kombiniert sie zu einem 32-Kanal-Konditionierungssignal (16 Kanäle aus der Maske + 16 Kanäle aus dem maskierten Video), das das Modell verwendet, um die maskierten Bereiche zu füllen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierung, die um die Inpainting-Latent-Informationen erweitert werden soll | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, die um die Inpainting-Latent-Informationen erweitert werden soll | CONDITIONING | Ja | - |
| `vae` | Das VAE-Modell, das verwendet wird, um die Maske und das maskierte Video in den latenten Raum zu kodieren | VAE | Ja | - |
| `video` | Quellvideo-Frames [T, H, W, 3] | IMAGE | Ja | - |
| `quadmask` | Vorverarbeitete Quadmask von VOIDQuadmaskPreprocess [T, H, W] | MASK | Ja | - |
| `width` | Die Breite, auf die das Video und die Maske skaliert werden (Standard: 672) | INT | Ja | 16 bis MAX_RESOLUTION (Schritt: 8) |
| `height` | Die Höhe, auf die das Video und die Maske skaliert werden (Standard: 384) | INT | Ja | 16 bis MAX_RESOLUTION (Schritt: 8) |
| `length` | Anzahl der zu verarbeitenden Pixel-Frames. Für CogVideoX-Fun-V1.5 (patch_size_t=2) muss latent_t gerade sein — Längen, die ein ungerades latent_t erzeugen, werden abgerundet (z. B. 49 → 45) (Standard: 45) | INT | Ja | 1 bis MAX_RESOLUTION (Schritt: 1) |
| `batch_size` | Die Batch-Größe für das ausgegebene Rausch-Latent (Standard: 1) | INT | Ja | 1 bis 64 |

**Hinweis:** Da CogVideoX-Fun-V1.5 `patch_size_t=2` verwendet, muss das kodierte Latent eine gerade zeitliche Dimension haben. Wenn `length` ein ungerades `latent_t` erzeugen würde, rundet der Node es automatisch auf den nächsten gültigen Wert ab und protokolliert eine Warnung. Die Verwendung eines ungeraden `latent_t` beschädigt das letzte Frame durch zirkuläres Padding, was zu sichtbarem Ruckeln oder verschwindenden Motiven gegen Ende des dekodierten Videos führen kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierung mit hinzugefügten Inpainting-Latent-Informationen | CONDITIONING |
| `negative` | Die negative Konditionierung mit hinzugefügten Inpainting-Latent-Informationen | CONDITIONING |
| `latent` | Ein mit Nullen gefüllter Rausch-Latent-Tensor mit Form [batch_size, 16, latent_t, latent_h, latent_w] | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/de.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
