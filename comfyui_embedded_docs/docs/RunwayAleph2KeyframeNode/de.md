# RunwayAleph2KeyframeNode

Der Runway Aleph2 Keyframe-Node verankert ein Steuerungsbild an einem bestimmten Zeitpunkt Ihres Eingabevideos, sodass das Aleph2-Modell die Bearbeitung an dieser Stelle in Ihrem Material steuert. Verbinden Sie diesen Node mit dem Eingang "keyframes" des Runway Aleph2 Video to Video-Node und verketten Sie mehrere davon (bis zu 5) über den optionalen "keyframes"-Eingang.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das Steuerungsbild, das am gewählten Zeitpunkt des Eingabevideos angewendet wird. | IMAGE | Ja | - |
| `timing` | Wie dieses Bild auf der Zeitachse des Eingabevideos platziert wird. | COMBO | Ja | "Absolute seconds"<br>"Fraction of duration" |
| `keyframes` | Optionale frühere Keyframes, die mit diesem verkettet werden. | KEYFRAME | Nein | - |

### Details zum `timing`-Parameter

Der Parameter `timing` hat zwei Modi:

- **"Absolute seconds"**: Wenn ausgewählt, erscheint ein Unterparameter `seconds`. Dieser gibt die Zeit in Sekunden ab Beginn des Eingabevideos an, zu der das Bild angewendet wird (Standard: 0.0, Bereich: 0.0 bis 30.0, Schritt: 0.1).
- **"Fraction of duration"**: Wenn ausgewählt, erscheint ein Unterparameter `fraction`. Dieser gibt an, an welcher Stelle im Eingabevideo das Bild angewendet wird, als Bruchteil seiner Dauer, wobei 0.0 der Anfang und 1.0 das Ende ist (Standard: 0.0, Bereich: 0.0 bis 1.0, Schritt: 0.01).

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `keyframes` | Eine Kette von Keyframes, die diesen und alle zuvor verbundenen Keyframes enthält. | KEYFRAME |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/de.md)

---
**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`
