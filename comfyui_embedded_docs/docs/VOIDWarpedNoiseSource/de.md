# VOIDWarpedNoiseSource

Dieser Node wandelt einen LATENT (z. B. die Ausgabe des Nodes VOIDWarpedNoise) in eine NOISE-Quelle um. Dadurch können Sie vorberechnetes gewarpetes Rauschen in Nodes einspeisen, die eine Rauschenquelle erwarten, wie etwa SamplerCustomAdvanced.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `warped_noise` | Latent mit gewarpetem Rauschen von VOIDWarpedNoise | LATENT | Ja | N/A |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `NOISE` | Eine NOISE-Quelle, die das übergebene Latent umschließt und mit SamplerCustomAdvanced verwendet werden kann | NOISE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/de.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
