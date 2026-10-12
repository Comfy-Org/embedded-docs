# RenormCFG

Der RenormCFG-Node modifiziert den Classifier-Free-Guidance-Prozess (CFG) in Diffusionsmodellen durch Anwendung von bedingter Skalierung und Normalisierung. Er passt den Denoising-Prozess basierend auf einem angegebenen Zeitschritt-Schwellenwert und einem Renormalisierungsfaktor an und steuert so den Einfluss von bedingten gegenüber unbedingten Vorhersagen während der Bilderzeugung. Das resultierende Modell wird mit diesem gepatchten CFG-Verhalten zurückgegeben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Diffusionsmodell, auf das renormalisiertes CFG angewendet werden soll | MODEL | Ja | - |
| `cfg_trunc` | Zeitschritt-Schwellenwert für die Anwendung der CFG-Skalierung. Wenn der aktuelle Zeitschritt unter diesem Wert liegt, werden CFG-Skalierung und Renormalisierung angewendet; andernfalls wird nur die bedingte Vorhersage verwendet (Standard: 100.0) | FLOAT | Nein | 0.0 - 100.0 (Schrittweite 0.01) |
| `renorm_cfg` | Renormalisierungsfaktor, der die maximale Norm der CFG-skalierten Vorhersage relativ zur ursprünglichen bedingten Vorhersage begrenzt. Ein Wert von 0.0 deaktiviert die Renormalisierung (Standard: 1.0) | FLOAT | Nein | 0.0 - 100.0 (Schrittweite 0.01) |

Hinweis: `cfg_trunc` und `renorm_cfg` sind erweiterte Parameter. Die Renormalisierung wird nur wirksam, wenn `renorm_cfg` größer als 0.0 ist und der aktuelle Zeitschritt unter `cfg_trunc` liegt; wenn die Norm der neuen Vorhersage bereits unter dem berechneten Maximum liegt, wird keine Neuskalierung durchgeführt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit der angewendeten renormalisierten CFG-Funktion | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/de.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
