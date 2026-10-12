# Luma Ray 3.2 Keyframe

Dieser Node verankert ein Referenzbild an einer bestimmten Position auf der Zeitachse des Ausgabevideos von Luma Ray 3.2. Verbinden Sie diesen Node mit dem Eingang "keyframes" des Nodes Luma Ray 3.2 Keyframes to Video und verketten Sie mehrere Keyframes miteinander, indem Sie den optionalen Eingang "keyframes" anschließen.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Referenzbild, das zum gewählten Zeitpunkt des Ausgabevideos platziert wird. | IMAGE | Ja | - |
| `position` | Wie dieses Bild auf der Zeitachse des Ausgabevideos platziert wird. | DYNAMIC_COMBO | Ja | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Optionale frühere Keyframes, die mit diesem verkettet werden. | LUMA_RAY32_KEYFRAME | Nein | - |

### Fraction of duration (0.0-1.0) Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `fraction` | An welcher Stelle im Ausgabevideo dieses Bild angewendet wird (0.0 = Anfang, 1.0 = Ende). Standard: 0.0. | FLOAT | Ja | 0.0 bis 1.0 (Schritt: 0.01) |

### Absolute time (seconds) Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Zeit in Sekunden ab Beginn des Ausgabevideos, an der dieses Bild angewendet wird. Standard: 0.0. | FLOAT | Ja | 0.0 bis 10.0 (Schritt: 0.1) |

Der Parameter `position` bestimmt, welcher Wert verwendet wird, um das Bild auf der Zeitachse zu platzieren. Nur der zur ausgewählten Option gehörende Unterparameter wird angezeigt und verwendet: `fraction` für "Fraction of duration (0.0-1.0)" und `seconds` für "Absolute time (seconds)".

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `keyframes` | Eine Keyframe-Kette, die das neue Keyframe zusammen mit allen optionalen früheren Keyframes enthält. | LUMA_RAY32_KEYFRAME |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/de.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
