# HitPaw Videobearbeitung

Der HitPaw Video Enhance-Node verwendet eine externe API, um die Qualität von Videos zu verbessern. Er skaliert Videos mit niedriger Auflösung auf eine höhere Auflösung hoch, entfernt visuelle Artefakte und reduziert Rauschen. Die Verarbeitungskosten werden pro Sekunde des Eingabevideos berechnet.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das KI-Modell, das zur Videoverbesserung verwendet werden soll. Wenn ein Modell ausgewählt wird, wird ein verschachtelter `resolution`-Parameter eingeblendet. Die verfügbaren Modelle und ihre unterstützten Auflösungen variieren. | DYNAMIC_COMBO | Ja | `"Portrait Restore Model (1x)"`<br>`"Portrait Restore Model (2x)"`<br>`"General Restore Model (1x)"`<br>`"General Restore Model (2x)"`<br>`"General Restore Model (4x)"`<br>`"Ultra HD Model (2x)"`<br>`"Generative Model (1x)"` |
| `video` | Die Eingabevideodatei, die verbessert werden soll. | VIDEO | Ja | N/A |

### Portrait Restore, General Restore und Ultra HD Model Eingaben

Diese Auflösungsoptionen werden von Portrait Restore Model (1x), Portrait Restore Model (2x), General Restore Model (1x), General Restore Model (2x), General Restore Model (4x) und Ultra HD Model (2x) gemeinsam verwendet.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.resolution` | Die Zielauflösung für das verbesserte Video. Wenn `"original"` ausgewählt wird, bleibt die Auflösung des Eingabevideos erhalten. | COMBO | Ja | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"`<br>`"8K"` |

### Generative Model (1x) Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model.resolution` | Die Zielauflösung für das verbesserte Video. Wenn `"original"` ausgewählt wird, bleibt die Auflösung des Eingabevideos erhalten. Die Option `"8K"` ist für dieses Modell nicht verfügbar. | COMBO | Ja | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"` |

**Hinweise:**

* Das Eingabevideo `video` muss eine Dauer zwischen 0,5 Sekunden und 60 Minuten (3600 Sekunden) haben.
* Die ausgewählte `resolution` muss mindestens so groß sein wie die Abmessungen des Eingabevideos. Bei quadratischen Videos muss sie mindestens so groß sein wie Breite und Höhe des Videos. Bei nicht quadratischen Videos muss sie mindestens so groß sein wie die kürzere Dimension des Videos. Ist die Zielauflösung kleiner, wird ein Fehler ausgelöst. Wenn `"original"` ausgewählt wird, bleibt die Auflösung des Eingabevideos erhalten.
* Wenn eine andere Auflösung als `"original"` ausgewählt wird, werden nicht quadratische Videos so skaliert, dass ihre kürzere Dimension der ausgewählten Auflösung entspricht, wobei das Seitenverhältnis beibehalten wird. Quadratische Videos werden so skaliert, dass beide Dimensionen der quadratischen Zielgröße der ausgewählten Auflösung entsprechen (zum Beispiel erzeugt `"4K/UHD"` 2048×2048).

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `video` | Die verbesserte Videodatei. | VIDEO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/de.md)

---
**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`
