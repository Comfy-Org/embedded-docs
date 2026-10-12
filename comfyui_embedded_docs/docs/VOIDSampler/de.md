# VOIDSampler

VOIDSampler ist ein spezialisierter DDIM-Sampler, der für VOID-Inpainting-Modelle entwickelt wurde. Er reproduziert den exakten Denoising-Prozess, mit dem VOID trainiert wurde, und überspringt die Rauschskalierung, die standardmäßige KSampler anwenden. Verwenden Sie diesen Node zusammen mit SamplerCustom oder SamplerCustomAdvanced, kombiniert mit RandomNoise oder VOIDWarpedNoiseSource.

## Eingaben

Dieser Node hat keine konfigurierbaren Eingabeparameter. Er ist ein eigenständiger Sampler, der einen festen DDIM-Sampling-Algorithmus anwendet.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| *Keine Eingaben* | Dieser Node akzeptiert keine Eingabeparameter. | - | - | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `SAMPLER` | Ein Sampler-Objekt, das den VOID-DDIM-Algorithmus implementiert und bereit ist, mit SamplerCustom- oder SamplerCustomAdvanced-Nodes verbunden zu werden. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/de.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
