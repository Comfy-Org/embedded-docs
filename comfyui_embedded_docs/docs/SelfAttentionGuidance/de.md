# SelfAttentionGuidance

Der Knoten Self-Attention Guidance wendet Guidance auf Diffusionsmodelle an, indem er den Attention-Mechanismus während des Sampling-Prozesses modifiziert. Er erfasst Attention-Scores aus unbedingten Denoising-Schritten und verwendet sie, um unscharfe Guidance-Karten zu erstellen, die die endgültige Ausgabe beeinflussen. Diese Technik hilft, den Generierungsprozess zu steuern, indem sie die eigenen Attention-Muster des Modells nutzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das Self-Attention-Guidance angewendet werden soll | MODEL | Ja | - |
| `scale` | Die Stärke des Self-Attention-Guidance-Effekts (Standard: 0.5) | FLOAT | Nein | -2.0 bis 5.0 |
| `blur_sigma` | Der Grad der Unschärfe, der zum Erstellen der Guidance-Karte angewendet wird (Standard: 2.0) | FLOAT | Nein | 0.0 bis 10.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter Self-Attention-Guidance | MODEL |

**Hinweis:** Dieser Knoten ist derzeit experimentell und weist Einschränkungen bei Chunked-Batches auf. Er kann Attention-Scores nur aus einem UNet-Aufruf speichern und funktioniert möglicherweise nicht ordnungsgemäß bei größeren Batchgrößen.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/de.md)

---
**Source fingerprint (SHA-256):** `ab8f7a0cf19c85f8e77b2d6b380c0224a407a900a42341de7503f5394a3216fb`
