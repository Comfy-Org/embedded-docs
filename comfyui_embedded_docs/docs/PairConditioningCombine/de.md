# PairConditioningCombine

Der Node PairConditioningCombine führt zwei separate Konditionierungspaare (jeweils bestehend aus einer positiven und einer negativen Konditionierung) zu einem einzigen kombinierten Paar zusammen. Er nimmt die positive und negative Konditionierung aus zwei verschiedenen Quellen und kombiniert sie mithilfe der internen Logik von ComfyUI, wodurch eine finale positive und eine finale negative Konditionierung ausgegeben werden. Dieser Node ist experimentell und für fortgeschrittene Workflows zur Konditionierungsmanipulation gedacht.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive_A` | Erste positive Konditionierungseingabe | CONDITIONING | Ja | - |
| `negative_A` | Erste negative Konditionierungseingabe | CONDITIONING | Ja | - |
| `positive_B` | Zweite positive Konditionierungseingabe | CONDITIONING | Ja | - |
| `negative_B` | Zweite negative Konditionierungseingabe | CONDITIONING | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Kombinierte positive Konditionierungsausgabe | CONDITIONING |
| `negative` | Kombinierte negative Konditionierungsausgabe | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/de.md)

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
