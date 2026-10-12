# SkipLayerGuidanceDiT

Verbessert die Guidance hin zu detaillierter Struktur durch die Verwendung eines weiteren Satzes CFG-negativer Bedingungen mit übersprungenen Layern. Diese generische Version von SkipLayerGuidance kann auf jedem DiT-Modell verwendet werden und ist von Perturbed Attention Guidance inspiriert. Die ursprüngliche experimentelle Implementierung wurde für SD3 erstellt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die Skip-Layer-Guidance angewendet werden soll | MODEL | Ja | - |
| `double_layers` | Kommagetrennte Layer-Nummern für zu überspringende Doppelblöcke (Standard: "7, 8, 9") | STRING | Ja | - |
| `single_layers` | Kommagetrennte Layer-Nummern für zu überspringende Einzelblöcke (Standard: "7, 8, 9") | STRING | Ja | - |
| `scale` | Guidance-Skalierungsfaktor (Standard: 3.0) | FLOAT | Ja | 0.0 - 10.0 |
| `start_percent` | Startprozentsatz für die Anwendung der Guidance (Standard: 0.01) | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Endprozentsatz für die Anwendung der Guidance (Standard: 0.15) | FLOAT | Ja | 0.0 - 1.0 |
| `rescaling_scale` | Skalierungsfaktor für die Neuskalierung zur Anpassung der Ausgabemagnitude (Standard: 0.0, bedeutet keine Neuskalierung) | FLOAT | Ja | 0.0 - 10.0 |

**Hinweis:** Wenn sowohl `double_layers` als auch `single_layers` leer sind (keine Layer-Nummern enthalten), gibt der Node das ursprüngliche Modell zurück, ohne eine Guidance anzuwenden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter Skip-Layer-Guidance | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/de.md)

---
**Source fingerprint (SHA-256):** `35ca97f87913d0efcbb502ca040a8f357da112b202184d8786f63acd76809808`
