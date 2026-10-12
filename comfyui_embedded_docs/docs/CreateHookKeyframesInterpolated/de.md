# CreateHookKeyframesInterpolated

Erzeugt eine Sequenz von Hook-Keyframes mit interpolierten Stärkewerten zwischen einem Start- und Endpunkt. Der Node generiert mehrere Keyframes, die den Stärke-Parameter über einen angegebenen Prozentbereich des Generierungsprozesses sanft übergehen lassen, wobei verschiedene Interpolationsmethoden zur Steuerung der Übergangskurve verwendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `strength_start` | Der Startstärkewert für die Interpolationssequenz (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `strength_end` | Der Endstärkewert für die Interpolationssequenz (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `interpolation` | Die Interpolationsmethode, die für den Übergang zwischen den Stärkewerten verwendet wird (Standard: LINEAR) | COMBO | Ja | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `start_percent` | Die Startprozentposition im Generierungsprozess (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Die Endprozentposition im Generierungsprozess (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `keyframes_count` | Die Anzahl der zu generierenden Keyframes in der Interpolationssequenz (Standard: 5) | INT | Ja | 2 - 100 |
| `print_keyframes` | Ob generierte Keyframe-Informationen im Log ausgegeben werden sollen (Standard: False) | BOOLEAN | Ja | True/False |
| `prev_hook_kf` | Optionale vorherige Gruppe von Hook-Keyframes, an die angehängt werden soll | HOOK_KEYFRAMES | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOK_KF` | Die generierte Gruppe von Hook-Keyframes mit der interpolierten Sequenz | HOOK_KEYFRAMES |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/de.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
