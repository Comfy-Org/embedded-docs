# CLIP-Hooks festlegen

Der Node SetClipHooks ermöglicht es Ihnen, benutzerdefinierte Hooks auf ein CLIP-Modell anzuwenden, wodurch erweiterte Änderungen an dessen Verhalten möglich sind. Er kann Hooks auf Conditioning-Ausgaben anwenden und optional die CLIP-Scheduling-Funktionalität aktivieren. Dieser Node erstellt eine geklonte Kopie des eingegebenen CLIP-Modells mit den angegebenen Hook-Konfigurationen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das CLIP-Modell, auf das Hooks angewendet werden sollen | CLIP | Ja | - |
| `apply_to_conds` | Ob Hooks auf Conditioning-Ausgaben angewendet werden sollen (Standard: True) | BOOLEAN | Ja | - |
| `schedule_clip` | Ob CLIP-Scheduling aktiviert werden soll (Standard: False) | BOOLEAN | Ja | - |
| `hooks` | Optionale Hook-Gruppe, die auf das CLIP-Modell angewendet werden soll | HOOKS | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Ein geklontes CLIP-Modell, auf das die angegebenen Hooks angewendet wurden | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/de.md)

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`
