# CLIPAttentionMultiply

Der Node CLIPAttentionMultiply ermöglicht es, den Attention-Mechanismus in CLIP-Modellen anzupassen, indem auf verschiedene Komponenten der Self-Attention-Schichten Multiplikationsfaktoren angewendet werden. Er funktioniert, indem die Gewichte und Bias-Werte der Query-, Key-, Value- und Output-Projektion im Attention-Mechanismus des CLIP-Modells modifiziert werden. Dieser experimentelle Node erstellt eine modifizierte Kopie des eingegebenen CLIP-Modells mit den angegebenen Skalierungsfaktoren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das zu modifizierende CLIP-Modell | CLIP | Ja | - |
| `q` | Multiplikationsfaktor für die Gewichte und Bias-Werte der Query-Projektion (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `k` | Multiplikationsfaktor für die Gewichte und Bias-Werte der Key-Projektion (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `v` | Multiplikationsfaktor für die Gewichte und Bias-Werte der Value-Projektion (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |
| `out` | Multiplikationsfaktor für die Gewichte und Bias-Werte der Output-Projektion (Standard: 1.0) | FLOAT | Ja | 0.0 - 10.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `CLIP` | Gibt ein modifiziertes CLIP-Modell zurück, auf das die angegebenen Attention-Skalierungsfaktoren angewendet wurden | CLIP |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/de.md)

---
**Source fingerprint (SHA-256):** `1f5c437cb4a372dfd69ad3c10e2b8cfc68821e0fe82dcf37df5e6fd64aa0b436`
