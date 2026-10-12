# GligenLoader

Dieser Node erkennt Modelle, die sich im Ordner `ComfyUI/models/gligen` befinden, und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie die **ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der Node `GLIGENLoader` ist für das Laden von GLIGEN-Modellen konzipiert, bei denen es sich um spezialisierte generative Modelle handelt. Er erleichtert das Abrufen und Initialisieren dieser Modelle von angegebenen Pfaden und macht sie für weitere generative Aufgaben bereit.

## Eingaben

| Feld | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `gligen_name` | Der Name des zu ladenden GLIGEN-Modells; gibt an, welche Modelldatei abgerufen und geladen werden soll, und ist entscheidend für die Initialisierung des GLIGEN-Modells. | `COMBO[STRING]` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `gligen` | Das geladene GLIGEN-Modell, bereit zur Verwendung in generativen Aufgaben; stellt das vollständig initialisierte Modell dar, das vom angegebenen Pfad geladen wurde. | `GLIGEN` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GligenLoader/de.md)
