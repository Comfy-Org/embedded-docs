# DisableNoise

Dieser Node stellt eine leere Rauschkonfiguration bereit, die die Rauschgenerierung während des Samplings deaktiviert. Er gibt ein spezielles Noise-Objekt aus, das keine Rauschdaten enthält, sodass jeder damit verbundene Node rauschbezogene Operationen überspringt. Er ist außerdem unter dem Alias „zero noise“ auffindbar.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| *Keine Eingabeparameter* | Dieser Node benötigt keine Eingabeparameter. | - | - | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `NOISE` | Gibt eine leere Rauschkonfiguration zurück, die verwendet werden kann, um die Rauschgenerierung in Sampling-Prozessen zu deaktivieren. | NOISE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/de.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
