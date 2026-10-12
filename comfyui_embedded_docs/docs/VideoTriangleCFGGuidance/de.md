# VideoTriangleCFGGuidance

Der VideoTriangleCFGGuidance-Node wendet ein dreieckiges Skalierungsmuster für Classifier-Free-Guidance (CFG) auf ein Videomodell an. Er variiert die Conditioning-Skala mithilfe einer Dreieckswelle, die zwischen `min_cfg` und der ursprünglichen Conditioning-Skala des Modells oszilliert. Dadurch entsteht ein dynamisches Guidance-Muster, das dazu beitragen kann, die Konsistenz und Qualität der Videogenerierung zu verbessern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Videomodell, auf das die dreieckige CFG-Guidance angewendet werden soll. | MODEL | Ja | - |
| `min_cfg` | Der minimale CFG-Skalierungswert für das dreieckige Muster. Dieser Parameter wird im erweiterten Bereich der Node-Oberfläche angezeigt (Standard: 1.0). | FLOAT | Ja | 0.0 - 100.0 (step: 0.5, round: 0.01) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeter dreieckiger CFG-Guidance. | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/de.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
