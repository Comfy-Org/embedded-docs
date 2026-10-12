# SkipLayerGuidanceSD3

Der SkipLayerGuidanceSD3-Node verbessert die Führung in Richtung detaillierter Struktur, indem er einen zusätzlichen Satz Classifier-Free-Guidance mit übersprungenen Layern anwendet. Diese experimentelle Implementierung ist von Perturbed Attention Guidance inspiriert und funktioniert, indem sie während des negativen Konditionierungsprozesses selektiv bestimmte Layer umgeht, um strukturelle Details in der generierten Ausgabe zu verbessern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die Skip-Layer-Guidance angewendet werden soll | MODEL | Ja | - |
| `layers` | Kommagetrennte Liste der zu überspringenden Layer-Indizes (Standard: "7, 8, 9") | STRING | Ja | - |
| `scale` | Die Stärke des Skip-Layer-Guidance-Effekts (Standard: 3.0) | FLOAT | Ja | 0.0 - 10.0 |
| `start_percent` | Der Startpunkt der Guidance-Anwendung als Prozentsatz der Gesamtschritte (Standard: 0.01) | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Der Endpunkt der Guidance-Anwendung als Prozentsatz der Gesamtschritte (Standard: 0.15) | FLOAT | Ja | 0.0 - 1.0 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter Skip-Layer-Guidance | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/de.md)

---
**Source fingerprint (SHA-256):** `8fba6e3037387e6beab64175099de1c96babdd492609099ba8ad3a49a6c34efe`
