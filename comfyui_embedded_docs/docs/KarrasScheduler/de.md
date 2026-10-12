# KarrasScheduler

Der KarrasScheduler-Node ist dafür ausgelegt, eine Sequenz von Rauschpegeln (Sigmas) basierend auf dem Rauschplan von Karras et al. (2022) zu erzeugen. Dieser Scheduler ist nützlich, um den Diffusionsprozess in generativen Modellen zu steuern, und ermöglicht fein abgestimmte Anpassungen der Rauschpegel, die bei jedem Schritt des Generierungsprozesses angewendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `steps` | Gibt die Anzahl der Schritte im Rauschplan an und beeinflusst die Granularität der erzeugten Sigma-Sequenz. | INT |
| `sigma_max` | Der maximale Sigma-Wert im Rauschplan; legt die Obergrenze der Rauschpegel fest. | FLOAT |
| `sigma_min` | Der minimale Sigma-Wert im Rauschplan; legt die Untergrenze der Rauschpegel fest. | FLOAT |
| `rho` | Ein Parameter, der die Form der Rauschplan-Kurve steuert und beeinflusst, wie die Rauschpegel von sigma_min zu sigma_max fortschreiten. | FLOAT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Die erzeugte Sequenz von Rauschpegeln (Sigmas), die dem Rauschplan von Karras et al. (2022) folgt. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/de.md)
