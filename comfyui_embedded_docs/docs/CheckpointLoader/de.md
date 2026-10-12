# CheckpointLoader

Der Node `CheckpointLoader` lädt einen vortrainierten Modell-Checkpoint zusammen mit seiner Konfigurationsdatei. Er nimmt eine Konfigurationsdatei und eine Checkpoint-Datei als Eingaben entgegen und gibt die geladenen Modellkomponenten zurück – das Hauptmodell, das CLIP-Modell und das VAE-Modell – zur Verwendung im Workflow. Dieser Node ist veraltet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `config_name` | Die Konfigurationsdatei, die die Modellarchitektur und die Einstellungen definiert | COMBO | Ja | Verfügbare Konfigurationsdateien |
| `ckpt_name` | Die Checkpoint-Datei, die die trainierten Modellgewichte und Parameter enthält | COMBO | Ja | Verfügbare Checkpoint-Dateien |

**Hinweis:** Dieser Node erfordert, dass sowohl eine Konfigurationsdatei als auch eine Checkpoint-Datei ausgewählt wird. Die Konfigurationsdatei muss zur Architektur der zu ladenden Checkpoint-Datei passen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Die geladene Hauptmodellkomponente, bereit für die Inferenz | MODEL |
| `CLIP` | Die geladene CLIP-Modellkomponente zur Textkodierung | CLIP |
| `VAE` | Die geladene VAE-Modellkomponente zur Bildkodierung und -dekodierung | VAE |

**Wichtiger Hinweis:** Dieser Node wurde als veraltet markiert und könnte in zukünftigen Versionen entfernt werden. Erwägen Sie, für neue Workflows alternative Lade-Nodes zu verwenden.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/de.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
