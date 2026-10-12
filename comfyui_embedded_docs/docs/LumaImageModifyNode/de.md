# LumaImageModifyNode

Modifiziert Bilder synchron basierend auf einem Text-Prompt und dem Seitenverhältnis des Originalbilds. Dieser Node nimmt ein Eingabebild entgegen und transformiert es gemäß dem bereitgestellten Prompt, wobei eine konfigurierbare Bildgewichtung verwendet wird, um zu steuern, wie stark das Originalbild verändert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `image` | Das zu modifizierende Eingabebild | IMAGE | Ja | - |
| `prompt` | Prompt für die Bilderzeugung (Standard: "") | STRING | Ja | - |
| `image_weight` | Gewichtung des Bildes; je näher an 1.0, desto weniger wird das Bild modifiziert (Standard: 0.1). Intern wird dieser Wert invertiert (1.0 - image_weight) und zwischen 0.0 und 0.98 begrenzt. | FLOAT | Nein | 0.0-0.98 |
| `model` | Das für die Bildmodifikation zu verwendende Luma-Modell. Verschiedene Modelle haben unterschiedliche Kosten. | STRING | Ja | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` |
| `seed` | Seed, um zu bestimmen, ob der Node erneut ausgeführt werden soll; die tatsächlichen Ergebnisse sind unabhängig vom Seed nicht deterministisch (Standard: 0) | INT | Nein | 0-18446744073709551615 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das vom Luma-Modell generierte modifizierte Bild | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/de.md)

---
**Source fingerprint (SHA-256):** `56b13600f6fb8cd6ff80bc8c8184db059273c2ef648630ff1ef10a7ed6b04b7c`
