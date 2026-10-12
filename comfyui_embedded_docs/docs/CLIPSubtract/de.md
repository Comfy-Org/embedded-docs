# CLIPSubtract

Der CLIPSubtract-Node führt eine Subtraktionsoperation zwischen zwei CLIP-Modellen aus. Er verwendet das erste CLIP-Modell als Basis und subtrahiert die Key-Patches vom zweiten CLIP-Modell, wobei ein optionaler Multiplikator die Stärke der Subtraktion steuert. Dies ermöglicht ein fein abgestimmtes Modell-Blending, indem bestimmte Eigenschaften eines Modells mithilfe eines anderen Modells entfernt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `clip1` | Das Basis-CLIP-Modell, das modifiziert wird | CLIP | Erforderlich | - | - |
| `clip2` | Das CLIP-Modell, dessen Key-Patches vom Basismodell subtrahiert werden | CLIP | Erforderlich | - | - |
| `multiplier` | Steuert die Stärke der Subtraktionsoperation. Positive Werte subtrahieren Merkmale von clip2, negative Werte fügen stattdessen Merkmale hinzu. | FLOAT | Erforderlich | 1.0 | -10.0 bis 10.0, Schrittweite 0.01 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CLIP` | Das resultierende CLIP-Modell nach der Subtraktionsoperation | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/de.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
