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
| `OPTICAL_FLOW` | Das geladene Optical-Flow-Modell, auf den Evaluierungsmodus eingestellt, mit fp16-Präzision auf Geräten, die das unterstützen, sofern `--force-fp32` nicht gesetzt ist (sonst float32), und in einen ModelPatcher für die Verwendung mit anderen Nodes verpackt. | OPTICAL_FLOW |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/de.md)

---
**Source fingerprint (SHA-256):** `82e5d747679ede113ec4d72fd6eda4b8f20d098832612bebf26ef65de8b4b3dc`
