# SamplerDPMAdaptative

Der Node SamplerDPMAdaptative implementiert einen adaptiven DPM-Sampler (Diffusion Probabilistic Model), der die Schrittweiten während des Sampling-Prozesses automatisch anpasst. Er verwendet toleranzbasierte Fehlerkontrolle, um optimale Schrittweiten zu bestimmen, und balanciert so Recheneffizienz und Sampling-Genauigkeit aus. Dieser adaptive Ansatz trägt dazu bei, die Qualität zu erhalten und möglicherweise die Anzahl der benötigten Schritte zu reduzieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `order` | Die Ordnung der Sampler-Methode (Standard: 3) | INT | Ja | 2-3 |
| `rtol` | Relative Toleranz für die Fehlerkontrolle (Standard: 0.05) | FLOAT | Ja | 0.0-100.0 |
| `atol` | Absolute Toleranz für die Fehlerkontrolle (Standard: 0.0078) | FLOAT | Ja | 0.0-100.0 |
| `h_init` | Anfängliche Schrittweite (Standard: 0.05) | FLOAT | Ja | 0.0-100.0 |
| `pcoeff` | Proportionalkoeffizient für die Schrittweitensteuerung (Standard: 0.0) | FLOAT | Ja | 0.0-100.0 |
| `icoeff` | Integralkoeffizient für die Schrittweitensteuerung (Standard: 1.0) | FLOAT | Ja | 0.0-100.0 |
| `dcoeff` | Ableitungskoeffizient für die Schrittweitensteuerung (Standard: 0.0) | FLOAT | Ja | 0.0-100.0 |
| `accept_safety` | Sicherheitsfaktor für die Schrittakzeptanz (Standard: 0.81) | FLOAT | Ja | 0.0-100.0 |
| `eta` | Stochastizitätsparameter (Standard: 0.0) | FLOAT | Ja | 0.0-100.0 |
| `s_noise` | Rauschskalierungsfaktor (Standard: 1.0) | FLOAT | Ja | 0.0-100.0 |

Alle Eingaben sind erweiterte Parameter, mit denen das adaptive Sampling-Verhalten feinabgestimmt werden kann. Alle numerischen Eingaben erlauben Dezimalwerte und akzeptieren einen Minimalwert von 0.0 und einen Maximalwert von 100.0, mit Ausnahme von `order`, das auf die ganzzahligen Werte 2 oder 3 beschränkt ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt eine konfigurierte Instanz eines adaptiven DPM-Samplers zurück | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMAdaptative/de.md)

---
**Source fingerprint (SHA-256):** `07b2e5b9f21ec101eabccc6be245d043e64a996a14db10434b03eaae0a91b1d8`
