# Upscale-Modell laden

Dieser Node erkennt Modelle, die sich im Ordner `ComfyUI/models/upscale_models` befinden, und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie die **ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der UpscaleModelLoader-Node ist für das Laden von Upscale-Modellen aus einem angegebenen Verzeichnis vorgesehen. Er ermöglicht das Abrufen und Vorbereiten von Upscale-Modellen für Bild-Upscaling-Aufgaben und stellt sicher, dass die Modelle korrekt geladen und für die Auswertung konfiguriert werden.

## Eingaben

| Feld | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `model_name` | Gibt den Namen des zu ladenden Upscale-Modells an, identifiziert die richtige Modelldatei im Upscale-Modellverzeichnis und ruft sie ab. | `COMBO[STRING]` |

## Ausgaben

| Feld | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `upscale_model` | Gibt das geladene und vorbereitete Upscale-Modell zurück, bereit zur Verwendung für Bild-Upscaling-Aufgaben. | `UPSCALE_MODEL` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/de.md)
