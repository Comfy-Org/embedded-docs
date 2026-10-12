# StyleModelLoader

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/style_models` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie die **ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der Node StyleModelLoader dient zum Laden eines Style-Modells von einem angegebenen Pfad. Er konzentriert sich darauf, Style-Modelle abzurufen und zu initialisieren, mit denen bestimmte künstlerische Stile auf Bilder angewendet werden können, wodurch die Anpassung visueller Ausgaben basierend auf dem geladenen Style-Modell ermöglicht wird.

## Eingaben

| Parametername | Beschreibung | Comfy-Datentyp | Python-Datentyp |
| --- | --- | --- | --- |
| `style_model_name` | Gibt den Namen des zu ladenden Style-Modells an. Dieser Name wird verwendet, um die Modelldatei innerhalb einer vordefinierten Verzeichnisstruktur zu finden, wodurch verschiedene Style-Modelle dynamisch basierend auf Benutzereingaben oder Anwendungsanforderungen geladen werden können. | COMBO[STRING] | `str` |

## Ausgaben

| Parametername | Beschreibung | Comfy-Datentyp | Python-Datentyp |
| --- | --- | --- | --- |
| `style_model` | Gibt das geladene Style-Modell zurück, bereit zur Verwendung beim Anwenden von Stilen auf Bilder. Dies ermöglicht die dynamische Anpassung visueller Ausgaben durch Anwenden verschiedener künstlerischer Stile. | `STYLE_MODEL` | `StyleModel` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/de.md)
