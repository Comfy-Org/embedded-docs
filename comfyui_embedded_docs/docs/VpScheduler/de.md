# VpScheduler

Der Node VPScheduler dient dazu, eine Sequenz von Rauschpegeln (Sigmas) basierend auf der Variance-Preserving-(VP)-Scheduling-Methode zu erzeugen. Diese Sequenz ist entscheidend für die Steuerung des Denoising-Prozesses in Diffusionsmodellen und ermöglicht die kontrollierte Generierung von Bildern oder anderen Datentypen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `steps` | Gibt die Anzahl der Schritte im Diffusionsprozess an und beeinflusst die Granularität der erzeugten Rauschpegel. | INT |
| `beta_d` | Bestimmt die Gesamtverteilung des Rauschpegels und beeinflusst die Varianz der erzeugten Rauschpegel. | FLOAT |
| `beta_min` | Legt die Untergrenze für den Rauschpegel fest, sodass das Rauschen einen bestimmten Schwellenwert nicht unterschreitet. | FLOAT |
| `eps_s` | Passt den Start-Epsilon-Wert an und optimiert den anfänglichen Rauschpegel im Diffusionsprozess fein. | FLOAT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Eine Sequenz von Rauschpegeln (Sigmas), die basierend auf der VP-Scheduling-Methode erzeugt wird und dazu dient, den Denoising-Prozess in Diffusionsmodellen zu steuern. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VpScheduler/de.md)
