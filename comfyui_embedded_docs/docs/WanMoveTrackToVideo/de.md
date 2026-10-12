# WanMoveTrackToVideo

Der Node WanMoveTrackToVideo bereitet Konditionierungs- und Latentraum-Daten für die Videogenerierung vor und bezieht dabei optionale Bewegungsverfolgungsinformationen ein. Er kodiert eine Startbildsequenz in eine latente Repräsentation und kann Positionsdaten aus Objekt-Tracks einmischen, um die Bewegung im generierten Video zu steuern. Der Node gibt modifizierte positive und negative Konditionierung sowie einen leeren Latent-Tensor aus, der für ein Videomodell bereit ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die zu modifizierende positive Konditionierungseingabe. | CONDITIONING | Ja | - |
| `negative` | Die zu modifizierende negative Konditionierungseingabe. | CONDITIONING | Ja | - |
| `vae` | Das VAE-Modell, das verwendet wird, um das Startbild in den Latentraum zu kodieren. | VAE | Ja | - |
| `tracks` | Optionale Bewegungsverfolgungsdaten, die Objektpfade enthalten. Verwendet `track_path` und optional `track_visibility`; wenn `track_visibility` fehlt, werden alle Tracks als sichtbar behandelt. | TRACKS | Nein | - |
| `strength` | Stärke der Track-Konditionierung. (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 |
| `width` | Die Breite des Ausgabevideos. Muss durch 16 teilbar sein. (Standard: 832) | INT | Ja | 16 - MAX_RESOLUTION |
| `height` | Die Höhe des Ausgabevideos. Muss durch 16 teilbar sein. (Standard: 480) | INT | Ja | 16 - MAX_RESOLUTION |
| `length` | Die Anzahl der Frames in der Videosequenz, in Schritten von 4. (Standard: 81) | INT | Ja | 1 - MAX_RESOLUTION |
| `batch_size` | Die Batch-Größe für die Latent-Ausgabe. (Standard: 1) | INT | Ja | 1 - 4096 |
| `start_image` | Das Startbild oder die zu kodierende Bildsequenz. | IMAGE | Ja | - |
| `clip_vision_output` | Optionale Ausgabe eines CLIP-Vision-Modells, die der Konditionierung hinzugefügt wird. | CLIP_VISION_OUTPUT | Nein | - |

**Hinweis:** Der Parameter `strength` hat nur dann eine Wirkung, wenn `tracks` bereitgestellt werden und `strength` größer als 0.0 ist; die Track-Konditionierung wird nur angewendet, wenn zusätzlich `start_image` bereitgestellt wird. Wenn `tracks` nicht bereitgestellt werden oder `strength` 0.0 ist, wird die Track-Mischung übersprungen. Wenn die Track-Mischung aktiv ist, erhält die positive Konditionierung das track-gemischte latente Bild, während die negative Konditionierung das unveränderte latente Bild erhält. Wenn `start_image` nicht bereitgestellt wird, wird keine latente Bild- und Masken-Konditionierung erstellt; die positive und negative Konditionierung werden unverändert durchgereicht (außer dass `clip_vision_output` weiterhin hinzugefügt wird, sofern bereitgestellt), und der Node gibt ein leeres Latent aus.

**Hinweis:** Wenn `start_image` bereitgestellt wird, wird die Bildsequenz auf die Zielwerte für `width` und `height` skaliert und auf die ersten `length` Frames gekürzt. Wenn die Sequenz kürzer als `length` ist, werden die verbleibenden Frames mit neutralgrauen Frames (Wert 0.5) aufgefüllt, bevor die VAE-Kodierung erfolgt. Die resultierende Konditionierung enthält eine `concat_mask` mit Wert 0 an den zeitlichen Positionen, die den Startbild-Frames entsprechen, und 1 an allen anderen Stellen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierte positive Konditionierung, die möglicherweise `concat_latent_image`, `concat_mask` und `clip_vision_output` enthält. | CONDITIONING |
| `negative` | Die modifizierte negative Konditionierung, die möglicherweise `concat_latent_image`, `concat_mask` und `clip_vision_output` enthält. | CONDITIONING |
| `latent` | Ein leerer Latent-Tensor mit der Form `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`, bestimmt durch die Eingaben `batch_size`, `length`, `height` und `width`. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/de.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
