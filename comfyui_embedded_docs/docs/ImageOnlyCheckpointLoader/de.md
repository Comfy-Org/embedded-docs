# Nur Checkpoint-Bild laden (img2vid-Modell)

Dieser Node erkennt Modelle im Ordner `ComfyUI/models/checkpoints` und liest außerdem Modelle aus zusätzlichen Pfaden, die in der Datei extra_model_paths.yaml konfiguriert sind. Manchmal müssen Sie die **ComfyUI-Oberfläche aktualisieren**, damit sie die Modelldateien aus dem entsprechenden Ordner lesen kann.

Dieser Node ist auf das Laden von Checkpoints speziell für bildbasierte Modelle in Workflows zur Videogenerierung spezialisiert. Er ruft die erforderlichen Komponenten aus einem gegebenen Checkpoint effizient ab und konfiguriert sie, wobei der Schwerpunkt auf bildbezogenen Aspekten des Modells liegt.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `ckpt_name` | Gibt den Namen des zu ladenden Checkpoints an; entscheidend, um die korrekte Checkpoint-Datei aus einer vordefinierten Liste zu identifizieren und abzurufen. | COMBO[STRING] |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Gibt das Hauptmodell zurück, das aus dem Checkpoint geladen wurde und für die Bildverarbeitung in Kontexten der Videogenerierung konfiguriert ist. | MODEL |
| `clip_vision` | Stellt die CLIP-Vision-Komponente aus dem Checkpoint bereit, zugeschnitten auf Bildverständnis und Merkmalsextraktion. | `CLIP_VISION` |
| `vae` | Liefert die Variational Autoencoder (VAE)-Komponente, die für Bildmanipulations- und Generierungsaufgaben unerlässlich ist. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/de.md)
