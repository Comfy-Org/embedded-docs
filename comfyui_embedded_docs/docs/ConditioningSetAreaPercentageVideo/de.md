# ConditioningSetAreaPercentageVideo

Der Node ConditioningSetAreaPercentageVideo modifiziert Konditionierungsdaten, indem er einen bestimmten räumlichen Bereich und zeitlichen Abschnitt für die Videogenerierung definiert. Er verwendet Prozentwerte relativ zu den Gesamtabmessungen, um Position, Größe und Dauer des Bereichs festzulegen, in dem die Konditionierung angewendet wird. Dies ist nützlich, um die Generierung auf bestimmte Teile einer Videosequenz zu fokussieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `conditioning` | Die zu ändernden Konditionierungsdaten | CONDITIONING | Ja | - |
| `width` | Die Breite des Bereichs als Prozentsatz der Gesamtbreite (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `height` | Die Höhe des Bereichs als Prozentsatz der Gesamthöhe (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `temporal` | Die zeitliche Dauer des Bereichs als Prozentsatz der gesamten Videolänge (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `x` | Die horizontale Startposition des Bereichs als Prozentsatz (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `y` | Die vertikale Startposition des Bereichs als Prozentsatz (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `z` | Die zeitliche Startposition des Bereichs als Prozentsatz der Video-Zeitleiste (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 (Schrittweite 0.01) |
| `strength` | Der Stärkemultiplikator, der auf die Konditionierung innerhalb des definierten Bereichs angewendet wird (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 (Schrittweite 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `conditioning` | Die geänderten Konditionierungsdaten mit den angegebenen Bereichs- und Stärkeeinstellungen | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/de.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
