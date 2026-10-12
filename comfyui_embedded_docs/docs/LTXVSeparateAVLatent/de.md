# LTXVSeparateAVLatent

Der Node LTXVSeparateAVLatent teilt einen kombinierten audio-visuellen Latent in zwei separate Latents auf: einen mit den Videodaten und einen mit den Audiodaten. Dies funktioniert mit jedem audio-visuellen Modell, wie z. B. LTXV oder MiniMax H3. Der `samples`-Tensor wird entlang seiner ersten Dimension aufgeteilt, wobei das erste Element zum Video-Latent und das zweite Element zum Audio-Latent wird; falls eine `noise_mask` vorhanden ist, wird sie auf die gleiche Weise aufgeteilt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `av_latent` | Die kombinierte audio-visuelle Latent-Darstellung, die in Video- und Audio-Latents aufgeteilt werden soll. | LATENT | Ja | N/A |

**Hinweis:** Der `samples`-Tensor des Eingabe-Latents sollte mindestens zwei Elemente entlang der ersten Dimension (Batch-Dimension) haben. Das erste Element wird für das Video-Latent verwendet, das zweite Element für das Audio-Latent. Falls eine `noise_mask` vorhanden ist, wird sie auf die gleiche Weise aufgeteilt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video_latent` | Die Latent-Darstellung, die die getrennten Videodaten enthält. | LATENT |
| `audio_latent` | Die Latent-Darstellung, die die getrennten Audiodaten enthält. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/de.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
