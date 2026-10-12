# BetaSamplingScheduler

Der Node BetaSamplingScheduler erzeugt eine Abfolge von Rauschpegeln (Sigmas) für den Sampling-Prozess mithilfe eines Beta-Scheduling-Algorithmus. Er nimmt ein Modell und Konfigurationsparameter entgegen, um einen angepassten Rauschplan zu erstellen, der den Denoising-Prozess während der Bildgenerierung steuert. Dieser Scheduler ermöglicht die Feinabstimmung des Rauschreduzierungsverlaufs über Alpha- und Beta-Parameter.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zum Sampling verwendete Modell, das das Modell-Sampling-Objekt bereitstellt | MODEL | Ja | - |
| `steps` | Die Anzahl der Sampling-Schritte, für die Sigmas erzeugt werden (Standard: 20) | INT | Ja | 1 bis 10000 |
| `alpha` | Alpha-Parameter für den Beta-Scheduler, der die Scheduling-Kurve steuert (Standard: 0.6, erweiterter Parameter) | FLOAT | Ja | 0.0 bis 50.0 (Schritt 0.01) |
| `beta` | Beta-Parameter für den Beta-Scheduler, der die Scheduling-Kurve steuert (Standard: 0.6, erweiterter Parameter) | FLOAT | Ja | 0.0 bis 50.0 (Schritt 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `SIGMAS` | Eine Abfolge von Rauschpegeln (Sigmas), die für den Sampling-Prozess verwendet werden | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/de.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
