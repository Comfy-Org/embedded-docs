# Hook-Keyframes aus Floats erstellen

Dieser Node erzeugt Hook-Keyframes aus einer Liste von Gleitkomma-Stärkewerten und verteilt sie gleichmäßig zwischen angegebenen Start- und End-Prozentsätzen. Er erzeugt eine Sequenz von Keyframes, bei der jeder Stärkewert einer bestimmten Prozentposition in der Animationszeitleiste zugewiesen wird. Der Node kann entweder eine neue Keyframe-Gruppe erstellen oder zu einer vorhandenen hinzufügen, mit einer Option, die erzeugten Keyframes zu Debugging-Zwecken auszugeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `floats_strength` | Ein einzelner Float-Wert oder eine Liste von Float-Werten, die Stärkewerte für die Keyframes darstellen (Standard: -1) | FLOATS | Ja | -1 bis ∞ |
| `start_percent` | Die Start-Prozentposition für den ersten Keyframe in der Zeitleiste (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `end_percent` | Die End-Prozentposition für den letzten Keyframe in der Zeitleiste (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `print_keyframes` | Wenn aktiviert, werden die Informationen zu den erzeugten Keyframes in der Konsole ausgegeben (Standard: False) | BOOLEAN | Ja | True/False |
| `prev_hook_kf` | Eine vorhandene Hook-Keyframe-Gruppe, zu der die neuen Keyframes hinzugefügt werden, oder es wird eine neue Gruppe erstellt, wenn keine bereitgestellt wird | HOOK_KEYFRAMES | Nein | - |

**Hinweis:** Der Parameter `floats_strength` akzeptiert entweder einen einzelnen Float-Wert oder eine iterierbare Liste von Floats. Die Keyframes werden linear zwischen `start_percent` und `end_percent` basierend auf der Anzahl der bereitgestellten Stärkewerte verteilt. Der erste Keyframe hat garantiert mindestens einen Schritt, um sicherzustellen, dass er angewendet wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOK_KF` | Eine Hook-Keyframe-Gruppe, die die neu erstellten Keyframes enthält, entweder als neue Gruppe oder an die eingegebene Keyframe-Gruppe angehängt | HOOK_KEYFRAMES |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/de.md)

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`
