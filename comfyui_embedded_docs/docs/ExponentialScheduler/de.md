# ExponentialScheduler

Der `ExponentialScheduler`-Node ist darauf ausgelegt, eine Folge von Sigma-Werten gemäß einem exponentiellen Zeitplan für Diffusions-Sampling-Prozesse zu erzeugen. Er bietet einen anpassbaren Ansatz zur Steuerung der Rauschpegel, die bei jedem Schritt des Diffusionsprozesses angewendet werden, und ermöglicht eine Feinabstimmung des Sampling-Verhaltens.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `steps` | Gibt die Anzahl der Schritte im Diffusionsprozess an. Sie beeinflusst die Länge der erzeugten Sigma-Sequenz und somit die Granularität der Rauschanwendung. | INT |
| `sigma_max` | Definiert den maximalen Sigma-Wert und legt die Obergrenze der Rauschintensität im Diffusionsprozess fest. Er spielt eine entscheidende Rolle bei der Bestimmung des Bereichs der angewendeten Rauschpegel. | FLOAT |
| `sigma_min` | Legt den minimalen Sigma-Wert fest und etabliert die Untergrenze der Rauschintensität. Dieser Parameter hilft bei der Feinabstimmung des Startpunkts der Rauschanwendung. | FLOAT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Eine Folge von Sigma-Werten, die gemäß dem exponentiellen Zeitplan erzeugt wird. Diese Werte werden verwendet, um die Rauschpegel bei jedem Schritt des Diffusionsprozesses zu steuern. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/de.md)
