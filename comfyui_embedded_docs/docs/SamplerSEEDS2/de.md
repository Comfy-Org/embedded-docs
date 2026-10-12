# SamplerSEEDS2

Dieser Node bietet einen konfigurierbaren Sampler für die Bilderzeugung. Er basiert auf einem Solver für stochastische Differentialgleichungen (SDE) und kann sich je nach Einstellungen wie mehrere spezifische Sampler verhalten, darunter `seeds_2`, `exp_heun_2_x0` und `exp_heun_2_x0_sde`.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `solver_type` | Wählt den zugrunde liegenden Solver-Algorithmus für den Sampler aus. | COMBO | Ja | "phi_1"<br>"phi_2" |
| `eta` | Stochastische Stärke (Standard: 1.0). | FLOAT | Nein | 0.0 - 100.0 |
| `s_noise` | SDE-Rauschmultiplikator (Standard: 1.0). | FLOAT | Nein | 0.0 - 100.0 |
| `r` | Relative Schrittweite für die Zwischenstufe (c2-Node) (Standard: 0.5). | FLOAT | Nein | 0.01 - 1.0 |

**Hinweis:** Die Node-Beschreibung definiert die folgenden Sampler-Voreinstellungen:
- `seeds_2`: Standardeinstellungen
- `exp_heun_2_x0`: `solver_type` = "phi_2", `r` = 1.0, `eta` = 0.0
- `exp_heun_2_x0_sde`: `solver_type` = "phi_2", `r` = 1.0, `eta` = 1.0, `s_noise` = 1.0

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Ein konfiguriertes Sampler-Objekt, das an andere Sampling-Nodes übergeben werden kann. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/de.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
