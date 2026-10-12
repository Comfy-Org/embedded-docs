# ScaleROPE

Der ScaleROPE-Node ermöglicht es Ihnen, das Rotary Position Embedding (ROPE) eines Modells zu ändern, indem Sie getrennte Skalierungs- und Verschiebungsfaktoren auf seine X-, Y- und T-(Zeit-)Komponenten anwenden. Er ist ein fortgeschrittener, experimenteller Node, mit dem das Verhalten der Positionskodierung des Modells angepasst wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, dessen ROPE-Parameter geändert werden. | MODEL | Ja | - |
| `scale_x` | Der Skalierungsfaktor, der auf die X-Komponente des ROPE angewendet wird (Standard: 1.0). | FLOAT | Ja | 0.0 - 100.0 (Schrittweite 0.1) |
| `shift_x` | Der Verschiebungswert, der auf die X-Komponente des ROPE angewendet wird (Standard: 0.0). | FLOAT | Ja | -256.0 - 256.0 (Schrittweite 0.1) |
| `scale_y` | Der Skalierungsfaktor, der auf die Y-Komponente des ROPE angewendet wird (Standard: 1.0). | FLOAT | Ja | 0.0 - 100.0 (Schrittweite 0.1) |
| `shift_y` | Der Verschiebungswert, der auf die Y-Komponente des ROPE angewendet wird (Standard: 0.0). | FLOAT | Ja | -256.0 - 256.0 (Schrittweite 0.1) |
| `scale_t` | Der Skalierungsfaktor, der auf die T-(Zeit-)Komponente des ROPE angewendet wird (Standard: 1.0). | FLOAT | Ja | 0.0 - 100.0 (Schrittweite 0.1) |
| `shift_t` | Der Verschiebungswert, der auf die T-(Zeit-)Komponente des ROPE angewendet wird (Standard: 0.0). | FLOAT | Ja | -256.0 - 256.0 (Schrittweite 0.1) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das Modell mit den neu angewendeten ROPE-Skalierungs- und Verschiebungsparametern. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/de.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
