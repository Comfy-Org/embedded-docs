# WebcamCapture

Der Node WebcamCapture erfasst Bilder von einem Webcam-Gerät und konvertiert sie in ein Format, das innerhalb von ComfyUI-Workflows verwendet werden kann. Er erbt vom Node LoadImage und bietet Optionen zur Steuerung der Aufnahmeabmessungen und des Zeitpunkts. Wenn aktiviert, kann der Node bei jeder Verarbeitung der Workflow-Warteschlange neue Bilder erfassen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Die Webcam-Eingabequelle, von der Bilder erfasst werden | WEBCAM | Ja | - |
| `width` | Die gewünschte Breite für das erfasste Bild (Standard: 0, verwendet die native Auflösung der Webcam) | INT | Ja | 0 bis MAX_RESOLUTION |
| `height` | Die gewünschte Höhe für das erfasste Bild (Standard: 0, verwendet die native Auflösung der Webcam) | INT | Ja | 0 bis MAX_RESOLUTION |
| `capture_on_queue` | Wenn aktiviert, wird bei jeder Verarbeitung der Workflow-Warteschlange ein neues Bild erfasst (Standard: True) | BOOLEAN | Ja | - |

**Hinweis:** Wenn sowohl `width` als auch `height` auf 0 gesetzt sind, verwendet der Node die native Auflösung der Webcam. Wenn eine der beiden Dimensionen auf einen Wert ungleich 0 gesetzt wird, wird das erfasste Bild entsprechend skaliert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Das erfasste Webcam-Bild, konvertiert in ComfyUIs Bildformat | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/de.md)

---
**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`
