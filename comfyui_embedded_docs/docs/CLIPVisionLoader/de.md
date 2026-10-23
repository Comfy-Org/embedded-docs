# ClipVisionLoader

Dieser Node erkennt automatisch Modelle im Ordner `ComfyUI/models/clip_vision` sowie alle zusätzlichen Modellpfade, die in der Datei `extra_model_paths.yaml` konfiguriert sind. Wenn Sie Modelle hinzufügen, nachdem ComfyUI gestartet wurde, **aktualisieren Sie bitte die ComfyUI-Oberfläche**, damit die neuesten Modelldateien aufgelistet werden.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip_name` | Listet alle unterstützten Modelldateien im Ordner `ComfyUI/models/clip_vision` auf. | COMBO[STRING] |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip_vision` | Geladenes CLIP-Vision-Modell, bereit zum Kodieren von Bildern oder für andere Vision-bezogene Aufgaben. | CLIP_VISION |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/de.md)
