# CosmosPredict2ImageToVideoLatent

Erstellt Video-Latents für den Cosmos Predict2 Image-to-Video-Workflow. Der Node kann ein leeres Video-Latent mit einer bestimmten Größe und Länge erzeugen oder kodierte Start- und/oder Endbilder in die Sequenz einfügen, sodass diese Frames während der Generierung beibehalten werden. Jedes bereitgestellte Bild wird auf die angeforderten `width` und `height` skaliert und mit dem angegebenen VAE kodiert, bevor es an den Anfang und/oder das Ende der Latent-Sequenz gesetzt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | Das VAE-Modell, das zum Kodieren der Start- und Endbilder in den Latent-Raum verwendet wird | VAE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 848, muss ein Vielfaches von 16 sein) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 480, muss ein Vielfaches von 16 sein) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames in der Videosequenz (Standard: 93) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der zu generierenden Videosequenzen (Standard: 1) | INT | Ja | 1 bis 4096 |
| `start_image` | Optionales Startbild für die Videosequenz | IMAGE | Nein | - |
| `end_image` | Optionales Endbild für die Videosequenz | IMAGE | Nein | - |

**Hinweis:** Wenn weder `start_image` noch `end_image` angegeben ist, gibt der Node einfach ein leeres Latent mit der angeforderten Größe und Länge zurück. Wenn eines oder beide Bilder angegeben sind, werden sie auf `width` und `height` skaliert, mit dem `vae` kodiert und an den Anfang und/oder das Ende der Latent-Sequenz gesetzt. Die entsprechenden Bereiche werden in der Noise-Maske markiert, damit sie während der Generierung beibehalten werden. Die kodierten Latents werden in das Wan 2.1-Latent-Format konvertiert, und das resultierende Latent und die Maske werden `batch_size`-mal wiederholt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Das generierte Video-Latent, das `samples` (die Video-Latent-Sequenz) enthält und, wenn mindestens eines von `start_image` oder `end_image` angegeben ist, eine `noise_mask`, die die Frames markiert, die während der Generierung beibehalten werden sollen | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/de.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
