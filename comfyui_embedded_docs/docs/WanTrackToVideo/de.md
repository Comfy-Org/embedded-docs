# WanTrackToVideo

Der WanTrackToVideo-Node wandelt Motion-Tracking-Daten in Videosequenzen um, indem er Track-Punkte verarbeitet und entsprechende Videoframes generiert. Er nimmt Tracking-Koordinaten als Eingabe entgegen und erzeugt Video-Konditionierung und latente Repräsentationen, die für die Videogenerierung verwendet werden können. Wenn keine Tracks bereitgestellt werden, fällt er auf die standardmäßige Bild-zu-Video-Konvertierung zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierung für die Videogenerierung | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierung für die Videogenerierung | CONDITIONING | Ja | - |
| `vae` | VAE-Modell zum Kodieren und Dekodieren | VAE | Ja | - |
| `tracks` | JSON-formatierte Tracking-Daten als mehrzeiliger String (Standard: "[]"). Jeder Track wird auf eine feste Länge von 121 Punkten aufgefüllt oder gekürzt. | STRING | Ja | - |
| `width` | Ausgabebreite des Videos in Pixeln (Standard: 832, Schrittweite: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Ausgabehöhe des Videos in Pixeln (Standard: 480, Schrittweite: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames im Ausgabevideo (Standard: 81, Schrittweite: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `temperature` | Temperaturparameter für Motion-Patching (Standard: 220.0, Schrittweite: 0.1). Erweiterte Einstellung. | FLOAT | Ja | 1.0 bis 1000.0 |
| `topk` | Top-k-Wert für Motion-Patching (Standard: 2). Erweiterte Einstellung. | INT | Ja | 1 bis 10 |
| `start_image` | Startbild für die Videogenerierung | IMAGE | Nein | - |
| `clip_vision_output` | CLIP-Vision-Ausgabe für zusätzliche Konditionierung | CLIP_VISION_OUTPUT | Nein | - |

**Hinweis:** Wenn `tracks` gültige Tracking-Daten enthält, verarbeitet der Node Motion-Tracks, um ein Video zu generieren. Wenn `tracks` leer ist, wechselt er in den Standardmodus für Bild-zu-Video. Wenn `start_image` bereitgestellt wird, wird das erste Frame der Videosequenz initialisiert, und das Ergebnis des Motion-Patchings wird sowohl zur positiven als auch zur negativen Konditionierung hinzugefügt. Wenn `clip_vision_output` bereitgestellt wird, wird es ebenfalls sowohl zur positiven als auch zur negativen Konditionierung hinzugefügt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierung mit angewendeten Motion-Track-Informationen | CONDITIONING |
| `negative` | Negative Konditionierung mit angewendeten Motion-Track-Informationen | CONDITIONING |
| `latent` | Generierte latente Videorepräsentation | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/de.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
