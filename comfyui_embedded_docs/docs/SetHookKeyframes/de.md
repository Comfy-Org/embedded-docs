# Hook-Keyframes festlegen

Der Node Set Hook Keyframes ermöglicht es, Keyframe-Zeitplanung auf vorhandene Hook-Gruppen anzuwenden. Er nimmt eine Hook-Gruppe entgegen und wendet optional Timing-Informationen für Keyframes an, um zu steuern, wann verschiedene Hooks während des Generierungsprozesses ausgeführt werden. Wenn Keyframes bereitgestellt werden, klont der Node die Hook-Gruppe und legt das Keyframe-Timing für alle Hooks innerhalb der Gruppe fest.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `hooks` | Die Hook-Gruppe, auf die die Keyframe-Zeitplanung angewendet wird | HOOKS | Ja | - |
| `hook_kf` | Optionale Keyframe-Gruppe mit Timing-Informationen für die Hook-Ausführung | HOOK_KEYFRAMES | Nein | - |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `hooks` | Die geänderte Hook-Gruppe mit angewendeter Keyframe-Zeitplanung (geklont, wenn Keyframes bereitgestellt wurden) | HOOKS |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/de.md)

---
**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`
