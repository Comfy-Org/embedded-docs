# Checkpoint laden

Lädt eine Diffusion-Modell-Checkpoint-Datei und teilt sie in drei Kernkomponenten auf: das Hauptmodell, das zum Denoising von Latents verwendet wird, den CLIP-Textencoder und den VAE-Bildencoder/-decoder. Der Node erkennt automatisch alle Modelldateien im Ordner `ComfyUI/models/checkpoints` sowie alle zusätzlichen Pfade, die in Ihrer `extra_model_paths.yaml`-Datei konfiguriert sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Der Name des zu ladenden Checkpoints (Modells). Wählen Sie den Dateinamen des Checkpoint-Modells aus, der das KI-Modell bestimmt, das für die nachfolgende Bildgenerierung verwendet wird. | COMBO | Ja | Alle Modelldateien, die im Checkpoints-Ordner gefunden werden |

**Hinweis:** Wenn neue Modelldateien hinzugefügt werden, während ComfyUI läuft, müssen Sie den Browser aktualisieren (Ctrl+R), um die neuen Dateien in der Dropdown-Liste zu sehen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das Modell, das zum Denoising von Latents verwendet wird. Dies ist das zentrale Diffusionsmodell, das für die Bildgenerierung verwendet wird. | MODEL |
| `CLIP` | Das CLIP-Modell, das zum Kodieren von Text-Prompts verwendet wird und Textbeschreibungen in Informationen umwandelt, die die KI verstehen kann. | CLIP |
| `VAE` | Das VAE-Modell, das zum Kodieren und Dekodieren von Bildern in den und aus dem Latentraum verwendet wird. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/de.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
