# SamplerDpmppSde

Dieser Node ist dafür ausgelegt, einen Sampler für das DPM++ SDE-Modell (stochastische Differentialgleichung) zu generieren. Er passt sich sowohl an CPU- als auch an GPU-Ausführungsumgebungen an und optimiert die Implementierung des Samplers basierend auf der verfügbaren Hardware.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `eta` | Gibt die Schrittweite für den SDE-Solver an und beeinflusst die Granularität des Sampling-Prozesses. | FLOAT |
| `s_noise` | Bestimmt den Grad des Rauschens, das während des Sampling-Prozesses angewendet wird, und beeinflusst die Vielfalt der generierten Samples. | FLOAT |
| `r` | Steuert das Verhältnis der Rauschreduzierung im Sampling-Prozess und wirkt sich auf die Klarheit und Qualität der generierten Samples aus. | FLOAT |
| `noise_device` | Wählt die Ausführungsumgebung (CPU oder GPU) für den Sampler aus und optimiert die Leistung basierend auf der verfügbaren Hardware. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Der generierte Sampler, der mit den angegebenen Parametern konfiguriert wurde und für die Verwendung in Sampling-Vorgängen bereit ist. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/de.md)
