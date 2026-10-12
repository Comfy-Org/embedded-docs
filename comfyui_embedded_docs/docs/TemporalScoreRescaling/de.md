# TemporalScoreRescaling

Dieser Knoten wendet Temporal Score Rescaling (TSR) auf ein Diffusionsmodell an. Er patcht das Modell so, dass während des Samplings der vorhergesagte Score oder das Rauschen neu skaliert wird, um die Vielfalt der generierten Ergebnisse zu steuern. Dies ist als Post-CFG-Funktion (Classifier-Free Guidance) implementiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, das mit der TSR-Funktion gepatcht werden soll. | MODEL | Ja | - |
| `tsr_k` | Steuert die Stärke der Neuskalierung. Ein niedrigeres k erzeugt detailliertere Ergebnisse; ein höheres k erzeugt glattere Ergebnisse in der Bilderzeugung. Die Einstellung k = 1 deaktiviert die Neuskalierung. (Standard: 0.95) | FLOAT | Ja | 0.01 - 100.0 |
| `tsr_sigma` | Steuert, wie früh die Neuskalierung wirksam wird. Größere Werte wirken früher. (Standard: 1.0) | FLOAT | Ja | 0.01 - 100.0 |

Hinweis: Die Neuskalierung wird übersprungen, wenn `tsr_k` auf 1 gesetzt ist, wenn der Sigma-Wert 0 ist oder wenn das Signal-Rausch-Verhältnis 0 ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `patched_model` | Das Eingabemodell, jetzt gepatcht mit der Temporal Score Rescaling-Funktion, die auf seinen Sampling-Prozess angewendet wird. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/de.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
