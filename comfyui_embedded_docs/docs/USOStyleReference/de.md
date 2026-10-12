# USO-Stilreferenz anwenden

Der Node `USOStyleReference` wendet eine Stilreferenz auf ein Modell an, indem CLIP-Vision-Merkmale mit einem Modell-Patch kombiniert werden, und gibt eine gepatchte Kopie des Eingabemodells zurück. Die visuellen Stilinformationen werden mit der Textkonditionierung des Modells kombiniert, sodass sie die Generierung beeinflussen können. Dieser Node ist für Flux-Modelle vorgesehen und als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Basismodell, auf das der Stilreferenz-Patch angewendet wird. | MODEL | Ja | - |
| `model_patch` | Der Modell-Patch, der das Projektionsmodell enthält, mit dem die Merkmale des Referenzbilds kodiert werden. | MODEL_PATCH | Ja | - |
| `clip_vision_output` | Die kodierten visuellen Merkmale, die durch CLIP-Vision-Verarbeitung aus dem Referenzbild extrahiert wurden. | CLIP_VISION_OUTPUT | Ja | - |

Hinweis: Der `clip_vision_output` muss von einem CLIP-Vision-Modell stammen, das die vollständigen verborgenen Zustände und den vorletzten verborgenen Zustand bereitstellt. Der Node kombiniert die verborgenen Zustände 20 von hinten, 11 von hinten sowie den vorletzten verborgenen Zustand zum Stil-Embedding. Der `model_patch` muss über sein Attribut `model` ein Projektionsmodell bereitstellen, das diese Bildmerkmale in das Stil-Embedding umwandelt. Während des Samplings wird das Stil-Embedding der Textkonditionierung vorangestellt, damit es die Generierung beeinflussen kann, und passende Text-IDs mit Nullposition werden den Text-IDs vorangestellt, damit die ID-Sequenz an der erweiterten Konditionierung ausgerichtet bleibt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendetem Stilreferenz-Patch. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/de.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
