# EpsilonScaling

Implementiert die Epsilon-Scaling-Methode aus dem Forschungspapier „Elucidating the Exposure Bias in Diffusion Models“. Diese Methode verbessert die Sample-Qualität, indem sie das vorhergesagte Rauschen während des Sampling-Prozesses skaliert. Sie verwendet einen gleichmäßigen Zeitplan, um Exposure Bias in Diffusionsmodellen zu mildern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das Epsilon-Scaling angewendet werden soll | MODEL | Ja | - |
| `scaling_factor` | Der Faktor, der zum Skalieren des vorhergesagten Rauschens verwendet wird (Standard: 1.005) | FLOAT | Nein | 0.5 - 1.5 |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit angewendetem Epsilon-Scaling | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/de.md)
