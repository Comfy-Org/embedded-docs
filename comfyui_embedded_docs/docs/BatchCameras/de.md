# Batch Cameras

Fasst Kameras und Kameraorbits in einer Kameraliste zusammen, in der Reihenfolge der Eingaben. Render Mesh und Render Splat rendern ein Bild pro Kamera in der Liste, woraus ein Multi-View-Render aufgebaut wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `cameras` | Erweiterbarer Slot für Kameras aus Create Camera Info, Create Camera Orbit oder einem Viewer. Eine Kameraliste zählt als jede darin enthaltene Kamera. | AUTOGROW | Ja | 1 bis 50 Kameras |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `camera_info` | Eine Kameraliste mit allen Eingabekameras in der Reihenfolge der Eingaben. | LOAD3D_CAMERA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/de.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`
