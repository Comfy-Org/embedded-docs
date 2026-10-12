# Leeres Latent-Audio

Empty Latent Audio erzeugt einen leeren latenten Tensor für die Audiobearbeitung. Er generiert eine leere latente Audio-Repräsentation mit einer angegebenen Dauer und Batch-Größe, die als Ausgangspunkt für Arbeitsabläufe zur Audioerzeugung oder -verarbeitung verwendet werden kann. Der Node berechnet automatisch die geeigneten latenten Dimensionen basierend auf der Audiodauer und der Abtastrate.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `seconds` | Die Dauer des Audios in Sekunden (Standard: 47.6) | FLOAT | Ja | 1.0 - 1000.0 |
| `batch_size` | Die Anzahl der latenten Bilder im Batch (Standard: 1) | INT | Ja | 1 - 4096 |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Gibt einen leeren latenten Tensor für die Audiobearbeitung mit der angegebenen Dauer und Batch-Größe zurück. Der Tensor hat die Form [batch_size, 64, length], wobei length aus der Audiodauer und der Abtastrate berechnet wird. Die Ausgabe enthält außerdem Metadaten, die angeben, dass der Typ "audio" ist, sowie ein zeitliches Downscaling-Verhältnis von 2048. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/de.md)

---
**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`
