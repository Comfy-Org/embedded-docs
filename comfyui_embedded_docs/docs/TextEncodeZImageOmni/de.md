# TextEncodeZImageOmni

TextEncodeZImageOmni kodiert einen Text-Prompt zusammen mit bis zu drei optionalen Referenzbildern in ein Konditionierungsformat für Bildgenerierungsmodelle. Der Prompt wird tokenisiert und mit dem CLIP-Modell kodiert, und jedes verbundene Bild kann optional durch einen Vision-Encoder und/oder eine VAE verarbeitet werden, sodass visuelle Referenzen zusammen mit dem Text eingebettet werden. Dieser Node ist als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, das zum Tokenisieren und Kodieren des Text-Prompts verwendet wird. | CLIP | Ja |  |
| `image_encoder` | Ein optionales Vision-Encoder-Modell. Wenn angegeben, wird es zum Kodieren der Eingabebilder verwendet, und die resultierenden Embeddings werden der Konditionierung hinzugefügt. | CLIP_VISION | Nein |  |
| `prompt` | Der zu kodierende Text-Prompt. Unterstützt mehrzeilige Eingabe und dynamische Prompts. | STRING | Ja |  |
| `auto_resize_images` | Wenn aktiviert (Standard: True), werden Eingabebilder vor der VAE-Kodierung automatisch so skaliert, dass ihre Gesamtpixelanzahl nahe bei 1024x1024 liegt, wobei die Dimensionen auf Vielfache von 8 gerundet werden. | BOOLEAN | Ja | True<br>False |
| `vae` | Ein optionales VAE-Modell. Wenn angegeben, wird es zum Kodieren der Eingabebilder in latente Repräsentationen verwendet, die der Konditionierung als Referenz-Latents hinzugefügt werden. | VAE | Nein |  |
| `image1` | Das erste optionale Referenzbild. | IMAGE | Nein |  |
| `image2` | Das zweite optionale Referenzbild. | IMAGE | Nein |  |
| `image3` | Das dritte optionale Referenzbild. | IMAGE | Nein |  |

**Hinweis:** Der Node akzeptiert maximal drei Bilder (`image1`, `image2`, `image3`). Die Eingaben `image_encoder` und `vae` werden nur verwendet, wenn mindestens ein Bild bereitgestellt wird; wenn beide verbunden sind, wird jedes Bild von beiden verarbeitet. Wenn `auto_resize_images` True ist und eine `vae` verbunden ist, werden Bilder vor der Kodierung so skaliert, dass ihre Gesamtpixelanzahl nahe bei 1024x1024 liegt. Wenn keine Bilder bereitgestellt werden, wird nur der Text-Prompt kodiert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die endgültige Konditionierungsausgabe. Sie enthält den kodierten Text-Prompt und kann, wenn Bilder bereitgestellt werden, kodierte Bild-Embeddings, Referenz-Latents und zusätzliche Text-Embeddings enthalten, die aus der Bildplatzhalter-Vorlage abgeleitet wurden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/de.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
