# SamplerLMS

Der SamplerLMS-Node erstellt einen Least-Mean-Squares-(LMS-)Sampler zur Verwendung in Diffusionsmodellen. Er erzeugt ein Sampler-Objekt, das im Sampling-Prozess verwendet werden kann und es Ihnen ermöglicht, die Ordnung des LMS-Algorithmus für numerische Stabilität und Genauigkeit zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `order` | Der Parameter `order` für den LMS-Sampler-Algorithmus, der die Genauigkeit und Stabilität der numerischen Methode steuert (Standard: 4). Dieser Parameter wird im erweiterten Bereich der Node-Oberfläche angezeigt. | INT | Ja | 1 bis 100 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Ein konfiguriertes LMS-Sampler-Objekt, das in der Sampling-Pipeline verwendet werden kann | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/de.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
