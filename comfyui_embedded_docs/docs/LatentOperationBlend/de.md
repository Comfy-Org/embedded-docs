# LatentOperationBlend

Dieser Node erstellt eine Latent-Operation, die ein Latent in Richtung eines Referenz-Latents mischt, und gibt diese Operation zurück, sodass sie in Nodes wie Latent Apply Operation oder Latent Apply Operation CFG eingebunden werden kann. Wenn die Referenz eine andere räumliche Größe hat, wird sie mit Nearest-Neighbor-Interpolation auf das Ziel-Latent skaliert, und eine Referenz mit kleinerem Batch wird wiederholt, um die Ziel-Batch-Größe abzugleichen. Ein Wert von 0 für `strength` lässt das Latent unverändert. Dieser Node ist als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `reference` | Das Latent, in dessen Richtung gemischt werden soll. Seine Samples werden auf das Gerät und den dtype des verarbeiteten Latents gecastet und dann skaliert und wiederholt, um daran angepasst zu werden. | LATENT | Ja | - |
| `strength` | Wie weit in Richtung der Referenz gemischt wird: 0 lässt das Latent unverändert, 1 entspricht dem skalierten Referenz-Latent (Standard: 1.0). | FLOAT | Ja | 0.0 bis 1.0 (Schrittweite 0.0001) |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `operation` | Eine Mischoperation, die auf Latent-Samples angewendet werden kann. | LATENT_OPERATION |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/de.md)

---
**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`
