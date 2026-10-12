# ConditioningSetMask

Dieser Node dient dazu, das Conditioning eines generativen Modells zu verändern, indem eine Maske mit einer bestimmten Stärke auf bestimmte Bereiche angewendet wird. Er ermöglicht gezielte Anpassungen innerhalb des Conditionings und erlaubt eine präzisere Steuerung des Generierungsprozesses.

## Eingaben

### Erforderlich

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die zu verändernden Conditioning-Daten. Sie dienen als Grundlage für die Anwendung der Maske und der Stärkeanpassungen. | CONDITIONING |
| `mask` | Ein Masken-Tensor, der die Bereiche innerhalb des Conditionings angibt, die verändert werden sollen. | `MASK` |
| `strength` | Die Stärke der Wirkung der Maske auf das Conditioning; ermöglicht eine Feinabstimmung der angewendeten Änderungen. | `FLOAT` |
| `set_cond_area` | Legt fest, ob die Wirkung der Maske auf den Standardbereich angewendet oder durch die Maske selbst begrenzt wird, was Flexibilität beim Anvisieren bestimmter Regionen bietet. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die veränderten Conditioning-Daten, auf die die Masken- und Stärkeanpassungen angewendet wurden. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/de.md)
