# MiniMax H3 Bild zu Video

Dieser Node bereitet die Konditionierung und das leere Latent vor, die zur Generierung eines Videos mit dem MiniMax H3-Modell benötigt werden. Er nimmt einen Text-Prompt sowie optional Bilder für den ersten und/oder letzten Frame des Videos entgegen und wandelt sie in Modelleingaben um. Keyframe-Bilder werden skaliert, kodiert und an die Konditionierung am Anfang und Ende des Videos angehängt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | CLIP-Modell, das verwendet wird, um den Prompt zu tokenisieren und die Keyframe-Bilder in die Konditionierung zu kodieren. | CLIP | Ja |  |
| `vae` | VAE-Modell, das verwendet wird, um die Keyframe-Bilder in den latenten Raum zu kodieren, wenn Keyframe-Bilder bereitgestellt werden. | VAE | Ja |  |
| `prompt` | Text-Prompt, der das zu generierende Video beschreibt. Unterstützt mehrere Zeilen und dynamische Prompts. | STRING | Ja |  |
| `width` | Breite des Videos in Pixeln (Standard: 1344). | INT | Ja | 32 bis MAX_RESOLUTION (Schrittweite 32) |
| `height` | Höhe des Videos in Pixeln (Standard: 768). | INT | Ja | 32 bis MAX_RESOLUTION (Schrittweite 32) |
| `length` | Frame-Anzahl bei 24 fps, aufgerundet auf das 17k+5-Raster des Modells (124 = ~5s; der trainierte Bereich ist ~124–362, längere Werte sind nicht getestet) (Standard: 124). | INT | Ja | 5 bis 3600 (Schrittweite 17) |
| `first_frame` | Optionales Bild, das als erster Frame des Videos verwendet wird. Es wird auf die volle Canvas-Größe gestreckt, sodass sein Seitenverhältnis nicht erhalten bleibt. Nur das erste Bild des Eingabe-Batches wird verwendet. | IMAGE | Nein |  |
| `last_frame` | Optionales Bild, das als letzter Frame des Videos verwendet wird. Es wird zugeschnitten, um die Canvas abzudecken, wobei sein Seitenverhältnis erhalten bleibt. Nur das erste Bild des Eingabe-Batches wird verwendet. | IMAGE | Nein |  |

Wenn `first_frame` und/oder `last_frame` bereitgestellt werden, werden die Keyframe-Bilder mit dem VAE kodiert und jeweils bei Frame 0 bzw. am letzten Frame an die Konditionierung angehängt. Wenn keines von beiden bereitgestellt wird, arbeitet der Node ausschließlich mit dem Prompt. Die angeforderte `length` wird auf die nächstgelegene gültige Frame-Anzahl (17k + 5) aufgerundet, sodass die effektive Frame-Anzahl geringfügig höher sein kann als angefordert.

Das Audio-Video-Latent wird als leeres Paar erstellt, das der angeforderten `width`, `height` und der aufgerundeten Frame-Anzahl entspricht. Der Audioanteil wird anhand derselben Frame-Anzahl mit 40 Audio-Frames pro Sekunde dimensioniert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Konditionierung, die den kodierten Prompt und, wenn Keyframe-Bilder bereitgestellt werden, die kodierten Keyframes und die Frame-Anzahl für das MiniMax H3-Modell enthält. | CONDITIONING |
| `latent` | Leeres Audio-Video-Latent, das den zu generierenden Inhalt mit der angeforderten Breite, Höhe und Frame-Anzahl darstellt. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
