# SamplerER_SDE

Der Node SamplerER_SDE bietet spezialisierte Sampling-Methoden für Diffusionsmodelle und verschiedene Solver-Typen: ER-SDE, Reverse-time SDE und ODE. Er ermöglicht es Ihnen, das stochastische Verhalten und die Anzahl der Berechnungsstufen des Sampling-Prozesses zu steuern. Der Node passt Einstellungen automatisch basierend auf dem gewählten Solver-Typ an, damit der Sampler korrekt funktioniert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `solver_type` | Der Typ des Solvers, der für das Sampling verwendet werden soll. Bestimmt den mathematischen Ansatz für den Diffusionsprozess (Standard: "ER-SDE"). | COMBO | Ja | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | Die maximale Anzahl von Stufen für den Sampling-Prozess (Standard: 3). Steuert den Rechenaufwand und die Qualität. Dies ist ein erweiterter Parameter. | INT | Ja | 1-3 |
| `eta` | Stochastische Stärke von SDEs.<br>Wenn eta=0, reduzieren sie sich auf deterministische ODE.<br>Ein großes eta kann ungültige Ausgaben verursachen. Wenn dies auftritt, versuchen Sie, diesen Wert zu verringern. (Standard: 1.0). Dies ist ein erweiterter Parameter. | FLOAT | Ja | 0.0-10.0 (step: 0.01) |
| `s_noise` | Rauschskalierungsfaktor für den Sampling-Prozess (Standard: 1.0). Steuert die Menge an Rauschen, die während des Samplings angewendet wird. Dies ist ein erweiterter Parameter. | FLOAT | Ja | 0.0-100.0 (step: 0.01) |

**Parameterbeschränkungen:**

- Wenn `solver_type` auf "ODE" gesetzt ist oder `eta` 0 ist, wechselt der Node in den ODE-Modus und setzt `s_noise` auf 0.0, unabhängig vom eingegebenen Wert für `s_noise`.
- Der Parameter `eta` steuert die stochastische Stärke sowohl des Solver-Typs "ER-SDE" als auch "Reverse-time SDE". Er hat keine Auswirkung, wenn der Solver im ODE-Modus läuft.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Ein konfiguriertes Sampler-Objekt, das in der Sampling-Pipeline mit den angegebenen Solver-Einstellungen verwendet werden kann. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/de.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
