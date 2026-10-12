# ControlNetInpaintingAliMamaApply

Der Node ControlNetInpaintingAliMamaApply wendet ControlNet-Konditionierung für Inpainting-Aufgaben an, indem er positive und negative Konditionierung mit einem Steuerbild und einer Maske kombiniert. Er verarbeitet das Eingabebild und die Maske, um modifizierte Konditionierung zu erzeugen, die den Generierungsprozess lenkt und Kontrolle darüber ermöglicht, welche Bereiche des Bildes per Inpainting bearbeitet werden. Der Node unterstützt Stärkeanpassung und Zeitsteuerung, um den Einfluss des ControlNet in verschiedenen Phasen des Generierungsprozesses fein abzustimmen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierung, die die Generierung in Richtung gewünschter Inhalte lenkt | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, die die Generierung weg von unerwünschten Inhalten lenkt | CONDITIONING | Ja | - |
| `control_net` | Das ControlNet-Modell, das zusätzliche Kontrolle über die Generierung bietet | CONTROL_NET | Ja | - |
| `vae` | Der VAE (Variational Autoencoder), der zum Kodieren und Dekodieren von Bildern verwendet wird | VAE | Ja | - |
| `image` | Das Eingabebild, das als Steuerungsvorgabe für das ControlNet dient | IMAGE | Ja | - |
| `mask` | Die Maske, die definiert, welche Bereiche des Bildes mit Inpainting bearbeitet werden sollen | MASK | Ja | - |
| `strength` | Die Stärke des ControlNet-Effekts (Standard: 1.0, Schrittweite: 0.01) | FLOAT | Ja | 0.0 bis 10.0 |
| `start_percent` | Erweiterter Parameter. Der Startpunkt (als Prozentsatz), an dem der Einfluss des ControlNet während der Generierung beginnt (Standard: 0.0, Schrittweite: 0.001) | FLOAT | Ja | 0.0 bis 1.0 |
| `end_percent` | Erweiterter Parameter. Der Endpunkt (als Prozentsatz), an dem der Einfluss des ControlNet während der Generierung endet (Standard: 1.0, Schrittweite: 0.001) | FLOAT | Ja | 0.0 bis 1.0 |

**Hinweis:** Wenn beim ControlNet `concat_mask` aktiviert ist, wird die Maske invertiert und vor der Verarbeitung auf das Bild angewendet; die invertierte Maske wird in die zusätzlichen Konkatenierungsdaten aufgenommen, die an das ControlNet gesendet werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierte positive Konditionierung, bei der ControlNet für Inpainting angewendet wurde | CONDITIONING |
| `negative` | Die modifizierte negative Konditionierung, bei der ControlNet für Inpainting angewendet wurde | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/de.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
