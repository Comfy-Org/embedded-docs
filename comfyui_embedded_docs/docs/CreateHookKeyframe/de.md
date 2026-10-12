# Hook-Keyframe erstellen

Der Node „Create Hook Keyframe“ ermöglicht es Ihnen, bestimmte Punkte in einem Generierungsprozess zu definieren, an denen sich das Hook-Verhalten ändert. Er erstellt Keyframes, die die Stärke von Hooks bei bestimmten Prozentwerten des Generierungsfortschritts ändern. Diese Keyframes können miteinander verkettet werden, um komplexe Planungsmuster zu erstellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `strength_mult` | Multiplikator für die Hook-Stärke an diesem Keyframe (Standard: 1.0) | FLOAT | Ja | -20.0 bis 20.0 |
| `start_percent` | Der Prozentpunkt im Generierungsprozess, an dem dieses Keyframe wirksam wird (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `prev_hook_kf` | Optionale vorherige Hook-Keyframe-Gruppe, zu der dieses Keyframe hinzugefügt werden soll | HOOK_KEYFRAMES | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `HOOK_KF` | Eine Gruppe von Hook-Keyframes einschließlich des neu erstellten Keyframes | HOOK_KEYFRAMES |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/de.md)

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`
