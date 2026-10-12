# Style Model anwenden

Dieser Node wendet ein Stilmodell auf eine gegebene Konditionierung an und verbessert oder verändert deren Stil basierend auf der Ausgabe eines CLIP-Vision-Modells. Er integriert die Konditionierung des Stilmodells in die vorhandene Konditionierung, wodurch eine nahtlose Mischung von Stilen im Generierungsprozess ermöglicht wird.

## Eingaben

### Erforderlich

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning` | Die ursprünglichen Konditionierungsdaten, auf die die Konditionierung des Stilmodells angewendet wird. Sie sind entscheidend für die Definition des Basiskontexts oder -stils, der verbessert oder verändert wird. | `CONDITIONING` |
| `style_model` | Das Stilmodell, das verwendet wird, um basierend auf der Ausgabe des CLIP-Vision-Modells eine neue Konditionierung zu erzeugen. Es spielt eine Schlüsselrolle bei der Definition des neuen Stils, der angewendet werden soll. | `STYLE_MODEL` |
| `clip_vision_output` | Die Ausgabe eines CLIP-Vision-Modells, die vom Stilmodell verwendet wird, um eine neue Konditionierung zu erzeugen. Sie liefert den visuellen Kontext, der für die Stilanwendung erforderlich ist. | `CLIP_VISION_OUTPUT` |

## Ausgaben

| Parameter | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `conditioning` | Die verbesserte oder veränderte Konditionierung, die die Ausgabe des Stilmodells einbezieht. Sie stellt die finale, stilisierte Konditionierung dar, die für die weitere Verarbeitung oder Generierung bereit ist. | `CONDITIONING` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/de.md)
