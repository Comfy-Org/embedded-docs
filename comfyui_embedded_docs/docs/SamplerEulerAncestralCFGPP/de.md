# SamplerEulerAncestralCFG++

Der Node SamplerEulerAncestralCFG++ erstellt einen Sampler, der die Euler-Ancestral-Methode mit Classifier-Free-Guidance (CFG++) für die Bildgenerierung verwendet. Dieser Sampler kombiniert Ancestral-Sampling-Techniken mit Guidance-Konditionierung, um vielfältige Bildvariationen bei gleichbleibender Kohärenz zu erzeugen, und ermöglicht eine Feinabstimmung über Parameter, die Rauschen und Schrittgrößenanpassungen steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `eta` | Steuert die Schrittgröße während des Samplings, wobei höhere Werte zu aggressiveren Aktualisierungen führen (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |
| `s_noise` | Passt die Menge des während des Sampling-Prozesses hinzugefügten Rauschens an (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt ein konfiguriertes Sampler-Objekt zurück, das in der Bildgenerierungspipeline verwendet werden kann | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/de.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
