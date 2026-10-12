# ModelSave

Der Node ModelSave speichert ein MODEL als `.safetensors`-Checkpoint-Datei auf dem Speicher Ihres Computers. Er schreibt die Datei in das Ausgabeverzeichnis von ComfyUI und verwendet dabei das von Ihnen angegebene Dateinamenpräfix. Wenn verfügbar, bettet er Workflow-Prompt-Informationen und Modell-Metadaten in die gespeicherte Datei ein.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das auf dem Datenträger gespeichert werden soll | MODEL | Ja | - |
| `filename_prefix` | Das Dateinamen- und Pfadpräfix für die gespeicherte Modelldatei (Standard: "diffusion_models/ComfyUI") | STRING | Ja | - |
| `prompt` | Workflow-Prompt-Informationen (automatisch bereitgestellt) | PROMPT | Nein | - |
| `extra_pnginfo` | Zusätzliche Workflow-Metadaten (automatisch bereitgestellt) | EXTRA_PNGINFO | Nein | - |

Hinweis: Der gespeicherte Dateiname wird aus dem Wert von `filename_prefix` gefolgt von einem fünfstelligen Zähler gebildet (zum Beispiel `diffusion_models/ComfyUI_00001_.safetensors`). Wenn bereits eine Datei mit demselben Präfix existiert, wird der Zähler erhöht, damit die neue Datei einen eindeutigen Namen erhält. Sofern verfügbar, werden der Workflow-Prompt, zusätzliche Metadaten und Informationen zur Modellarchitektur (zum Beispiel Stable Diffusion XL, SDXL Refiner, Stable Video Diffusion oder Stable Diffusion 3) in die gespeicherte Datei eingebettet. Wenn die Metadatenspeicherung über die Kommandozeileneinstellungen von ComfyUI deaktiviert ist, werden der Prompt und die zusätzlichen Metadaten nicht in die Datei geschrieben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| *None* | Dieser Node gibt keine Ausgabewerte zurück | - |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/de.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
