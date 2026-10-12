# UNetCrossAttentionMultiply

Der Node `UNetCrossAttentionMultiply` wendet Multiplikationsfaktoren auf den Cross-Attention-Mechanismus in einem UNet-Modell an. Er ermöglicht es Ihnen, die Query-, Key-, Value- und Output-Komponenten der Cross-Attention-Schichten zu skalieren, um mit unterschiedlichen Attention-Verhalten und Effekten zu experimentieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das UNet-Modell, das mit Attention-Skalierungsfaktoren geändert werden soll | MODEL | Ja | - |
| `q` | Skalierungsfaktor für Query-Komponenten in Cross-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `k` | Skalierungsfaktor für Key-Komponenten in Cross-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `v` | Skalierungsfaktor für Value-Komponenten in Cross-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `out` | Skalierungsfaktor für Output-Komponenten in Cross-Attention (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte UNet-Modell mit skalierten Cross-Attention-Komponenten | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/de.md)

---
**Source fingerprint (SHA-256):** `f55a6809be88bfb32fa2c70fabd0e5bb7360be78670c9473d4a79517b811454e`
