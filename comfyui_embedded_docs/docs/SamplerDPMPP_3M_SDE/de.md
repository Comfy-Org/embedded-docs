# SamplerDPMPP_3M_SDE

Der Node `SamplerDPMPP_3M_SDE` erstellt einen DPM++ 3M SDE Sampler zur Verwendung im Sampling-Prozess. Dieser Sampler verwendet eine stochastische Differentialgleichungsmethode dritter Ordnung mit mehreren Schritten und konfigurierbaren Rauschparametern. Der Node ermöglicht die Auswahl, ob Rauschberechnungen auf der GPU oder CPU durchgeführt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `eta` | Steuert die Stochastizität des Sampling-Prozesses (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `s_noise` | Steuert die Menge des während des Samplings hinzugefügten Rauschens (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `noise_device` | Wählt das Gerät für Rauschberechnungen, entweder GPU oder CPU (Standard: "gpu") | COMBO | Ja | "gpu"<br>"cpu" |

Hinweis: Alle drei Eingaben sind erweiterte Parameter.

Wenn `noise_device` auf "cpu" gesetzt ist, wird der Standard-`dpmpp_3m_sde`-Sampler erstellt; wenn er auf "gpu" gesetzt ist, wird der GPU-beschleunigte `dpmpp_3m_sde_gpu`-Sampler erstellt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt ein konfiguriertes Sampler-Objekt zur Verwendung in Sampling-Workflows zurück | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/de.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
