# LoraLoaderBypassModelOnly

Dieser Node wendet eine LoRA (Low-Rank Adaptation) auf ein Modell an, um dessen Verhalten zu ändern, betrifft jedoch nur die Modellkomponente selbst. Er lädt eine angegebene LoRA-Datei und justiert die Gewichte des Modells mit einer bestimmten Stärke, während andere Komponenten wie der CLIP-Textencoder unverändert bleiben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Basismodell, auf das die LoRA-Anpassungen angewendet werden. | MODEL | Ja | - |
| `lora_name` | Der Name der zu ladenden und anzuwendenden LoRA-Datei. Die Optionen werden aus den Dateien im Verzeichnis `loras` gefüllt. | STRING | Ja | (Liste der verfügbaren LoRA-Dateien) |
| `strength_model` | Die Stärke der Wirkung der LoRA auf die Gewichte des Modells. Ein positiver Wert wendet die LoRA an, ein negativer Wert wendet die Umkehrung an, und ein Wert von 0 hat keine Wirkung (Standard: 1.0). | FLOAT | Ja | -100.0 bis 100.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geänderte Modell mit den auf seine Gewichte angewendeten LoRA-Anpassungen. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/de.md)

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
