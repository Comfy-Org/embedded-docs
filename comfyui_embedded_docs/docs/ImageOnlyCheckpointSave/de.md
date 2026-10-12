# ImageOnlyCheckpointSave

Dieser Node speichert eine Checkpoint-Datei, die ein Modell zusammen mit seinem CLIP-Vision-Encoder und VAE bündelt. Die Datei wird im safetensors-Format im Ausgabeverzeichnis geschrieben, wobei das angegebene Dateinamenpräfix verwendet wird, sodass die bildbezogenen Komponenten eines Modells als einzelner Checkpoint gespeichert werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das im Checkpoint zu speichernde Modell | MODEL | Ja | - |
| `clip_vision` | Der im Checkpoint zu speichernde CLIP-Vision-Encoder | CLIP_VISION | Ja | - |
| `vae` | Das im Checkpoint zu speichernde VAE (Variational Autoencoder) | VAE | Ja | - |
| `filename_prefix` | Das Präfix für den Ausgabedateinamen (Standard: "checkpoints/ComfyUI") | STRING | Ja | - |
| `prompt` | Versteckter Parameter, der die Prompt-Daten des Workflows empfängt | PROMPT | Nein | - |
| `extra_pnginfo` | Versteckter Parameter, der zusätzliche PNG-Metadaten empfängt | EXTRA_PNGINFO | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| - | Dieser Node gibt keine Ausgaben zurück | - |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/de.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
