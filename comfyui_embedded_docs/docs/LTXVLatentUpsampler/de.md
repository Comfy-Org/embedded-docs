# LTXVLatentUpsampler

Der Node `LTXVLatentUpsampler` erhöht die räumliche Auflösung einer Video-Latentdarstellung um den Faktor zwei. Er verwendet ein spezielles Upscale-Modell, um die Latent-Daten zu verarbeiten, die zuerst denormalisiert und anschließend mithilfe der Kanalstatistiken des bereitgestellten VAE renormiert werden. Dieser Node ist für Video-Workflows innerhalb des Latentraums konzipiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `samples` | Die eingegebene Latentdarstellung des Videos, das hochskaliert werden soll. | LATENT | Ja |  |
| `upscale_model` | Das geladene Modell, das für die 2-fache Hochskalierung der Latent-Daten verwendet wird. | LATENT_UPSCALE_MODEL | Ja |  |
| `vae` | Das VAE-Modell, das verwendet wird, um die eingegebenen Latents vor der Hochskalierung zu denormalisieren und die ausgegebenen Latents anschließend zu normalisieren. | VAE | Ja |  |

Hinweis: Dieser Node ist in ComfyUI als experimentell gekennzeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Die hochskalierte Latentdarstellung, deren räumliche Dimensionen im Vergleich zur Eingabe verdoppelt sind. Das ausgegebene Latent hat dieselbe Batch-Größe, Anzahl an Kanälen und zeitliche Länge wie die Eingabe. Der `noise_mask` aus der Eingabe wird, falls vorhanden, aus der Ausgabe entfernt. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/de.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
