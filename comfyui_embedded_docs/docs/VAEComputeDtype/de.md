# VAE Compute Dtype

Dieser Node legt den Compute-Dtype fest, der verwendet wird, wenn ein VAE kodiert oder dekodiert, ohne den restlichen Modellgraphen zu verändern. Er gibt eine Kopie des eingegebenen VAE mit der angeforderten Präzision zurück, sodass ein Workflow einen Zweig mit höherer Präzision ausführen kann, während andere unverändert bleiben. `"default"` behält den Compute-Dtype bei, den das eingegebene VAE bereits verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | VAE, der angepasst werden soll. Der Node arbeitet auf einer Kopie, daher wird der verbundene VAE nicht verändert. | VAE | Ja | - |
| `dtype` | Compute-Dtype für die VAE-Kodierung und -Dekodierung. `"default"` behält den Compute-Dtype des eingegebenen VAE bei (Standard: `"default"`). | COMBO | Ja | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `vae` | Die Kopie des VAE, auf die der ausgewählte Compute-Dtype angewendet wurde. | VAE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/de.md)

---
**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`
