# BasicGuider

Der BasicGuider-Node erstellt einen einfachen Guidance-Mechanismus für den Sampling-Prozess. Er verwendet ein Modell und Konditionierungsdaten als Eingaben und erzeugt ein Guider-Objekt, das verwendet werden kann, um den Generierungsprozess während des Samplings zu steuern. Dieser Node bietet die grundlegende Guidance-Funktionalität, die für eine kontrollierte Generierung erforderlich ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das für die Guidance verwendet werden soll | MODEL | Ja | - |
| `conditioning` | Die Konditionierungsdaten, die den Generierungsprozess steuern | CONDITIONING | Ja | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `GUIDER` | Ein Guider-Objekt, das während des Sampling-Prozesses verwendet werden kann, um die Generierung zu steuern | GUIDER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/de.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
