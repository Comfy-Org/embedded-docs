# ModelSamplingSD3

Dieser Node wendet Sampling-Einstellungen im Stable-Diffusion-3-Stil auf ein Modell an. Er erstellt eine Kopie des Modells und ersetzt dessen Sampling-Methode durch eine flussbasierte Sampling-Konfiguration, die den angegebenen `shift`-Wert verwendet, der steuert, wie die Sampling-Verteilung geformt wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das Eingabemodell, auf das SD3-Sampling-Parameter angewendet werden | MODEL | Ja | - |
| `shift` | Steuert den Sampling-Shift-Parameter (Standard: 3.0) | FLOAT | Ja | 0.0 - 100.0 (step: 0.01) |

Hinweis: Der `shift`-Wert wird zusammen mit einem festen internen Multiplikator von 1000 angewendet. Wenn das ursprüngliche Modell eine Noise-Scale-Einstellung besitzt, wird dieser Wert auf das modifizierte Modell übertragen. Das ursprüngliche Modell wird nicht verändert; eine geklonte und gepatchte Kopie wird zurückgegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das modifizierte Modell mit angewendeten SD3-Sampling-Parametern | MODEL |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/de.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
