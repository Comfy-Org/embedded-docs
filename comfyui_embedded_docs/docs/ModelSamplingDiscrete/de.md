# ModelSamplingDiscrete

Dieser Node ist darauf ausgelegt, das Sampling-Verhalten eines Modells zu ändern, indem eine diskrete Sampling-Strategie angewendet wird. Er ermöglicht die Auswahl verschiedener Sampling-Methoden wie epsilon, v_prediction, lcm oder x0 und passt optional die Rauschreduzierungsstrategie des Modells basierend auf der Einstellung für das Zero-Shot-Rauschverhältnis (zsnr) an.

## Eingaben

| Parameter | Beschreibung | Datentyp | Python-Datentyp |
| --- | --- | --- | --- |
| `model` | Das Modell, auf das die diskrete Sampling-Strategie angewendet wird. Dieser Parameter ist entscheidend, da er das Basismodell definiert, das modifiziert wird. | MODEL | `torch.nn.Module` |
| `sampling` | Gibt die diskrete Sampling-Methode an, die auf das Modell angewendet werden soll. Die Wahl der Methode beeinflusst, wie das Modell Samples erzeugt, und bietet unterschiedliche Strategien für das Sampling. | COMBO[STRING] | `str` |
| `zsnr` | Ein boolesches Flag, das, wenn aktiviert, die Rauschreduzierungsstrategie des Modells basierend auf dem Zero-Shot-Rauschverhältnis (zsnr) anpasst. Dies kann die Qualität und die Eigenschaften der erzeugten Samples beeinflussen. | `BOOLEAN` | `bool` |

## Ausgaben

| Parameter | Beschreibung | Datentyp | Python-Datentyp |
| --- | --- | --- | --- |
| `model` | Das modifizierte Modell mit der angewendeten diskreten Sampling-Strategie. Dieses Modell ist nun in der Lage, Samples mit der angegebenen Methode und den Anpassungen zu erzeugen. | MODEL | `torch.nn.Module` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/de.md)
