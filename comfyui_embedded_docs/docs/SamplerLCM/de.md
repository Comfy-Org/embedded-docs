# SamplerLCM

Dieser Node stellt einen LCM-Sampler (Latent Consistency Model) mit einstellbarem Rauschen pro Schritt bereit. Er ermöglicht Ihnen die Kontrolle darüber, wie viel Rauschen während des Samplings angewendet wird: `s_noise` wirkt als Multiplikator auf die Trainings-Rauschskala des Modells, und der Rauschpegel kann vom ersten bis zum letzten Schritt variieren. Der konfigurierte Sampler kann anschließend in einen Sampling-Workflow eingebunden werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `s_noise` | Rauschmultiplikator pro Schritt am ersten Schritt (1.0 = entspricht dem Training). Standard: 1.0. | FLOAT | Ja | 0.0 bis 64.0 (Schritt: 0.01) |
| `s_noise_end` | Rauschmultiplikator pro Schritt am letzten Schritt. Für einen konstanten Verlauf gleich `s_noise` setzen. Standard: 1.0. | FLOAT | Ja | 0.0 bis 64.0 (Schritt: 0.01) |
| `noise_clip_std` | Begrenzt das Rauschen pro Schritt auf +/- N*std. 0 deaktiviert. Standard: 0.0. | FLOAT | Ja | 0.0 bis 10.0 (Schritt: 0.01) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `SAMPLER` | Das konfigurierte LCM-Sampler-Objekt, bereit zur Verwendung in einem Sampling-Workflow. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/de.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
