# WanSoundImageToVideo

Der Node WanSoundImageToVideo bereitet eine Konditionierung und einen leeren latenten Video-Tensor für die Wan-Sound-zu-Video-Generierung vor. Er kann optional eine Audiokodierung, ein Referenzbild, ein Steuervideo und eine Bewegungsreferenz einbeziehen, um das generierte Video zu lenken.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Conditioning-Prompts, die festlegen, welche Inhalte im generierten Video erscheinen sollen | CONDITIONING | Ja | - |
| `negative` | Negative Conditioning-Prompts, die festlegen, welche Inhalte im generierten Video vermieden werden sollen | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Referenzbildern, Bewegungsreferenzen und Steuervideo-Frames in latente Repräsentationen verwendet wird | VAE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames im generierten Video (Standard: 77, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `audio_encoder_output` | Optionale Audiokodierung, die die Videogenerierung basierend auf Klangeigenschaften beeinflussen kann. Wenn angegeben, werden die Audio-Features interpoliert und zur Konditionierung der Videogenerierung verwendet. | AUDIO_ENCODER_OUTPUT | Nein | - |
| `ref_image` | Optionales Referenzbild, das visuelle Vorgaben für den Videoinhalt liefert. Das Bild wird auf die angegebene Breite und Höhe hochskaliert und anschließend in eine latente Repräsentation kodiert. Nur das erste Bild der Eingabe wird als Referenz verwendet. | IMAGE | Nein | - |
| `control_video` | Optionales Steuervideo, das Bewegung und Struktur des generierten Videos vorgibt. Das Video wird hochskaliert und kodiert und anschließend zur Konditionierung der Ausgabe verwendet. Nur die ersten `length` Frames werden verwendet. | IMAGE | Nein | - |
| `ref_motion` | Optionale Bewegungsreferenz, die Vorgaben für Bewegungsmuster im Video liefert. Wenn die Eingabe mehr als 73 Frames enthält, werden nur die letzten 73 verwendet. Wenn weniger als 73 Frames bereitgestellt werden, wird die Sequenz mit neutralen Frames aufgefüllt. | IMAGE | Nein | - |

Hinweis: Alle optionalen Eingaben können unabhängig voneinander oder zusammen verwendet werden. Der Node modifiziert die bereitgestellte `positive`- und `negative`-Konditionierung basierend darauf, welche optionalen Eingaben verbunden sind.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Verarbeitete positive Konditionierung, die für die Videogenerierung modifiziert wurde, einschließlich Audio-Embeddings, Referenz-Latents, Bewegungsreferenzen und Steuervideo-Konditionierung, wenn die entsprechenden optionalen Eingaben bereitgestellt werden | CONDITIONING |
| `negative` | Verarbeitete negative Konditionierung, die für die Videogenerierung modifiziert wurde, einschließlich Audio-Embeddings (auf null gesetzt), Referenz-Latents, Bewegungsreferenzen und Steuervideo-Konditionierung, wenn die entsprechenden optionalen Eingaben bereitgestellt werden | CONDITIONING |
| `latent` | Leerer latenter Video-Tensor, der als Ausgangspunkt für die Generierung verwendet wird. Der latente Tensor hat die Form `[batch_size, 16, latent_t, height/8, width/8]`, wobei `latent_t` als `((length - 1) // 4) + 1` berechnet wird. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
