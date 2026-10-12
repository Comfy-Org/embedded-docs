# StableCascade_StageB_Conditioning

Der Node StableCascade_StageB_Conditioning bereitet Konditionierungsdaten für die Generierung mit Stable Cascade Stage B vor, indem er vorhandene Konditionierungsinformationen mit der von Stage C erzeugten vorherigen latenten Repräsentation kombiniert. Er kopiert jeden Konditionierungseintrag und speichert die latenten Samples von Stage C darin, sodass spätere Generierungsschritte diese vorherigen Informationen für kohärentere Ergebnisse nutzen können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `conditioning` | Die Konditionierungsdaten, die mit den vorherigen Informationen von Stage C modifiziert werden sollen. Jeder Eintrag in der Liste wird kopiert und erhält die Stage-C-Samples. | CONDITIONING | Ja | - |
| `stage_c` | Die latente Repräsentation von Stage C. Ihr Wert `samples` wird als vorherige Information verwendet, die den Konditionierungsdaten hinzugefügt wird. | LATENT | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CONDITIONING` | Die modifizierten Konditionierungsdaten mit integrierten vorherigen Informationen von Stage C. | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
