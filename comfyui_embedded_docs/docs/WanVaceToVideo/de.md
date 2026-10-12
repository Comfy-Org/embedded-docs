# WanVaceToVideo

Der WanVaceToVideo-Node bereitet Videokonditionierungsdaten für VACE-gesteuerte Videogenerierungsmodelle vor. Er kombiniert positive und negative Konditionierung mit einem optionalen Kontrollvideo, Kontrollmasken und einem Referenzbild, kodiert sie durch ein VAE und gibt aktualisierte Konditionierung, einen leeren Latent-Tensor und einen Trim-Wert aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positiver Konditionierungseingang zur Steuerung der Generierung | CONDITIONING | Ja | - |
| `negative` | Negativer Konditionierungseingang zur Steuerung der Generierung | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Bildern und Videoframes verwendet wird | VAE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames im Video (Standard: 81, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `strength` | Konditionierungsstärke für die VACE-Steuerung (Standard: 1.0, Schritt: 0.01). Dies ist keine LoRA-Stärke. LoRA-Gewichte werden über separate LoRA-Nodes angewendet. | FLOAT | Ja | 0.0 bis 1000.0 |
| `control_video` | Optionales Eingabevideo für die Kontrollkonditionierung. Wenn es nicht bereitgestellt wird, wird automatisch ein neutralgraues Video erstellt. | IMAGE | Nein | - |
| `control_masks` | Optionale Masken, die bestimmen, welche Teile des Kontrollvideos aktiv sind. Wenn keine angegeben werden, wird eine vollständig weiße Maske verwendet. | MASK | Nein | - |
| `reference_image` | Optionales Referenzbild für zusätzliche Konditionierung. Wenn es bereitgestellt wird, wird es kodiert und der Latent-Sequenz vorangestellt. Nur das erste Bild wird verwendet. | IMAGE | Nein | - |

**Hinweis:** Wenn `control_video` bereitgestellt wird, wird es auf `length` Frames gekürzt und auf die angegebene `width` und `height` hochskaliert; wenn es weniger Frames als `length` hat, werden die fehlenden Frames mit neutralem Grau (Wert 0.5) aufgefüllt. Wenn es nicht bereitgestellt wird, wird automatisch ein neutralgraues Video mit `length` Frames erstellt. `control_masks` werden auf die angegebene `width` und `height` hochskaliert, auf `length` Frames gekürzt und bei kürzerer Länge mit dem Wert 1.0 aufgefüllt. Die Maske teilt das Kontrollvideo in inaktive und reaktive Teile, die jeweils VAE-kodiert und entlang der Kanal-Dimension konkateniert werden; die Maske wird außerdem auf Latent-Auflösung herunterskaliert. Wenn `reference_image` bereitgestellt wird, wird dessen erstes Bild VAE-kodiert und der Latent-Sequenz vorangestellt, und `trim_latent` gibt die Anzahl der hinzugefügten Latent-Frames an. Die Anzahl der Latent-Frames wird als `((length - 1) // 4) + 1` berechnet, und die räumlichen Latent-Dimensionen sind `height / 8` und `width / 8`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierung, auf die Videokontrolldaten (vace_frames, vace_mask, vace_strength) angewendet wurden | CONDITIONING |
| `negative` | Negative Konditionierung, auf die Videokontrolldaten (vace_frames, vace_mask, vace_strength) angewendet wurden | CONDITIONING |
| `latent` | Leerer Latent-Tensor, bereit für die Videogenerierung, mit der Form [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Anzahl der zu trimmenden Latent-Frames, wenn ein Referenzbild verwendet wird; 0, wenn kein Referenzbild bereitgestellt wird | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/de.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
