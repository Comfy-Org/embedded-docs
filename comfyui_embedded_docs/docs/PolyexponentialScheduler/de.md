# PolyexponentialScheduler

Der Node PolyexponentialScheduler ist dafür ausgelegt, eine Folge von Rauschpegeln (Sigmas) basierend auf einem polyexponentiellen Rauschplan zu erzeugen. Dieser Plan ist eine Polynomfunktion im Logarithmus von Sigma und ermöglicht eine flexible und anpassbare Progression der Rauschpegel während des Diffusionsprozesses.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `steps` | Gibt die Anzahl der Schritte im Diffusionsprozess an und beeinflusst damit die Granularität der erzeugten Rauschpegel. | INT |
| `sigma_max` | Der maximale Rauschpegel, der die Obergrenze des Rauschplans festlegt. | FLOAT |
| `sigma_min` | Der minimale Rauschpegel, der die Untergrenze des Rauschplans festlegt. | FLOAT |
| `rho` | Ein Parameter, der die Form des polyexponentiellen Rauschplans steuert und beeinflusst, wie sich die Rauschpegel zwischen Minimal- und Maximalwert entwickeln. | FLOAT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `sigmas` | Die Ausgabe ist eine Folge von Rauschpegeln (Sigmas), die auf den angegebenen polyexponentiellen Rauschplan zugeschnitten ist. | SIGMAS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/de.md)
