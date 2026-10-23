# UnclipConditioning

Dieser Node ist darauf ausgelegt, CLIP-Vision-Ausgaben in den Konditionierungsprozess zu integrieren und den Einfluss dieser Ausgaben anhand angegebener Stärke- und Rausch-Augmentierungsparameter anzupassen. Er reichert die Konditionierung mit visuellem Kontext an und verbessert so den Generierungsprozess.

## Eingaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning` | Die Basiskonditionierungsdaten, zu denen die CLIP-Vision-Ausgaben hinzugefügt werden und die als Grundlage für weitere Änderungen dienen. | `CONDITIONING` |
| `clip_vision_output` | Die Ausgabe eines CLIP-Vision-Modells, die visuellen Kontext bereitstellt, der in die Konditionierung integriert wird. | `CLIP_VISION_OUTPUT` |
| `strength` | Bestimmt die Intensität des Einflusses der CLIP-Vision-Ausgabe auf die Konditionierung. | `FLOAT` |
| `noise_augmentation` | Gibt den Grad der Rausch-Augmentierung an, der auf die CLIP-Vision-Ausgabe angewendet wird, bevor sie in die Konditionierung integriert wird. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning` | Die angereicherten Konditionierungsdaten, die nun integrierte CLIP-Vision-Ausgaben mit angewendeter Stärke und Rausch-Augmentierung enthalten. | `CONDITIONING` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/de.md)
