# Wan22FunControlToVideo

Der Node Wan22FunControlToVideo bereitet Konditionierungsdaten und einen leeren Latent-Tensor für die Videogenerierung mit dem Wan-Videomodell vor. Er kodiert optionale Referenzbilder und Steuervideos in den Latent-Raum, hängt sie an die positive und negative Konditionierung an und erstellt einen mit Nullen gefüllten Latent-Tensor mit den korrekten räumlichen und zeitlichen Dimensionen für das angeforderte Video.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungseingabe zur Steuerung der Videogenerierung | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungseingabe zur Steuerung der Videogenerierung | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren von Bildern in den Latent-Raum verwendet wird | VAE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames in der Videosequenz (Standard: 81, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der zu generierenden Videosequenzen (Standard: 1) | INT | Ja | 1 bis 4096 |
| `ref_image` | Optionales Referenzbild, das visuelle Anleitung für die Generierung liefert | IMAGE | Nein | - |
| `control_video` | Optionales Steuervideo, das den Generierungsprozess steuert | IMAGE | Nein | - |

**Hinweis:** Der Parameter `length` wird in Schritten von 4 Frames verarbeitet, und der Node wendet beim Aufbau des Latent-Raums automatisch eine zeitliche Skalierung an. Wenn `ref_image` angegeben wird, wird nur dessen erstes Frame kodiert (auf `width` x `height` skaliert) und als Referenz-Latents an die Konditionierung angehängt. Wenn `control_video` angegeben wird, wird es auf `length` Frames gekürzt, skaliert, kodiert und in das von der Konditionierung verwendete Concat-Latent eingefügt. Das verkettete Latent wird entlang der Kanal-Dimension dupliziert, und sein Kanal-Layout hängt von der Latent-Kanalanzahl des VAE ab (48 Kanäle verwenden das Wan-2.2-Format, andernfalls das Wan-2.1-Format). Der Parameter `start_image` wird in der Ausführungslogik referenziert, ist aber nicht im Eingabeschema des Nodes enthalten, sodass er nicht über die Node-Oberfläche festgelegt werden kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierung mit hinzugefügten videospezifischen Latent-Daten, einschließlich Concat-Latent, Maske und optionalen Referenz-Latents | CONDITIONING |
| `negative` | Negative Konditionierung mit hinzugefügten videospezifischen Latent-Daten, einschließlich Concat-Latent, Maske und optionalen Referenz-Latents | CONDITIONING |
| `latent` | Leerer Latent-Tensor, der für die Videogenerierung vorbereitet ist und entsprechend Batch-Größe, Latent-Kanälen, Länge, Höhe und Breite dimensioniert ist | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/de.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
