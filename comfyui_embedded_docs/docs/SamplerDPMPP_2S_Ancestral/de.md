# SamplerDPMPP_2S_Ancestral

Der SamplerDPMPP_2S_Ancestral-Node erstellt einen Sampler, der die Sampling-Methode DPM++ 2S Ancestral zur Bilderzeugung verwendet. Dieser Sampler kombiniert deterministische und stochastische Elemente, um variierte Ergebnisse zu erzeugen und dennoch eine gewisse Konsistenz beizubehalten. Er ermöglicht die Steuerung von Zufälligkeit und Rauschpegeln während des Sampling-Prozesses.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `eta` | Steuert die Menge des während des Samplings hinzugefügten stochastischen Rauschens (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 (Schritt 0.01) |
| `s_noise` | Steuert die Skalierung des während des Sampling-Prozesses angewendeten Rauschens (Standard: 1.0) | FLOAT | Ja | 0.0 - 100.0 (Schritt 0.01) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `sampler` | Gibt ein konfiguriertes Sampler-Objekt zurück, das in der Sampling-Pipeline verwendet werden kann | SAMPLER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/de.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
