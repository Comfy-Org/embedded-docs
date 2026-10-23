# ConditioningSetDefaultAndCombine

Dieser Node kombiniert eine primäre Conditioning-Eingabe mit einer Standard-Conditioning-Eingabe mithilfe eines Hook-basierten Systems. Er führt die beiden Conditioning-Quellen zu einer einzigen Ausgabe zusammen, wodurch das Standard-Conditioning als Fallback oder Basis dienen kann, wenn das primäre Conditioning unvollständig ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standardwert | Bereich |
| --- | --- | --- | --- | --- | --- |
| `cond` | Die primäre Conditioning-Eingabe, die verarbeitet und kombiniert werden soll | CONDITIONING | Erforderlich | - | - |
| `cond_DEFAULT` | Die Standard-Conditioning-Daten, die mit dem primären Conditioning kombiniert werden sollen | CONDITIONING | Erforderlich | - | - |
| `hooks` | Optionale Hook-Konfiguration, die steuert, wie die Conditioning-Daten verarbeitet und kombiniert werden | HOOKS | Optional | - | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die kombinierten Conditioning-Daten, die aus dem Zusammenführen der primären und der Standard-Conditioning-Eingaben resultieren | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultCombine/de.md)

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
