# SamplerDPMPP_SDE

## Überblick

SamplerDPMPP_SDE erstellt einen DPM++ SDE-Sampler (stochastische Differentialgleichung) zur Verwendung im Sampling-Prozess. Dieser Sampler bietet eine stochastische Sampling-Methode mit konfigurierbaren Rauschparametern und Geräteauswahl. Er gibt ein Sampler-Objekt zurück, das in der Sampling-Pipeline verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `eta` | Steuert die Stochastizität des Sampling-Prozesses (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `s_noise` | Steuert die Menge an Rauschen, die während des Samplings hinzugefügt wird (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `r` | Ein Parameter, der das Sampling-Verhalten beeinflusst (Standard: 0.5) | FLOAT | Ja | 0.0 - 100.0 |
| `noise_device` | Wählt das Gerät aus, auf dem Rauschberechnungen durchgeführt werden. Bei Einstellung auf "cpu" wird der `dpmpp_sde`-Sampler erstellt; bei Einstellung auf "gpu" wird der `dpmpp_sde_gpu`-Sampler erstellt (Standard: "gpu") | COMBO | Ja | "gpu"<br>"cpu" |

Hinweis: Alle Eingaben sind als erweiterte Parameter markiert. Die Auswahl von `noise_device` ändert, welche Sampler-Variante erstellt wird: "cpu" wird `dpmpp_sde` zugeordnet und "gpu" wird `dpmpp_sde_gpu` zugeordnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt ein konfiguriertes DPM++ SDE-Sampler-Objekt zur Verwendung in Sampling-Pipelines zurück | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/de.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
