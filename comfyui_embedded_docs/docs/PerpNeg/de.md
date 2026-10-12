# PerpNeg

Der PerpNeg-Node wendet senkrechte negative Guidance auf den Sampling-Prozess eines Modells an. Dieser Node ändert die Konfigurationsfunktion des Modells, um Rauschvorhersagen mithilfe negativer Konditionierung und Skalierungsfaktoren anzupassen. Er ist veraltet und wurde durch den PerpNegGuider-Node mit verbesserter Funktionalität ersetzt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, auf das die senkrechte negative Guidance angewendet werden soll | MODEL | Ja | - |
| `empty_conditioning` | Leere Konditionierung, die für Berechnungen der negativen Guidance verwendet wird | CONDITIONING | Ja | - |
| `neg_scale` | Skalierungsfaktor für die negative Guidance (Standard: 1.0) | FLOAT | Nein | 0.0 - 100.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter senkrechter negativer Guidance | MODEL |

**Hinweis**: Dieser Node ist veraltet und wurde durch PerpNegGuider ersetzt. Er ist als experimentell gekennzeichnet und sollte nicht in Produktions-Workflows verwendet werden.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/de.md)

---
**Source fingerprint (SHA-256):** `016bd9a9a9ee42855c15b3e582ada03557297df9a786d977439edd9d3363a5ba`
