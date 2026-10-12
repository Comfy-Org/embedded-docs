# SamplerDPMPP_2M_SDE

Der SamplerDPMPP_2M_SDE-Node erstellt einen DPM++ 2M SDE-Sampler für Diffusionsmodelle. Dieser Sampler verwendet Differentialgleichungslöser zweiter Ordnung mit stochastischen Differentialgleichungen, um Samples zu erzeugen. Er bietet verschiedene Solver-Typen und Optionen zur Rauschbehandlung, um den Sampling-Prozess zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `solver_type` | Der Typ des Differentialgleichungslösers, der für den Sampling-Prozess verwendet werden soll (Standard: "midpoint") | COMBO | Ja | `"midpoint"`<br>`"heun"` |
| `eta` | Steuert die Stochastizität des Sampling-Prozesses (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `s_noise` | Steuert die Menge des während des Samplings hinzugefügten Rauschens (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `noise_device` | Das Gerät, auf dem die Rauschberechnungen durchgeführt werden. Wenn auf "cpu" gesetzt, verwendet der Sampler eine CPU-basierte Rauscherzeugung; wenn auf "gpu" gesetzt, verwendet er eine GPU-basierte Rauscherzeugung für möglicherweise schnellere Leistung (Standard: "gpu") | COMBO | Ja | `"gpu"`<br>`"cpu"` |

Hinweis: `eta`, `s_noise` und `noise_device` sind als erweiterte Parameter markiert und erscheinen im erweiterten Abschnitt der Benutzeroberfläche des Nodes.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Ein konfiguriertes Sampler-Objekt, das für die Verwendung in der Sampling-Pipeline bereitsteht | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/de.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
