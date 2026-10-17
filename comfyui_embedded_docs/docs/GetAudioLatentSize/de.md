# Get Audio Latent Size

Liest ein Audio-Latent und gibt dessen Länge, die Anzahl der Audiokanäle und die Batch-Größe zurück, sodass diese Werte wiederverwendet werden können, ohne das Audio zu dekodieren. Verwenden Sie ihn, um Rauschmasken zu dimensionieren oder Audio- und Videolängen vor dem Sampling anzugleichen. Die gemessenen Werte werden außerdem direkt am Node selbst angezeigt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latent` | Das zu untersuchende Audio- oder Audio/Video-Latent. Wenn das Latent mehrere Streams enthält, wird der Audio-Stream gemessen. | LATENT | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `length` | Die Länge des Audio-Latents, angegeben in Latent-Zellen statt in Audio-Samples. | INT |
| `audio_channels` | Die Anzahl der Audiokanäle. Latents ohne Audiokanal-Dimension geben einen Kanal an. | INT |
| `batch_size` | Die Anzahl der Latents im Batch. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/de.md)

---
**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`
