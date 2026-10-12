# Model-Patch laden

Der Node ModelPatchLoader lädt eine Model-Patch-Datei aus dem Ordner `model_patches` und bereitet sie für die Verwendung in einem Workflow vor. Er erkennt automatisch den in der Datei enthaltenen Patch-Typ, erstellt die passende Architektur, lädt die gespeicherten Gewichte und verpackt alles in einem Model-Patcher, sodass es auf andere Modelle angewendet werden kann. Er unterstützt viele spezialisierte Patch-Formate, darunter zusätzliche ControlNet-Zweige, Feature-Embedder-Modelle, Adapter, Animations-/LLLite-Guidance-Module und ähnliche Module.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `name` | Der Dateiname des Model-Patches, der aus dem Ordner `model_patches` geladen werden soll. Wählen Sie eine der verfügbaren Patch-Dateien aus der Liste. | COMBO | Ja | Dynamisch generierte Liste aller im Ordner `model_patches` gefundenen Model-Patch-Dateien |

Hinweis: Dieser Node ist als experimentell gekennzeichnet. Der Patch-Typ wird automatisch anhand des Dateiinhalts erkannt, sodass keine manuelle Typauswahl erforderlich ist. Der Node liest die Checkpoint-Metadaten und prüft die Gewichtsschlüssel, um zu entscheiden, welche Architektur aufgebaut werden soll (zum Beispiel Qwen Image block-wise ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP-Feature-Projektion, Lightricks-Duration-Head, Anima LLLite, MultiTalk oder SUPIR). Gewichte werden mit aktiviertem sicheren Laden geladen, und das Modell wird auf dem Offload-Gerät innerhalb eines `CoreModelPatcher` platziert, sodass es später auf ein anderes Modell angewendet werden kann.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL_PATCH` | Der geladene Model-Patch, verpackt in einem Model-Patcher, bereit, im Workflow auf ein Modell angewendet zu werden | MODEL_PATCH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/de.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`
