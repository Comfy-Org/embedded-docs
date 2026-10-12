# KlingCameraControls

Der Node „Kling Camera Controls“ ermöglicht es Ihnen, verschiedene Kamera-Bewegungs- und Rotationsparameter zu konfigurieren, um Motion-Control-Effekte bei der Videogenerierung zu erzeugen. Er bietet Steuerelemente für Kamerapositionierung, Rotation und Zoom, um unterschiedliche Kamerabewegungen zu simulieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `camera_control_type` | Gibt den Typ der zu verwendenden Kamerasteuerungskonfiguration an | COMBO | Ja | `"simple"`<br>`"advanced"` |
| `horizontal_movement` | Steuert die Bewegung der Kamera entlang der horizontalen Achse (x-Achse). Negativ bedeutet nach links, positiv bedeutet nach rechts (Standard: 0.0) | FLOAT | Nein | -10.0 bis 10.0 |
| `vertical_movement` | Steuert die Bewegung der Kamera entlang der vertikalen Achse (y-Achse). Negativ bedeutet nach unten, positiv bedeutet nach oben (Standard: 0.0) | FLOAT | Nein | -10.0 bis 10.0 |
| `pan` | Steuert die Rotation der Kamera in der vertikalen Ebene (x-Achse). Negativ bedeutet Rotation nach unten, positiv bedeutet Rotation nach oben (Standard: 0.5) | FLOAT | Nein | -10.0 bis 10.0 |
| `tilt` | Steuert die Rotation der Kamera in der horizontalen Ebene (y-Achse). Negativ bedeutet Rotation nach links, positiv bedeutet Rotation nach rechts (Standard: 0.0) | FLOAT | Nein | -10.0 bis 10.0 |
| `roll` | Steuert den Rollwinkel der Kamera (z-Achse). Negativ bedeutet gegen den Uhrzeigersinn, positiv bedeutet im Uhrzeigersinn (Standard: 0.0) | FLOAT | Nein | -10.0 bis 10.0 |
| `zoom` | Steuert die Änderung der Brennweite der Kamera. Negativ bedeutet ein engeres Sichtfeld, positiv bedeutet ein weiteres Sichtfeld (Standard: 0.0) | FLOAT | Nein | -10.0 bis 10.0 |

**Hinweis:** Mindestens einer der Kamerasteuerungsparameter (`horizontal_movement`, `vertical_movement`, `pan`, `tilt`, `roll` oder `zoom`) muss einen Wert ungleich null haben, damit die Konfiguration gültig ist.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `camera_control` | Gibt die konfigurierten Kamerasteuerungseinstellungen zur Verwendung in der Videogenerierung zurück | CAMERA_CONTROL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControls/de.md)

---
**Source fingerprint (SHA-256):** `dbba1083b662bb2563c77dec857e4f3123e4e53d58a1d51f2646288af28ebba0`
