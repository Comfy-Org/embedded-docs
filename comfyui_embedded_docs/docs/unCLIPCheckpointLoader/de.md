# UnclipCheckpointLoader

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/checkpoints` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie möglicherweise **die ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Der unCLIPCheckpointLoader-Node ist für das Laden von Checkpoints konzipiert, die speziell auf unCLIP-Modelle zugeschnitten sind. Er ermöglicht das Abrufen und Initialisieren von Modellen, CLIP-Vision-Modulen und VAEs aus einem angegebenen Checkpoint und vereinfacht damit den Einrichtungsprozess für weitere Vorgänge oder Analysen.

## Eingaben

| Feld | Beschreibung | Comfy-Datentyp |
| --- | --- | --- |
| `ckpt_name` | Gibt den Namen des zu ladenden Checkpoints an, identifiziert und ruft die korrekte Checkpoint-Datei aus einem vordefinierten Verzeichnis ab und bestimmt die Initialisierung von Modellen und Konfigurationen. | `COMBO[STRING]` |

## Ausgaben

| Feld | Beschreibung | Comfy-Datentyp | Python-Datentyp |
| --- | --- | --- | --- |
| `model` | Repräsentiert das primäre Modell, das aus dem Checkpoint geladen wurde. | `MODEL` | `torch.nn.Module` |
| `clip` | Repräsentiert das aus dem Checkpoint geladene CLIP-Modul, sofern verfügbar. | `CLIP` | `torch.nn.Module` |
| `vae` | Repräsentiert das aus dem Checkpoint geladene VAE-Modul, sofern verfügbar. | `VAE` | `torch.nn.Module` |
| `clip_vision` | Repräsentiert das aus dem Checkpoint geladene CLIP-Vision-Modul, sofern verfügbar. | `CLIP_VISION` | `torch.nn.Module` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/de.md)
