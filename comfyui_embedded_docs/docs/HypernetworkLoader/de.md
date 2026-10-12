# HypernetworkLoader

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/hypernetworks` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie möglicherweise **die ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner einlesen kann.

Der Node HypernetworkLoader ist darauf ausgelegt, die Fähigkeiten eines gegebenen Modells durch Anwendung eines Hypernetzwerks zu erweitern oder zu verändern. Er lädt ein angegebenes Hypernetzwerk und wendet es auf das Modell an, wodurch dessen Verhalten oder Leistung abhängig vom Parameter `strength` potenziell verändert wird. Dieser Prozess ermöglicht dynamische Anpassungen an der Architektur oder den Parametern des Modells und ermöglicht flexiblere und anpassungsfähigere KI-Systeme.

## Eingaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `model` | Das Basismodell, auf das das Hypernetzwerk angewendet wird, wodurch die Architektur bestimmt wird, die erweitert oder verändert werden soll. | `MODEL` |
| `hypernetwork_name` | Der Name des zu ladenden und auf das Modell anzuwendenden Hypernetzwerks, der das veränderte Verhalten oder die Leistung des Modells beeinflusst. | `COMBO[STRING]` |
| `strength` | Ein Skalar, der die Intensität der Wirkung des Hypernetzwerks auf das Modell anpasst und eine Feinabstimmung der Änderungen ermöglicht. | `FLOAT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell nach Anwendung des Hypernetzwerks, das die Auswirkung des Hypernetzwerks auf das ursprüngliche Modell zeigt. | `MODEL` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/de.md)
