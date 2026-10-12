# ModelComputeDtype

Der Node ModelComputeDtype ändert den Berechnungsdatentyp (Präzision), der von einem Modell während der Verarbeitung verwendet wird. Er erstellt eine Kopie des Eingabemodells und wendet die ausgewählte Präzisionseinstellung an. Je nach Hardware kann dies helfen, Speicherverbrauch und Leistung zu optimieren. Dies ist nützlich zum Debuggen und Testen verschiedener Präzisionskonfigurationen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Eingabemodell, das mit einem neuen Berechnungsdatentyp geändert werden soll | MODEL | Ja | - |
| `dtype` | Der auf das Modell anzuwendende Berechnungsdatentyp (Standard: "default"). Dieser Parameter ist als erweiterte Option gekennzeichnet. | COMBO | Ja | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das geänderte Modell mit angewendetem neuen Berechnungsdatentyp | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/de.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
