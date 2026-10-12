# UNetSelfAttentionMultiply

Der UNetSelfAttentionMultiply-Knoten wendet Multiplikationsfaktoren auf die Query-, Key-, Value- und Output-Komponenten des Self-Attention-Mechanismus in einem UNet-Modell an. Er ermöglicht es, verschiedene Teile der Attention-Berechnung zu skalieren, um zu experimentieren, wie sich Attention-Gewichte auf das Verhalten des Modells auswirken.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das UNet-Modell, das mit Attention-Skalierungsfaktoren geändert werden soll | MODEL | Ja | - |
| `q` | Multiplikationsfaktor für die Query-Komponente (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `k` | Multiplikationsfaktor für die Key-Komponente (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `v` | Multiplikationsfaktor für die Value-Komponente (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |
| `out` | Multiplikationsfaktor für die Output-Komponente (Standard: 1.0) | FLOAT | Nein | 0.0 - 10.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `MODEL` | Das modifizierte UNet-Modell mit skalierten Attention-Komponenten | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/de.md)

---
**Source fingerprint (SHA-256):** `7a6039eb2faae56437a5eb6fe01be6d38e53c0632175a3405a1e24a476d4da82`
