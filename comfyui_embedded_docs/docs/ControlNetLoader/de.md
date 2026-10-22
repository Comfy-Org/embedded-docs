# ControlnetLoader

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/controlnet` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie möglicherweise **die ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der ControlNetLoader-Node ist darauf ausgelegt, ein ControlNet-Modell von einem angegebenen Pfad zu laden. Er spielt eine entscheidende Rolle bei der Initialisierung von ControlNet-Modellen, die unerlässlich sind, um Steuermechanismen auf generierte Inhalte anzuwenden oder vorhandene Inhalte anhand von Steuersignalen zu verändern.

## Eingaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `control_net_name` | Gibt den Namen des zu ladenden ControlNet-Modells an; wird verwendet, um die Modelldatei innerhalb einer vordefinierten Verzeichnisstruktur zu finden. | `COMBO[STRING]` |

## Ausgaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `control_net` | Gibt das geladene ControlNet-Modell zurück, bereit zur Verwendung beim Steuern oder Ändern von Prozessen zur Inhaltsgenerierung. | `CONTROL_NET` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/de.md)
