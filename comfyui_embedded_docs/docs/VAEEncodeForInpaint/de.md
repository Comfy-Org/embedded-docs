# VaeEncodeForInpaint

Dieser Node ist für die Kodierung von Bildern in eine latente Repräsentation konzipiert, die für Inpainting-Aufgaben geeignet ist, und integriert zusätzliche Vorverarbeitungsschritte, um das Eingabebild und die Maske für eine optimale Kodierung durch das VAE-Modell anzupassen.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `pixels` | Das zu kodierende Eingabebild. Dieses Bild wird vorverarbeitet und in der Größe angepasst, um vor der Kodierung den vom VAE-Modell erwarteten Eingabedimensionen zu entsprechen. | `IMAGE` |
| `vae` | Das VAE-Modell, das zum Kodieren des Bildes in seine latente Repräsentation verwendet wird. Es spielt eine entscheidende Rolle im Transformationsprozess und bestimmt die Qualität und Eigenschaften des resultierenden latenten Raums. | VAE |
| `mask` | Eine Maske, die die Bereiche des Eingabebildes angibt, die per Inpainting bearbeitet werden sollen. Sie wird verwendet, um das Bild vor der Kodierung zu modifizieren, damit sich das VAE auf die relevanten Bereiche konzentriert. | `MASK` |
| `grow_mask_by` | Gibt an, um wie viel die Inpainting-Maske erweitert werden soll, um nahtlose Übergänge im latenten Raum sicherzustellen. Ein größerer Wert vergrößert den vom Inpainting betroffenen Bereich. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe umfasst die kodierte latente Repräsentation des Bildes und eine Rauschmaske, die beide für nachfolgende Inpainting-Aufgaben entscheidend sind. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/de.md)
