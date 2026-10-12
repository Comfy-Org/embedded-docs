# Leeres LTXV Latent-Audio

Der LTXV Empty Latent Audio-Node erstellt einen Batch leerer (mit Nullen gefüllter) latenter Audio-Tensoren. Er liest die Konfiguration eines verbundenen Audio-VAE-Modells, um die korrekten latenten Dimensionen zu bestimmen, etwa die Anzahl der Kanäle und Frequenz-Bins, und berechnet aus der Frame-Anzahl und der Frame-Rate, wie viele Audio-Latents benötigt werden. Das resultierende leere Latent kann als Ausgangspunkt für Workflows zur Audiogenerierung oder -manipulation verwendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `frames_number` | Anzahl der Frames. Der Standardwert ist 97. | INT | Ja | 1 bis 1000 |
| `frame_rate` | Anzahl der Frames pro Sekunde. Der Standardwert ist 25.0. Diese Eingabe akzeptiert entweder FLOAT- oder INT-Werte. | FLOAT | Ja | 1.0 bis 1000.0 |
| `batch_size` | Die Anzahl der latenten Audio-Samples im Batch. Der Standardwert ist 1. | INT | Ja | 1 bis 4096 |
| `audio_vae` | Das Audio-VAE-Modell, von dem die Konfiguration abgerufen wird. Angezeigt als "Audio VAE". | VAE | Ja | N/A |

**Hinweis:** Die Eingabe `audio_vae` ist obligatorisch. Der Node löst einen Fehler aus, wenn sie nicht angegeben wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `Latent` | Ein leerer latenter Audio-Tensor mit der Form (batch_size, z_channels, num_audio_latents, audio_freq), wobei die Kanalanzahl und die Frequenz-Bins vom Audio-VAE stammen und die Anzahl der Audio-Latents aus `frames_number` und `frame_rate` abgeleitet wird. Die Ausgabe enthält außerdem ein `type`-Feld, das auf "audio" gesetzt ist. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/de.md)

---
**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`
