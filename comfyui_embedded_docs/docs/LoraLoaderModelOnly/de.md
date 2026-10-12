# LoRA laden

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/loras` und liest zudem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie möglicherweise **die ComfyUI-Oberfläche aktualisieren**, damit die Modelldateien aus dem entsprechenden Ordner gelesen werden.

Dieser Node ist auf das Laden eines LoRA-Modells spezialisiert, ohne dass ein CLIP-Modell erforderlich ist. Er konzentriert sich darauf, ein gegebenes Modell anhand von LoRA-Parametern zu verbessern oder zu verändern. Er ermöglicht die dynamische Anpassung der Stärke des Modells über LoRA-Parameter und erlaubt so eine fein abgestimmte Steuerung des Modellverhaltens.

## Eingaben

| Feld | Beschreibung | Comfy dtype |
| --- | --- | --- |
| `model` | Das Basismodell für Änderungen, auf das LoRA-Anpassungen angewendet werden. | `MODEL` |
| `lora_name` | Der Name der zu ladenden LoRA-Datei, der die auf das Modell anzuwendenden Anpassungen angibt. | `COMBO[STRING]` |
| `strength_model` | Bestimmt die Intensität der LoRA-Anpassungen, wobei höhere Werte stärkere Änderungen anzeigen. | `FLOAT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeten LoRA-Anpassungen, das Änderungen im Modellverhalten oder in den Fähigkeiten widerspiegelt. | `MODEL` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/de.md)
