# LoraLoader

Dieser Node erkennt automatisch Modelle im LoRA-Ordner (einschließlich Unterordner), wobei der entsprechende Modellpfad `ComfyUI\models\loras` lautet. Weitere Informationen finden Sie unter Installieren von LoRA-Modellen.

Der Node „LoRA Loader“ wird hauptsächlich zum Laden von LoRA-Modellen verwendet. Sie können sich LoRA-Modelle als Filter vorstellen, mit denen Sie Ihren Bildern bestimmte Stile, Inhalte und Details verleihen können:

- Bestimmte künstlerische Stile anwenden (z. B. Tuschemalerei)
- Merkmale bestimmter Charaktere hinzufügen (z. B. Spielcharaktere)
- Spezifische Details zum Bild hinzufügen

All dies lässt sich mit LoRA erreichen.

Wenn Sie mehrere LoRA-Modelle laden möchten, können Sie mehrere Nodes direkt hintereinander verketten, wie unten dargestellt:

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Wird normalerweise verwendet, um eine Verbindung zum Basismodell herzustellen | MODEL |
| `clip` | Wird normalerweise verwendet, um eine Verbindung zum CLIP-Modell herzustellen | CLIP |
| `lora_name` | Wählen Sie den Namen des zu verwendenden LoRA-Modells aus | COMBO[STRING] |
| `strength_model` | Wertebereich von -100.0 bis 100.0, für die tägliche Bilderzeugung typischerweise zwischen 0~1 verwendet. Höhere Werte führen zu deutlicheren Anpassungseffekten des Modells | FLOAT |
| `strength_clip` | Wertebereich von -100.0 bis 100.0, für die tägliche Bilderzeugung typischerweise zwischen 0~1 verwendet. Höhere Werte führen zu deutlicheren Anpassungseffekten des Modells | FLOAT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit angewendeten LoRA-Anpassungen | MODEL |
| `clip` | Die CLIP-Instanz mit angewendeten LoRA-Anpassungen | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/de.md)
