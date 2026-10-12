# UnetLoader

Der UNETLoader-Node ist für das Laden von U-Net-Modellen anhand ihres Namens konzipiert und erleichtert die Verwendung vortrainierter U-Net-Architekturen innerhalb des Systems.

Dieser Node erkennt Modelle, die sich im Ordner `ComfyUI/models/diffusion_models` befinden.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `unet_name` | Gibt den Namen des zu ladenden U-Net-Modells an. Dieser Name wird verwendet, um das Modell innerhalb einer vordefinierten Verzeichnisstruktur zu finden, wodurch das dynamische Laden verschiedener U-Net-Modelle ermöglicht wird. | COMBO[STRING] |
| `weight_dtype` | 🚧  fp8_e4m3fn fp9_e5m2 | ... |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Gibt das geladene U-Net-Modell zurück, sodass es für die weitere Verarbeitung oder Inferenz innerhalb des Systems genutzt werden kann. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnetLoader/de.md)
