# LTXVConditioning

Der LTXVConditioning-Node fügt sowohl positiven als auch negativen Konditionierungseingaben Bildrateninformationen für Videogenerierungsmodelle hinzu. Er nimmt vorhandene Konditionierungsdaten und wendet den angegebenen Bildratenwert auf beide Konditionierungssätze an, sodass sie für die Verarbeitung durch Videomodelle geeignet sind.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierungseingabe, die die Bildrateninformationen erhält | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierungseingabe, die die Bildrateninformationen erhält | CONDITIONING | Ja | - |
| `frame_rate` | Der Bildratenwert, der auf beide Konditionierungssätze angewendet wird (Standard: 25.0) | FLOAT | Ja | 0.0 - 1000.0 (step: 0.01) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierung mit angewendeten Bildrateninformationen | CONDITIONING |
| `negative` | Die negative Konditionierung mit angewendeten Bildrateninformationen | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/de.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
