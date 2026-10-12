# CFG Guider

Der CFG Guider-Node erstellt ein Guidance-System zur Steuerung des Sampling-Prozesses bei der Bilderzeugung. Er nimmt ein Modell zusammen mit positiven und negativen Conditioning-Eingaben entgegen und wendet dann eine Classifier-Free-Guidance-Skala an, um die Generierung in Richtung gewünschter Inhalte zu lenken und unerwünschte Elemente zu vermeiden. Dieser Node gibt ein Guider-Objekt aus, das von Sampling-Nodes verwendet werden kann, um die Richtung der Bilderzeugung zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Modell, das für die Guidance verwendet werden soll | MODEL | Ja | - |
| `positive` | Die positive Konditionierung, die die Generierung in Richtung gewünschter Inhalte lenkt | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, die die Generierung von unerwünschten Inhalten weglenkt | CONDITIONING | Ja | - |
| `cfg` | Die Classifier-Free-Guidance-Skala, die steuert, wie stark die Konditionierung die Generierung beeinflusst (Standard: 8.0) | FLOAT | Ja | 0.0 bis 100.0 (Schritt: 0.1) |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `GUIDER` | Ein Guider-Objekt, das an Sampling-Nodes übergeben werden kann, um den Generierungsprozess zu steuern | GUIDER |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/de.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
