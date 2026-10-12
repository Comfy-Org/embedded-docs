# DiffControlnetLoader

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/controlnet` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie möglicherweise die **ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der DiffControlNetLoader-Node dient zum Laden differentieller ControlNets, spezialisierter Modelle, die das Verhalten eines anderen Modells anhand von ControlNet-Spezifikationen verändern können. Dieser Node ermöglicht die dynamische Anpassung des Modellverhaltens durch Anwendung differentieller ControlNets und erleichtert die Erstellung individuell angepasster Modellausgaben.

## Eingaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `model` | Das Basismodell, auf das das differentielle ControlNet angewendet wird, wodurch die Anpassung des Modellverhaltens ermöglicht wird. | `MODEL` |
| `control_net_name` | Identifiziert das spezifische differentielle ControlNet, das geladen und auf das Basismodell angewendet werden soll, um dessen Verhalten zu verändern. | `COMBO[STRING]` |

## Ausgaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `control_net` | Ein differentielles ControlNet, das geladen wurde und bereit ist, auf ein Basismodell angewendet zu werden, um dessen Verhalten zu verändern. | `CONTROL_NET` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlnetLoader/de.md)
