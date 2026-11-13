# Create Camera Orbit

Erstellt ein Kamera-Rig um das Ziel der ersten Kamera: standardmäßig ein Turntable, bei gesetztem `pitch` ein geneigter Sweep und optional Ansichten direkt nach unten und nach oben. Render Mesh rendert ein Bild pro Kamera, und Bake Texture From Views projiziert diese zurück auf das Mesh.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `camera_info` | Erste Kamera des Orbits. Bei einer Kameraliste wird jede darin enthaltene Kamera umkreist. | LOAD3D_CAMERA | Ja | - |
| `count` | Kameras, gleichmäßig entlang des Sweeps verteilt. Standard: 4. | INT | Ja | 1 bis 64 |
| `yaw` | Gesamtdrehung um das Ziel, in der Yaw-Richtung von Create Camera Info. Vollständige Drehungen enden einen Schritt vor der ersten Kamera; andere Sweeps enden an der letzten Kamera. Standard: 360.0. | FLOAT | Ja | -720.0 bis 720.0 (Schritt 1.0) |
| `pitch` | Gesamtneigung über dem Ziel, positiv ansteigend wie der Pitch von Create Camera Info; über 90 hinaus passieren die Kameras die Oberseite. Vollständige Drehungen laufen wie `yaw` in einer Schleife. Standard: 0.0. | FLOAT | Ja | -720.0 bis 720.0 (Schritt 1.0) |
| `poles` | Ansichten direkt nach unten und/oder oben auf das Ziel, nach dem Orbit hinzugefügt. Ihre Bildoberseite zeigt von der ersten Kamera weg. Standard: `"none"`. | COMBO | Ja | `"none"`<br>`"top"`<br>`"bottom"`<br>`"top and bottom"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `camera_info` | Die Kameraliste des Rigs, in Orbit-Reihenfolge, gefolgt von den Polansichten. | LOAD3D_CAMERA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraOrbit/de.md)

---
**Source fingerprint (SHA-256):** `b251efc969f8db7cf03527594be3bbd2af037f1ebb56bdf508bf264ddd9f8c08`
