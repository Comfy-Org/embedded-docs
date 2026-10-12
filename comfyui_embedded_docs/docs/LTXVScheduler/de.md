# LTXVScheduler

Der LTXVScheduler-Node erzeugt Sigma-Werte für einen benutzerdefinierten Sampling-Prozess. Er berechnet den Rauschplan aus der Anzahl der Tokens im bereitgestellten Latent oder verwendet standardmäßig 4096 Tokens, wenn kein Latent verbunden ist, und kann optional die Sigma-Werte strecken, sodass der Endwert dem angegebenen `terminal`-Wert entspricht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `steps` | Anzahl der Sampling-Schritte (Standard: 20) | INT | Ja | 1-10000 |
| `max_shift` | Maximaler Verschiebungswert, der in der Sigma-Berechnung verwendet wird (Standard: 2.05) | FLOAT | Ja | 0.0-100.0 (step: 0.01) |
| `base_shift` | Basis-Verschiebungswert, der in der Sigma-Berechnung verwendet wird (Standard: 0.95) | FLOAT | Ja | 0.0-100.0 (step: 0.01) |
| `stretch` | Streckt die Sigmas, sodass sie im Bereich [terminal, 1] liegen (Standard: True) | BOOLEAN | Ja | True/False |
| `terminal` | Der Endwert der Sigmas nach dem Strecken (Standard: 0.1). Wird nur verwendet, wenn `stretch` aktiviert ist. | FLOAT | Ja | 0.0-0.99 (step: 0.01) |
| `latent` | Optionale Latent-Eingabe, die zur Berechnung der Token-Anzahl für die Sigma-Anpassung verwendet wird. Wenn nicht angegeben, wird eine Standard-Token-Anzahl von 4096 verwendet. | LATENT | Nein | - |

**Hinweis:** Wenn `stretch` aktiviert ist, werden die Sigma-Werte ungleich null neu skaliert, sodass das letzte Sigma ungleich null dem `terminal`-Wert entspricht.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Sigma-Werte, die für den Sampling-Prozess erzeugt werden | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/de.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
