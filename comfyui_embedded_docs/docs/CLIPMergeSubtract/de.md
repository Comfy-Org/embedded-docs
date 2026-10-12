# CLIPMergeSubtract

Der Node CLIPMergeSubtract führt eine Modellzusammenführung durch, indem er die Gewichte eines CLIP-Modells von denen eines anderen CLIP-Modells subtrahiert. Er erstellt ein neues CLIP-Modell, indem er das erste Modell klont und anschließend die Key-Patches des zweiten Modells subtrahiert, wobei ein anpassbarer Multiplikator die Stärke der Subtraktion steuert. Dies ermöglicht eine fein abgestimmte Modellmischung, indem bestimmte Eigenschaften aus dem Basismodell entfernt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip1` | Das Basis-CLIP-Modell, das geklont und geändert wird | CLIP | Ja | - |
| `clip2` | Das CLIP-Modell, dessen Key-Patches vom Basismodell subtrahiert werden | CLIP | Ja | - |
| `multiplier` | Steuert die Stärke der Subtraktionsoperation (Standard: 1.0) | FLOAT | Ja | -10.0 bis 10.0 (Schritt: 0.01) |

**Hinweis:** Der Node schließt die Parameter `.position_ids` und `.logit_scale` unabhängig vom Wert des Multiplikators von der Subtraktionsoperation aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `clip` | Das resultierende CLIP-Modell nach der Subtraktion der Gewichte des zweiten Modells vom ersten | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/de.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
