# UNetTemporalAttentionMultiply

Der Node UNetTemporalAttentionMultiply wendet Multiplikationsfaktoren auf verschiedene Arten von Attention-Mechanismen in einem temporalen UNet-Modell an. Er modifiziert das Modell, indem er die Gewichtungen von Self-Attention- und Cross-Attention-Schichten anpasst und dabei zwischen strukturellen und temporalen Komponenten unterscheidet. Dies ermöglicht eine Feinabstimmung des Einflusses, den jeder Attention-Typ auf die Ausgabe des Modells hat.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Eingabemodell, das mit Attention-Multiplikatoren modifiziert werden soll | MODEL | Ja | - |
| `self_structural` | Multiplikator für strukturelle Komponenten der Self-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `self_temporal` | Multiplikator für temporale Komponenten der Self-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `cross_structural` | Multiplikator für strukturelle Komponenten der Cross-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `cross_temporal` | Multiplikator für temporale Komponenten der Cross-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angepassten Attention-Gewichtungen | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/de.md)

---
**Source fingerprint (SHA-256):** `b43c7c51cbc71349dd267c4abe1704899a394e205a60a13b45869f690d83a0f0`
