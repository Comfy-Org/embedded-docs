# ControlNet mit VAE anwenden

Dieser Node wendet ControlNet-Führung auf die Stable-Diffusion-3-Konditionierung an. Er nimmt positive und negative Konditionierungs-Eingaben zusammen mit einem ControlNet-Modell und einem Bild entgegen und wendet dann die Steuerungsführung mit anpassbarer Stärke und Zeitparametern an, um den Generierungsprozess zu beeinflussen.

**Hinweis:** Dieser Node wurde als veraltet markiert und könnte in zukünftigen Versionen entfernt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierung, auf die ControlNet-Führung angewendet werden soll | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung, auf die ControlNet-Führung angewendet werden soll | CONDITIONING | Ja | - |
| `control_net` | Das ControlNet-Modell, das für die Führung verwendet werden soll | CONTROL_NET | Ja | - |
| `vae` | Das im Prozess verwendete VAE-Modell | VAE | Ja | - |
| `image` | Das Eingabebild, das ControlNet als Führung verwenden soll | IMAGE | Ja | - |
| `strength` | Die Stärke des ControlNet-Effekts (Standard: 1.0). Bei Einstellung auf 0.0 überspringt der Node die ControlNet-Anwendung und gibt die Konditionierung unverändert zurück. | FLOAT | Ja | 0.0 - 10.0 |
| `start_percent` | Der Startpunkt im Generierungsprozess, ab dem ControlNet angewendet wird (Standard: 0.0) | FLOAT | Ja | 0.0 - 1.0 |
| `end_percent` | Der Endpunkt im Generierungsprozess, bis zu dem ControlNet angewendet wird (Standard: 1.0) | FLOAT | Ja | 0.0 - 1.0 |

**Hinweis:** Wenn `strength` auf 0.0 gesetzt ist, wird keine ControlNet-Führung angewendet und die Eingabe-Konditionierung wird unverändert an beide Ausgaben weitergegeben.

**Hinweis:** Wenn dieselbe Konditionierung an anderer Stelle wiederverwendet wird und bereits Steuerinformationen enthält, wird das neue ControlNet nach dem vorherigen verknüpft, sodass mehrere ControlNets nacheinander angewendet werden können.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die geänderte positive Konditionierung mit angewendeter ControlNet-Führung | CONDITIONING |
| `negative` | Die geänderte negative Konditionierung mit angewendeter ControlNet-Führung | CONDITIONING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/de.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
