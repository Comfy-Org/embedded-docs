# CFGZeroStar

Der CFGZeroStar-Node wendet eine spezialisierte Guidance-Skalierungstechnik auf Diffusionsmodelle an. Er modifiziert den Classifier-Free-Guidance-Prozess, indem er einen optimierten Skalierungsfaktor auf Basis der Differenz zwischen bedingten und unbedingten Vorhersagen berechnet. Dieser Ansatz passt die endgültige Ausgabe an, um eine verbesserte Kontrolle über den Generierungsprozess zu ermöglichen und gleichzeitig die Modellstabilität zu erhalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, das mit der CFGZeroStar-Guidance-Skalierungstechnik modifiziert werden soll | MODEL | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `patched_model` | Das modifizierte Modell mit angewendeter CFGZeroStar-Guidance-Skalierung | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/de.md)

---
**Source fingerprint (SHA-256):** `4ec70f67eed8aaca964ce3dfb5b650af2f44d34bcde3b74c3886c91e1e8e8cc0`
