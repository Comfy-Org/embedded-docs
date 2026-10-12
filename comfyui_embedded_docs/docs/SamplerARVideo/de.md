# SamplerARVideo

Der Node „Sampler AR Video“ bietet eine spezialisierte Sampling-Methode für autoregressive Videomodelle, beispielsweise für Modelle, die Causal-Forcing- oder Self-Forcing-Techniken verwenden. Er verwaltet alle Parameter, die mit der autoregressiven (AR-)Schleife zusammenhängen, direkt im Workflow, sodass sich einfach konfigurieren lässt, wie das Modell Videoframes Schritt für Schritt generiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Frames pro autoregressivem Block. Ein Wert von 1 bedeutet, dass das Modell jeweils ein Frame auf einmal generiert (framewise), während ein Wert von 3 bedeutet, dass es drei Frames zusammen generiert (chunkwise). Diese Einstellung muss mit dem Trainingsmodus des Checkpoints übereinstimmen. Standard: 1. | INT | Ja | 1 bis 64 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `SAMPLER` | Ein konfiguriertes Sampler-Objekt, das die Sampling-Funktion „ar_video“ mit den angegebenen autoregressiven Parametern verwendet. | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/de.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
