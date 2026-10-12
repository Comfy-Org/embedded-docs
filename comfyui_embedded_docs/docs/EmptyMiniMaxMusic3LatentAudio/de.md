# EmptyMiniMaxMusic3LatentAudio

Dieser Node erstellt ein leeres (mit Nullen gefülltes) Audio-Latent für das MiniMax Music3-Modell. Er wandelt die angeforderte Dauer in Sekunden in die entsprechende Anzahl an Audioframes um und erzeugt einen leeren Latent-Tensor der richtigen Größe, der als Ausgangspunkt für die Musikgenerierung verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Die Dauer des Audio-Latents in Sekunden (Standard: 120.0). Der Wert wird in Audioframes umgerechnet und auf die vom Modell unterstützten Dauerbeschränkungen begrenzt. | FLOAT | Ja | 0.04 bis (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), Schritt 0.04 |
| `batch_size` | Die Anzahl der in einem Batch zu erzeugenden Audio-Latents (Standard: 1). | INT | Ja | 1 bis 4096 |

Hinweis: Der Wert `seconds` wird auf den nächstgelegenen Audioframe gerundet und auf mindestens 1 Frame sowie maximal `MAX_AUDIO_FRAMES` Frames begrenzt, sodass die tatsächliche Latent-Länge geringfügig vom exakt eingegebenen Wert abweichen kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `LATENT` | Ein mit Nullen gefüllter Audio-Latent-Tensor der Form (batch_size, 128, latent_length). Enthält Metadaten, die das Sample als Audiodaten mit einem zeitlichen Downscale-Verhältnis von 512 kennzeichnen. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/de.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
