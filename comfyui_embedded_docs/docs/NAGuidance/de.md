# NAGuidance

Der NAGuidance-Node wendet Normalized Attention Guidance auf ein Modell an. Diese Technik ermöglicht die Verwendung negativer Prompts mit destillierten oder Schnell-Modellen, indem der Aufmerksamkeitsmechanismus des Modells während des Sampling-Prozesses modifiziert wird, um die Generierung von unerwünschten Konzepten wegzulenken.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das Normalized Attention Guidance angewendet werden soll. | MODEL | Ja | - |
| `nag_scale` | Der Skalierungsfaktor für die Guidance. Höhere Werte treiben die Generierung weiter vom negativen Prompt weg. (Standard: 5.0) | FLOAT | Ja | 0.0 - 50.0 |
| `nag_alpha` | Der Mischungsfaktor für die normalisierte Attention. Ein Wert von 1.0 ersetzt die ursprüngliche Attention vollständig, während 0.0 keine Wirkung hat. (Standard: 0.5) | FLOAT | Ja | 0.0 - 1.0 |
| `nag_tau` | Ein Skalierungsfaktor, der verwendet wird, um das Normalisierungsverhältnis zu begrenzen. (Standard: 1.5) | FLOAT | Ja | 1.0 - 10.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das gepatchte Modell mit aktivierter Normalized Attention Guidance. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/de.md)

---
**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`
