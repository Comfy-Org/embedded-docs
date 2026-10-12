# DeprecatedCheckpointLoader

Der CheckpointLoader-Node ist für fortgeschrittene Ladevorgänge konzipiert, insbesondere zum Laden von Modell-Checkpoints zusammen mit ihren Konfigurationen. Er ermöglicht das Abrufen von Modellkomponenten, die zum Initialisieren und Ausführen generativer Modelle erforderlich sind, einschließlich Konfigurationen und Checkpoints aus angegebenen Verzeichnissen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `config_name` | Gibt den Namen der zu verwendenden Konfigurationsdatei an. Dies ist entscheidend für die Bestimmung der Parameter und Einstellungen des Modells und wirkt sich auf Verhalten und Leistung des Modells aus. | COMBO[STRING] |
| `ckpt_name` | Gibt den Namen der zu ladenden Checkpoint-Datei an. Dies beeinflusst direkt den Zustand des initialisierten Modells und wirkt sich auf seine anfänglichen Gewichte und Bias-Werte aus. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Repräsentiert das primäre aus dem Checkpoint geladene Modell, bereit für weitere Operationen oder Inferenz. | MODEL |
| `clip` | Stellt die CLIP-Modellkomponente bereit, sofern verfügbar und angefordert, geladen aus dem Checkpoint. | CLIP |
| `vae` | Liefert die VAE-Modellkomponente, sofern verfügbar und angefordert, geladen aus dem Checkpoint. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/de.md)
