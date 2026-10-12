# Optical-Flow-Modell laden

Lädt ein Optical-Flow-Modell aus dem Ordner `models/optical_flow/`. Derzeit wird nur das RAFT-large-Format von torchvision unterstützt, also das Modell, das vom Node VOIDWarpedNoise verwendet wird. ComfyUI lädt Optical-Flow-Gewichte nicht automatisch herunter; Sie müssen die Checkpoint-Datei manuell im Verzeichnis `models/optical_flow/` ablegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model_name` | Zu ladendes Optical-Flow-Modell. Dateien müssen im Ordner `optical_flow` abgelegt werden. Derzeit wird nur `raft_large.pth` von torchvision unterstützt. | COMBO | Ja | Liste der Dateien im Ordner `models/optical_flow/` |

Hinweis: Der ausgewählte Checkpoint muss ein torchvision-RAFT-large-State-Dict sein, das Schlüssel mit den Präfixen `feature_encoder.`, `context_encoder.` und `update_block.` enthält. Wenn die Datei nicht diesem Format entspricht, löst der Node einen ValueError aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `OPTICAL_FLOW` | Das geladene Optical-Flow-Modell, auf den Evaluierungsmodus und float32-Präzision eingestellt und in einen ModelPatcher für die Verwendung mit anderen Nodes verpackt. | OPTICAL_FLOW |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/de.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
