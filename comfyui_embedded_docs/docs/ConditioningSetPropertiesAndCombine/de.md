# Kond.-Eigenschaften festlegen und kombinieren

Der Node ConditioningSetPropertiesAndCombine ändert Konditionierungsdaten, indem er Eigenschaften von einer neuen Konditionierungseingabe auf eine vorhandene Konditionierungseingabe anwendet. Er kombiniert die beiden Konditionierungs-Sets, während er die Stärke der neuen Konditionierung steuert und festlegt, wie der Konditionierungsbereich angewendet werden soll.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `cond` | Die ursprünglichen Konditionierungsdaten, die geändert werden sollen | CONDITIONING | Erforderlich | - | - |
| `cond_NEW` | Die neuen Konditionierungsdaten, die anzuwendende Eigenschaften bereitstellen | CONDITIONING | Erforderlich | - | - |
| `strength` | Steuert die Intensität der Eigenschaften der neuen Konditionierung | FLOAT | Erforderlich | 1.0 | 0.0 - 10.0 |
| `set_cond_area` | Bestimmt, wie der Konditionierungsbereich angewendet wird | STRING | Erforderlich | default | ["default", "mask bounds"] |
| `mask` | Optionale Maske, um bestimmte Bereiche für die Konditionierung festzulegen | MASK | Optional | - | - |
| `hooks` | Optionale Hook-Funktionen für benutzerdefinierte Verarbeitung | HOOKS | Optional | - | - |
| `timesteps` | Optionaler Zeitschrittbereich, um zu steuern, wann die Konditionierung angewendet wird | TIMESTEPS_RANGE | Optional | - | - |

**Hinweis:** Wenn `mask` angegeben ist, kann der Parameter `set_cond_area` "mask bounds" verwenden, um die Anwendung der Konditionierung auf die maskierten Bereiche zu beschränken.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die kombinierten Konditionierungsdaten mit geänderten Eigenschaften | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/de.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
