# LaplaceScheduler

Der Knoten LaplaceScheduler generiert eine Folge von Sigma-Werten gemäß einer Laplace-Verteilung zur Verwendung beim Diffusion-Sampling. Er erstellt einen Zeitplan für Rauschpegel, die schrittweise von einem Maximalwert auf einen Minimalwert abnehmen, wobei Parameter der Laplace-Verteilung verwendet werden, um den Verlauf zu steuern. Dieser Scheduler wird häufig in benutzerdefinierten Sampling-Workflows verwendet, um den Rausch-Zeitplan für Diffusionsmodelle festzulegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `steps` | Anzahl der Sampling-Schritte im Zeitplan (Standard: 20) | INT | Ja | 1 bis 10000 |
| `sigma_max` | Maximaler Sigma-Wert am Beginn des Zeitplans (Standard: 14.614642) | FLOAT | Ja | 0.0 bis 5000.0 |
| `sigma_min` | Minimaler Sigma-Wert am Ende des Zeitplans (Standard: 0.0291675) | FLOAT | Ja | 0.0 bis 5000.0 |
| `mu` | Mittelwertparameter für die Laplace-Verteilung (Standard: 0.0) | FLOAT | Ja | -10.0 bis 10.0 |
| `beta` | Skalenparameter für die Laplace-Verteilung (Standard: 0.5) | FLOAT | Ja | 0.0 bis 10.0 |

Hinweis: `sigma_max`, `sigma_min`, `mu` und `beta` sind erweiterte Parameter.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `SIGMAS` | Eine Folge von Sigma-Werten, die einem Laplace-Verteilungs-Zeitplan folgt | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/de.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
