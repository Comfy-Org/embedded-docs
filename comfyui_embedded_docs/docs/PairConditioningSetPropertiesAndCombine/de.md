# PairConditioningSetPropertiesAndCombine

Der Node PairConditioningSetPropertiesAndCombine modifiziert und kombiniert Conditioning-Paare, indem er neue Conditioning-Daten auf bestehende positive und negative Conditioning-Eingaben anwendet. Er ermöglicht es Ihnen, die Stärke des angewendeten Conditionings anzupassen und zu steuern, wie der Conditioning-Bereich festgelegt wird. Dieser Node ist besonders nützlich für fortgeschrittene Workflows zur Conditioning-Manipulation, bei denen Sie mehrere Conditioning-Quellen miteinander vermischen müssen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die ursprüngliche positive Conditioning-Eingabe | CONDITIONING | Ja | - |
| `negative` | Die ursprüngliche negative Conditioning-Eingabe | CONDITIONING | Ja | - |
| `positive_NEW` | Die neue positive Conditioning, die angewendet werden soll | CONDITIONING | Ja | - |
| `negative_NEW` | Die neue negative Conditioning, die angewendet werden soll | CONDITIONING | Ja | - |
| `strength` | Der Stärkefaktor für die Anwendung des neuen Conditionings (Standard: 1.0) | FLOAT | Ja | 0.0 bis 10.0 |
| `set_cond_area` | Steuert, wie der Conditioning-Bereich angewendet wird (Standard: "default") | STRING | Ja | "default"<br>"mask bounds" |
| `mask` | Optionale Maske, um den Anwendungsbereich des Conditionings einzuschränken | MASK | Nein | - |
| `hooks` | Optionale Hook-Gruppe für erweiterte Steuerung | HOOKS | Nein | - |
| `timesteps` | Optionale Spezifikation eines Timestep-Bereichs | TIMESTEPS_RANGE | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die kombinierte positive Conditioning-Ausgabe | CONDITIONING |
| `negative` | Die kombinierte negative Conditioning-Ausgabe | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/de.md)

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
