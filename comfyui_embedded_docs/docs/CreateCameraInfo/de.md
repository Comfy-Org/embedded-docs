# Kamera-Info erstellen

Der Node Create Camera Info erstellt eine Kamerainformationsstruktur für 3D-Rendering. Er unterstützt drei Modi zum Definieren der Kamera: Orbit (Yaw/Pitch/Distance um ein Ziel), look_at (explizite Weltposition) und Quaternion (Position plus Rotation). Das Koordinatensystem ist rechtshändig mit Y als Hochachse.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mode` | Wie die Kamera definiert wird: Orbit-Winkel, eine explizite Position oder eine Position + Quaternion. | DYNAMIC_COMBO | Ja | `"orbit"`<br>`"look_at"`<br>`"quaternion"` |
| `target_x` | Look-at-Punkt (Orbit-Drehpunkt / Ziel). Im Orbit-Modus verschiebt er die gesamte Kamera (Pan/Translate). Im Quaternion-Modus wird er ignoriert. Standardwert ist der Ursprung. (Standard: 0.0) | FLOAT | Nein | -1000.0 bis 1000.0 |
| `target_y` | Y-Komponente des Zielpunkts. (Standard: 0.0) | FLOAT | Nein | -1000.0 bis 1000.0 |
| `target_z` | Z-Komponente des Zielpunkts. (Standard: 0.0) | FLOAT | Nein | -1000.0 bis 1000.0 |
| `roll` | Rollwinkel der Kamera um die Blickachse, in Grad. (Standard: 0.0) | FLOAT | Nein | -180.0 bis 180.0 |
| `fov` | Vertikales Sichtfeld in Grad. (Standard: 35.0) | FLOAT | Nein | 1.0 bis 120.0 |
| `zoom` | Digitaler Zoom (Brennweitenmultiplikator). Werte größer als 1 zoomen heran, ohne die Kamera zu bewegen. (Standard: 1.0) | FLOAT | Nein | 0.01 bis 100.0 |
| `camera_type` | Von Render Splat verwendete Projektion: perspektivisch (Verkürzung) oder orthografisch (parallel). (Standard: "perspective") | COMBO | Nein | `"perspective"`<br>`"orthographic"` |

### Modusspezifische Parameter

Wenn `mode` auf `"orbit"` gesetzt ist, werden die folgenden Parameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `yaw` | Horizontaler Drehwinkel um das Ziel. (Standard: 35.0) | FLOAT | Ja | -360.0 bis 360.0 |
| `pitch` | Vertikaler Drehwinkel um das Ziel. (Standard: 30.0) | FLOAT | Ja | -89.0 bis 89.0 |
| `distance` | Entfernung der Kamera zum Ziel. (Standard: 4.0) | FLOAT | Ja | 0.01 bis 1000.0 |

Wenn `mode` auf `"look_at"` gesetzt ist, werden die folgenden Parameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `position_x` | Kameraposition im Weltkoordinatensystem (rechtshändig, Y-up). (Standard: 4.0) | FLOAT | Ja | -1000.0 bis 1000.0 |
| `position_y` | Y-Komponente der Kameraposition. (Standard: 4.0) | FLOAT | Ja | -1000.0 bis 1000.0 |
| `position_z` | Z-Komponente der Kameraposition. (Standard: 4.0) | FLOAT | Ja | -1000.0 bis 1000.0 |

Wenn `mode` auf `"quaternion"` gesetzt ist, werden die folgenden Parameter verfügbar:

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `position_x` | Kameraposition im Weltkoordinatensystem (rechtshändig, Y-up). (Standard: 4.0) | FLOAT | Ja | -1000.0 bis 1000.0 |
| `position_y` | Y-Komponente der Kameraposition. (Standard: 4.0) | FLOAT | Ja | -1000.0 bis 1000.0 |
| `position_z` | Z-Komponente der Kameraposition. (Standard: 4.0) | FLOAT | Ja | -1000.0 bis 1000.0 |
| `quat_x` | X-Komponente des Quaternions für die Weltrotation der Kamera. (Standard: 0.0) | FLOAT | Ja | -1.0 bis 1.0 |
| `quat_y` | Y-Komponente des Quaternions für die Weltrotation der Kamera. (Standard: 0.0) | FLOAT | Ja | -1.0 bis 1.0 |
| `quat_z` | Z-Komponente des Quaternions für die Weltrotation der Kamera. (Standard: 0.0) | FLOAT | Ja | -1.0 bis 1.0 |
| `quat_w` | Quaternion für die Weltrotation der Kamera (three.js: blickt entlang der lokalen -Z-Achse). Wird für Sie normalisiert. (Standard: 1.0) | FLOAT | Ja | -1.0 bis 1.0 |

**Hinweis:** Die Parameter `target_x`, `target_y` und `target_z` werden ignoriert, wenn `mode` auf `"quaternion"` gesetzt ist. Im Modus `"orbit"` definieren diese Zielparameter den Drehpunkt, um den die Kamera kreist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `camera_info` | Kamerainformationsstruktur mit Position, Rotation, Sichtfeld, Zoom und Projektionstyp für 3D-Rendering. | LOAD3DCAMERA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateCameraInfo/de.md)

---
**Source fingerprint (SHA-256):** `5a9703e8e01ad2cd92a97da8d892c278765a9cef8bcd38e3336d1f73717d9895`
